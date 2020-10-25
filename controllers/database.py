import json
import tornado.web
from database.influxdb import db


class DatabaseHandler(tornado.web.RequestHandler):
    async def get(self):
        res = db.get_list_database()
        self.write(json.dumps(res))
