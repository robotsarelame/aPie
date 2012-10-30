__author__ = 'IGulyaev'

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