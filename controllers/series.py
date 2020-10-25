import json
import tornado.web
from database.influxdb import db


class SeriesHandler(tornado.web.RequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        res = db.get_list_series()
        self.write(json.dumps(res))
