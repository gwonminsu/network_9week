import socket, os
from socketserver import BaseServer
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from OpenSSL import SSL

class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.use_privatekey_file ('cert.pem')
        ctx.use_certificate_file('cert.pem')
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family, self.socket_type))
        self.server_bind()
        self.server_activate()


class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)


def run_server(HandlerClass = SecureHTTPRequestHandler, ServerClass = SecureHTTPServer):
    server_address = ('', 4443)
    server = ServerClass(server_address, HandlerClass)
    running_address = server.socket.getsockname()
    print (f"Serving HTTPS Server on {running_address[0]}:{running_address[1]} ...")
    server.serve_forever()

if __name__ == '__main__':
    run_server()