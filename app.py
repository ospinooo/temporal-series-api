import argparse
import logging
import tornado.ioloop
import tornado.web

import controllers

from config import PORT
from config import DEBUG


def make_app():
    routes_rules = [(r"/", controllers.MetadataHandler),
                    (r"/ping", controllers.MetadataHandler),
                    (r"/version", controllers.MetadataHandler),
                    (r"/databases", controllers.DatabaseHandler),
                    (r"/([^/]*)/series", controllers.SeriesHandler),
                    (r"/([^/]*)/measurements", controllers.MeasurementHandler),
                    (r"/([^/]*)/tags", controllers.TagsRequestHandler),
                    (r"/([^/]*)/fields", controllers.FieldsHandler),
                    (r"/([^/]*)/users", controllers.UsersRequestHandler),
                    (r"/([^/]*)/measurement/([^/]*)/data",
                     controllers.DataRequestHandler),
                    (r"/([^/]*)/retention_policy",
                     controllers.RetentionPolicyRequestHandler)]

    return tornado.web.Application(routes_rules, debug=DEBUG)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=1)

    args = parser.parse_args()
    args.verbose = 70 - (10 * args.verbose) if args.verbose > 0 else 0
    return args


if __name__ == "__main__":
    args = get_arguments()
    logging.basicConfig(level=args.verbose,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info("Creating app")
    app = make_app()
    logging.info(f"Listening on port {PORT}")
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
