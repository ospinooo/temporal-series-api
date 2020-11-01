import json
import logging
from database.influxdb import db

from .default import DefaultRequestHandler


class TagsRequestHandler(DefaultRequestHandler):
    async def get(self, database: str):
        db.switch_database(database)
        query = "SHOW TAG KEYS"
        logging.info(query)
        res = db.query(query)
        res = list(res.get_points())
        self.write(json.dumps(res))


def parse_tag_string(tags_string):
    tags = {}
    for tag in tags_string.split(','):
        k, v = tag.split(':')
        tags[k] = v

    return tags