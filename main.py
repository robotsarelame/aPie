from google.appengine.ext import webapp
#only outputs hello message

class MainHandler(webapp.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {'error':error,
                                        'month':escape_html(month),
                                        'day':escape_html(day),
                                        'year':escape_html(year)})

    def get(self):
        self.response.out.write("Hello, Udacity!")

    def post(self, *args):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form('Ooops! something goes wrong :(', user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp.RequestHandler):
    def get(self, *args):
        self.response.out.write("Thanks! the data is valid!")

app = webapp.WSGIApplication([('/', MainHandler)], debug=True)

