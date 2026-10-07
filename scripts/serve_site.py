"""Serve the built site under the same path as GitHub Pages."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

SITE = Path(__file__).resolve().parents[1] / 'site'
PREFIX = '/neconyan-docs/'


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', PREFIX)
            self.end_headers()
            return
        if not urlsplit(self.path).path.startswith(PREFIX):
            self.send_error(404)
            return
        self.path = '/' + self.path[len(PREFIX):]
        super().do_GET()

    def log_message(self, format, *args):
        pass


def server(port=0):
    return ThreadingHTTPServer(('127.0.0.1', port), partial(Handler, directory=str(SITE)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=4599)
    args = parser.parse_args()
    with server(args.port) as httpd:
        print(f'Preview: http://127.0.0.1:{httpd.server_port}{PREFIX}', flush=True)
        httpd.serve_forever()
