import json
from database.influxdb import db

from .default import DefaultRequestHandler


class DataRequestHandler(DefaultRequestHandler):
    async def get(self, database: str, measurement: str):
        db.switch_database(database)
        fields = {}
        query = (f"SELECT {','.join(fields)}, "
                 f" FROM '{database}'.'autogen'.'{measurement}'  "
                 f" WHERE time > now() - 1h")
        res = db.query(query)
        self.write(json.dumps(res))
