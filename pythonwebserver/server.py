from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except FileNotFoundError:
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


print("[STARTING] Starting web server ...")
httpd = HTTPServer(('localhost', 8080), Server)
print("[RUNNING] Web server is running ...")
httpd.serve_forever()
