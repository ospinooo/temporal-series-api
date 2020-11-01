import json
from database.influxdb import db

from .default import DefaultRequestHandler


class SeriesHandler(DefaultRequestHandler):
    async def get(self, database: str):
        measurement = self.get_argument('measurement', None)
        tags_string = self.get_argument('tags', None)

        tags = {}
        if tags_string is not None:
            for tag in tags_string.split(','):
                k, v = tag.split(':')
                tags[k] = v

        res = db.get_list_series(database=database,
                                 measurement=measurement,
                                 tags=tags)
        self.write(json.dumps(res))
