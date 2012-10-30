__author__ = 'miracledelivery'

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os, utils

rot13_template =  os.path.join(os.path.dirname(__file__), 'templates/unit2_rot13.html' )
signup_template = os.path.join(os.path.dirname(__file__), 'templates/unit2_signup.html' )

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

class WelcomeUserHandler(webapp.RequestHandler):
    def get(self):
        user = self.request.get('user')
        self.response.out.write("Welcome, %s!!" % user)

class SignUpHandler(BaseHandler):
    def get(self):
        self.render(signup_template)

    def post(self):
        raw_username = self.request.get("username")
        raw_password = self.request.get("password")
        raw_email = self.request.get("email")
        raw_verify = self.request.get("verify")

        username = utils.validate_username(raw_username)
        password = utils.validate_password(raw_password)
        email = utils.validate_email(raw_email)

        if not (username and password and raw_password==raw_verify and email):
            form_values = {'username':raw_username, 'email':raw_email}
            if not username:
                form_values['username_error'] = 'Invalid username!'
            if not password:
                form_values['password_error'] = 'Invalid password!'
            if raw_password!=raw_verify:
                form_values['verify_error'] = "Ooops! Dpesn't match to the password above"
            if not email:
                form_values['email_error'] = "Invalid email address!"
            self.render(signup_template, **form_values)
        else:
            self.redirect("welcome?user=%s" % str(raw_username))

app = webapp.WSGIApplication([('/unit2/rot13', Rot13Handler),
                              ('/unit2/signup', SignUpHandler),
                              ('/unit2/welcome', WelcomeUserHandler)],
                            debug=True)
