import json
from database.influxdb import db

from .default import DefaultRequestHandler


class UsersRequestHandler(DefaultRequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        res = db.get_list_users()
        self.write(json.dumps(res))
