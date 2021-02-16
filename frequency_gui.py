import cherrypy
from radio_variables_1 import hihihi
import radio_variables_1
class index(object):
    @cherrypy.expose
    def index(self):
        return """
    <html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            <input type="button" id='send_request' name="send_request_button" value=" run send_request.py " onclick="exec('python send_request.py');">
            <p> %(hihihi)s </p>
            </form>
          </body>
        </html>""" % {"hihihi": hihihi}
    #  radio = 0
    radio_variables_1.radio = 0  # change the value in fileB's namespace
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(index())