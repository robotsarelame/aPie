__author__ = 'miracledelivery'

from google.appengine.ext import webapp
import main

rot13_form="""
<h>Enter the text below:</h1>
<p>
    <form method="post">
        <p><textarea rows="10" cols="45" name="text">%(text)s</textarea></p>
        <br>
        <input type="submit" name="submit_btn" value="Convert">
    </form>
</p>
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

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
        converted =''
        for char in text_to_convert:
            if char in list(alphabet):
                converted += convert(char, list(alphabet))
            elif char in list(alphabet.upper()):
                converted += convert(char, list(alphabet.upper()))
            else:
                converted +=char
        return converted

class Rot13Handler(webapp.RequestHandler):
    def write_rot13_form(self, text=""):
        self.response.out.write(rot13_form % {'text':main.escape_html(text)})

    def get(self, *args):
        self.write_rot13_form()

    def post(self, *args):
        user_text = self.request.get("text")
        converted_text = rot13_converter(user_text)
        self.write_rot13_form(text=converted_text)

app = webapp.WSGIApplication([('/unit2/rot13', Rot13Handler)],
    debug=True)
