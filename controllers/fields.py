import logging
import json
from database.influxdb import db

from .default import DefaultRequestHandler


class FieldsHandler(DefaultRequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        measurement = self.get_argument('measurement', None)

        query = "SHOW FIELD KEYS"
        if measurement is not None:
            query += f" FROM {measurement}"

        res = db.query(query)
        res = list(res.get_points())
        self.write(json.dumps(res))
