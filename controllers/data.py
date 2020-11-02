from controllers.tag import parse_tag_string
import json
import logging
from database.influxdb import db

from .default import DefaultRequestHandler


class DataRequestHandler(DefaultRequestHandler):
    async def get(self, database: str, measurement: str):
        db.switch_database(database)

        fields = self.get_argument('fields')
        fields_str = ', '.join(fields.split(','))

        tags_string = self.get_argument('tags')

        tags = parse_tag_string(tags_string)
        tags_str = "(" + "AND ".join(
            [f'"{k}"' + f"='{v}'" for k, v in tags.items()]) + ")"

        init_dt = self.get_argument('init_dt', None)
        end_dt = self.get_argument('end_dt', None)

        if init_dt is None and end_dt is None:
            time_str = f"time > now() - 1h"
        else:
            time_str = f"time >= '{init_dt}' AND time < '{end_dt}'"

        query = (f"SELECT {fields_str} "
                 f' FROM "{database}"."autogen"."{measurement}"  '
                 f" WHERE {time_str} AND {tags_str}")

        print(query)
        res = db.query(query)
        res = list(res.get_points())
        self.write(json.dumps(res))
