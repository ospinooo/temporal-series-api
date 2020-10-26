from .default import DefaultRequestHandler


class MetadataHandler(DefaultRequestHandler):
    def get(self):
        self.write({"res": "Hello, world"})
