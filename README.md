# SSL Python HTTP Server

>Для хоста на Linux добавьте строку:

``
CGIHTTPRequestHandler.have_fork=False
``

>После строки:

``
srvobj.socket = ssl.wrap_socket (srvobj.socket, certfile='certificate.crt', keyfile='private.key', server_side=True)
``
