import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class RedirectHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(302)  # Redirection
            self.send_header('Location', '/Pages/Index.html')  # Chemin vers Page1.html
            self.end_headers()
        else:
            super().do_GET()

# Change le port si nécessaire
port = 8000
os.chdir('D:/KAMGOKO/KabouKabou')  # Change le répertoire de travail
httpd = HTTPServer(('localhost', port), RedirectHandler)
print(f"Serving on http://localhost:{port}")
httpd.serve_forever()
