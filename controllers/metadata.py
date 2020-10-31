from .default import DefaultRequestHandler

from database.influxdb import db


class MetadataHandler(DefaultRequestHandler):
    def head(self):
        pass

    def get(self):
        self.write({'res': db.ping()})

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