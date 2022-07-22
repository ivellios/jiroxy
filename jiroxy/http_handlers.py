from http.server import SimpleHTTPRequestHandler


class JiraHttpRequestHandler(SimpleHTTPRequestHandler):

    def _read_data(self) -> bytes:
        with open("cache.txt", "rb") as f:
            data = f.read()
        return data

    def do_GET(self):
        data = self._read_data()

        self.send_response(200)
        self.end_headers()

        self.wfile.write(data)
