from controllers.tag import parse_tag_string
import json
from database.influxdb import db

from .default import DefaultRequestHandler


class SeriesHandler(DefaultRequestHandler):
    async def get(self, database: str):
        measurement = self.get_argument('measurement', None)
        tags_string = self.get_argument('tags', None)

        tags = {}
        if tags_string is not None:
            tags = parse_tag_string(tags_string)

        res = db.get_list_series(database=database,
                                 measurement=measurement,
                                 tags=tags)
        self.write(json.dumps(res))
