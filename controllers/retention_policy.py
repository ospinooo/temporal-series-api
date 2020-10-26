import json
from database.influxdb import db

from .default import DefaultRequestHandler


class RetentionPolicyRequestHandler(DefaultRequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        res = db.get_list_retention_policies()
        self.write(json.dumps(res))
