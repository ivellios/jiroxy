import os


def serve(server_class, handler_class):
    server_address = ('0.0.0.0', int(os.environ.get("SERVER_PORT", 8000)))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
