# Emm, err, so true: http://blog.est.im/post/34288214582
import http.server
http.server.BaseHTTPRequestHandler.address_string = lambda x:x.client_address[0]


import bottle

def error_handler(error):
     bottle.response.content_type = 'text/plain; charset=utf-8'
     return '%s - %s ' % (error.status, error.body or '')


class Bottle(bottle.Bottle):
    def __init__(self):
        bottle.Bottle.__init__(self, catchall=False)
        self.error_handler[500] = \
        self.error_handler[404] = \
        self.error_handler[401] = error_handler

