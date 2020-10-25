import tornado.web


class MetadataHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
