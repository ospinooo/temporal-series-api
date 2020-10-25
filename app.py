import tornado.ioloop
import tornado.web

from controllers import MetadataHandler
import logging

from config import PORT


def make_app():
    return tornado.web.Application([
        (r"/", MetadataHandler),
    ])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Creating app")
    app = make_app()
    logging.info(f"Listening on port {PORT}")
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
