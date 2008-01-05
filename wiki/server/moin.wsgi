# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - mod_wsgi driver script

    To use this, add those statements to your Apache's VirtualHost definition:
    
    # this is for icons, css, js (and must match url_prefix from wiki config):
    Alias       /moin_static160/ /usr/share/moin/htdocs/

    # this is the URL http://servername/moin/ you will use later to invoke moin:
    WSGIScriptAlias /moin/ /some/path/moin.wsgi

    # create some wsgi daemons - use someuser.somegroup same as your data_dir:
    WSGIDaemonProcess daemonname user=someuser group=somegroup processes=5 threads=10 maximum-requests=1000
    # umask=0007 does not work for mod_wsgi 1.0rc1, but will work later

    # use the daemons we defined above to process requests!
    WSGIProcessGroup daemonname

    @copyright: 2007 by MoinMoin:ThomasWaldmann
    @license: GNU GPL, see COPYING for details.
"""

# System path configuration
import sys

# Path to MoinMoin package, needed if you installed with --prefix=PREFIX
# or if you did not use setup.py.
## sys.path.insert(0, 'PREFIX/lib/python2.3/site-packages')

# Path of the directory where farmconfig.py is located (if different).
## sys.path.insert(0, '/path/to/farmconfig')

# Path of the directory where wikiconfig.py is located.
# YOU NEED TO CHANGE THIS TO MATCH YOUR SETUP.
sys.path.insert(0, '/path/to/wikiconfig')

from MoinMoin.server.server_wsgi import moinmoinApp as application

