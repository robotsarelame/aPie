__author__ = 'miracledelivery'

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import main, os

rot13_template =  os.path.join(os.path.dirname(__file__), 'templates\unit2_rot13.html' )

def convert(char, list):
    length = len(list)
    index = list.index(char)
    offset = index+13
    if offset < length:
        return list[offset]
    else:
        return list[offset-length]

def rot13_converter(text_to_convert):
    if text_to_convert:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        converted =''
        for char in text_to_convert:
            if char in list(alphabet):
                converted += convert(char, list(alphabet))
            elif char in list(alphabet.upper()):
                converted += convert(char, list(alphabet.upper()))
            else:
                converted +=char
        return converted

class BaseHandler(webapp.RequestHandler):
    def render(self, page_template, **values):
        self.response.out.write(template.render(page_template, values))

class Rot13Handler(BaseHandler):
    def get(self):
        self.render(rot13_template, text='')

    def post(self):
        user_text = self.request.get("text")
        converted_text = rot13_converter(user_text)
        self.render(rot13_template, text=main.escape_html(converted_text))

class SignUpHandler(webapp.RequestHandler):
    pass

app = webapp.WSGIApplication([('/unit2/rot13', Rot13Handler),
                                ('/unit2/signup', SignUpHandler)],
    debug=True)
