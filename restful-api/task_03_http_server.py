#!/usr/bin/python3
"""
3. Develop a simple API using Python with the `http.server` module
"""
import http.server
import socketserver


PORT = 8000

class Server(http.server.BaseHTTPRequestHandler):
    """ Web server creation """
    def do_GET(self):
        """ get web server  """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
