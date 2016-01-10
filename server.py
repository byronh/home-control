import tornado.ioloop
import tornado.web

from handlers import DesktopOnHandler, LightsBrightHandler, LightsDimHandler, LightsOffHandler, LightsOnHandler

if __name__ == '__main__':
    settings = {
        'debug': True,
        'port': 8080
    }
    app = tornado.web.Application([
        (r'/api/desktop/on', DesktopOnHandler),
        (r'/api/lights/bright', LightsBrightHandler),
        (r'/api/lights/dim', LightsDimHandler),
        (r'/api/lights/off', LightsOffHandler),
        (r'/api/lights/on', LightsOnHandler),

        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
        (r'/node_modules/(.*)', tornado.web.StaticFileHandler, {'path': 'node_modules'}),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
    ], **settings)

    try:
        app.listen(settings['port'])
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
