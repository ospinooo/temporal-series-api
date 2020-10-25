from influxdb import InfluxDBClient

from config import INFLUX_HOST
from config import INFLUX_PORT
from config import INFLUX_USER
from config import INFLUX_PASS


def create_connection(host=INFLUX_HOST,
                      port=INFLUX_PORT,
                      username=INFLUX_USER,
                      password=INFLUX_PASS):

    db = InfluxDBClient(host=host,
                        port=port,
                        username=username,
                        password=password)

    return db


db = create_connection()