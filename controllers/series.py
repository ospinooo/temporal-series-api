import json
from database.influxdb import db

from .default import DefaultRequestHandler


class SeriesHandler(DefaultRequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        res = db.get_list_series()
        self.write(json.dumps(res))
