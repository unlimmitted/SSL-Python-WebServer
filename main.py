import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import ssl # SSL module
webdir = "."
port = 443
os.chdir(webdir)
srvaddr=('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.socket = ssl.wrap_socket (srvobj.socket, certfile='certificate.crt',keyfile='private.key', server_side=True) # wrap socket
srvobj.serve_forever()