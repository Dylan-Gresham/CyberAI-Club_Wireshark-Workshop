import http.server
import ssl

PORT = 4443

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("127.0.0.1", PORT), handler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

context.minimum_version = ssl.TLSVersion.TLSv1_2
context.maximum_version = ssl.TLSVersion.TLSv1_2

context.set_ciphers("RSA")

context.load_cert_chain(certfile="../server.crt", keyfile="../server.key")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server running on port 4443")

httpd.serve_forever()
