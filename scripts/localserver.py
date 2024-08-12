#!/bin/python3
import http.server
import socketserver
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <dir> <port>")
        sys.exit(1)
    
    dir = sys.argv[1]
    port = int(sys.argv[2])
    handler = http.server.SimpleHTTPRequestHandler 
    
    os.chdir(dir)

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running at http://localhost:{port}/")
        httpd.serve_forever()

