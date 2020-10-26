import json
import tornado.web
from database.influxdb import db

from .default import DefaultRequestHandler


class DatabaseHandler(DefaultRequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    async def get(self):
        res = db.get_list_database()
        self.write(json.dumps(res))
