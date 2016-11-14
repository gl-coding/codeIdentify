import web 
from imgToCode import *

from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "/etc/ssl/server.crt"
CherryPyWSGIServer.ssl_private_key = "/etc/ssl/server.key"

urls = (
    "/", "index",
    "/hello", "Hello"
)

render = web.template.render('templates/')

class index:
     def GET(self):
         name='bob'
         return render.index(name)
         #return 'Hello, world!'

class Hello:
    def GET(self):
        return "get"
    def POST(self):
        tmp = web.input()
        data = web.data()
        convert = ConvertToCode()
        res = convert.webDataToCode(data)
        print res
        return "true"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
