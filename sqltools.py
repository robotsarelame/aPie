__author__ = 'IGulyaev'

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os

html_template =  os.path.join(os.path.dirname(__file__), 'templates/sql_tools.html' )

class MainHandler(webapp.RequestHandler):
    def render(self, **values):
        self.response.out.write(template.render(html_template, values))

    def get(self):
        self.render()

    def post(self):
        user_text = self.request.get("text")
        action = self.request.get("action")
        if action == 'up':
            self.render(text=user_text.upper())
        else:
            self.render(text=user_text.lower())

app = webapp.WSGIApplication([('/sqltools', MainHandler)], debug=True)