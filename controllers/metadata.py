from .default import DefaultRequestHandler


class MetadataHandler(DefaultRequestHandler):
    def head(self):
        pass

    def get(self):
        self.write({'res': self.get_argument('hola', True)})
        self.set_status(404)
        self.send_error()

    def post(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass

    def put(self):
        pass

    def options(self):
        pass