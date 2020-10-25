import logging
import tornado.ioloop
import tornado.web

from controllers import MetadataHandler
from controllers import SeriesHandler
from controllers import DatabaseHandler

from config import PORT
from config import DEBUG


def make_app():
    routes_rules = [(r"/", MetadataHandler), (r"/database", DatabaseHandler),
                    (r"/([^/]*)/series", SeriesHandler)]

    return tornado.web.Application(routes_rules, debug=DEBUG)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Creating app")
    app = make_app()
    logging.info(f"Listening on port {PORT}")
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
