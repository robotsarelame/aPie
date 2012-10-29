from google.appengine.ext import webapp

form ="""
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day in xrange(1,32):
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)

        import datetime
        now = datetime.datetime.now()

        if year in xrange(1900,now.year+1):
            return year

def valid_month(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

    if month:
        if month.lower() in [(m.lower()) for m in months]:
            return month.title()

def escape_html(s):
    import cgi
    return cgi.escape(s, quote=True)


class MainHandler(webapp.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {'error':error,
                                        'month':escape_html(month),
                                        'day':escape_html(day),
                                        'year':escape_html(year)})

    def get(self):
        self.write_form()

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

app = webapp.WSGIApplication([('/', MainHandler), ('/thanks', ThanksHandler)],
                             debug=True)

