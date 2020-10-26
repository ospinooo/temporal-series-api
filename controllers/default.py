import tornado.web


class DefaultRequestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')