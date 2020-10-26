import json
from database.influxdb import db

from .default import DefaultRequestHandler


class MeasurementHandler(DefaultRequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        res = db.get_list_measurements()
        self.write(json.dumps(res))
