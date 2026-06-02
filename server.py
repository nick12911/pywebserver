from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Serving on http://{HOST}:{PORT}")
server.serve_forever()
