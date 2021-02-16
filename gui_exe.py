import cherrypy
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        loader = 'x'
        tmpl = loader.load('gui_exe.html')

        return tmpl.generate(title='Sample').render('html', doctype='html')
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())