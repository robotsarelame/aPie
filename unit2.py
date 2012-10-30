__author__ = 'miracledelivery'

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os, utils

rot13_template =  os.path.join(os.path.dirname(__file__), 'templates\unit2_rot13.html' )
signup_template = os.path.join(os.path.dirname(__file__), 'templates\unit2_signup.html' )

class BaseHandler(webapp.RequestHandler):
    def render(self, page_template, **values):
        self.response.out.write(template.render(page_template, values))

class Rot13Handler(BaseHandler):
    def get(self):
        self.render(rot13_template)

    def post(self):
        user_text = self.request.get("text")
        converted_text = utils.rot13_converter(user_text)
        self.render(rot13_template, text=utils.escape_html(converted_text))

class SignUpHandler(BaseHandler):
    def get(self):
        self.render(signup_template)

    def post(self, **kwargs):
        pass

app = webapp.WSGIApplication([('/unit2/rot13', Rot13Handler),
                              ('/unit2/signup', SignUpHandler)],
                            debug=True)
