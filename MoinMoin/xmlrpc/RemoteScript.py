# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - Remote Script Execution Server part

    @copyright: 2006 MoinMoin:ThomasWaldmann
    @license: GNU GPL, see COPYING for details.
"""

from MoinMoin import log
logging = log.getLogger(__name__)

from MoinMoin.script import MoinScript

def execute(xmlrpcobj, their_secret, argv):
    request = xmlrpcobj.request
    their_secret = xmlrpcobj._instr(their_secret)

    our_secret = request.cfg.remote_script_secret
    if not our_secret:
        return u"No password set"

    if our_secret != their_secret:
        return u"Invalid password"

    try:
        logging.info("RemoteScript argv: %r" % argv)
        MoinScript(argv).run(showtime=0)
    except Exception, err:
        e = str(err)
        logging.error(e)
        return xmlrpcobj._outstr(e)
    return xmlrpcobj._outstr(u"OK")

