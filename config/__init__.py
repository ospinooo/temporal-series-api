import os
from dotenv import load_dotenv
load_dotenv()

PORT = os.getenv("PORT")

INFLUX_HOST = os.getenv("INFLUX_HOST")
INFLUX_PORT = os.getenv("INFLUX_PORT")
INFLUX_USER = os.getenv("INFLUX_USER")
INFLUX_PASS = os.getenv("INFLUX_PASS")
