from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
  html_data = ""

  def do_GET(self):
    self.get_html()
    self.set_headers()
    self.handle_request()

  def get_html(self):
    parsed_name = "/index.html"

    if self.path != "/" and ".html" in self.path :
      parsed_name = self.path.split('/')[1]
      if parsed_name in os.listdir('static/'):
        self.end_headers
      else:
        print("Error not found")
        self.html_data = "ERROR: File not found!"
        return

    # read html file
    cwd = os.getcwd()
    with open(f'{cwd}/static/{parsed_name}', 'r') as h:
      self.html_data = h.read()
      h.close()

  def handle_request(self):
    self.wfile.write(bytes(self.html_data, "utf-8"))

  def set_headers(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.send_header("Content-Length", len(self.html_data))
    self.end_headers()

if __name__ == '__main__':
  serverAddress = ('', 8080)
  server = HTTPServer(serverAddress, RequestHandler)
  server.serve_forever()