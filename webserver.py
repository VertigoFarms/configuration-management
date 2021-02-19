import tornado.ioloop
import tornado.web
import os

class WebServer(tornado.web.Application):
    #  PRIVATE METHODS
    def __init__(self, debug=False):
        location = os.path.dirname(__file__)
        if debug:
            path = "build"
        else:
            path = "dist"

        static_path = os.path.join(location, "client", path, "static")
        template_path = os.path.join(location, "client", path, "templates")

        handlers = [
            (r"/page1", ...),
            (r"/static/(.*)", tornado.Web.StaticFileHandler),
            (r"/", ...)
        ]

        settings = {
            "debug": debug,
            "static_path": static_path,
            "template_path": template_path
        }

        super(WebServer, self).__init__(handlers, **settings)

    #  PUBLIC METHODS
    def start(self, port):
        app = make_app()
        app.listen(port)
        tornado.ioloop.IOLoop.current().start()
