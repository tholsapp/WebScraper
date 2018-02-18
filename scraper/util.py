
from datetime import date

month = {
    'January'   : 1,
    'February'  : 2,
    'March'     : 3,
    'April'     : 4,
    'May'       : 5,
    'June'      : 6,
    'July'      : 7,
    'August'    : 8,
    'September' : 9,
    'October'   : 10,
    'November'  : 11,
    'December'  : 12,
}


class URL:
  url = ''
  published = date.today()

  def __init__(self, url, y, m, d):
    self.url = url
    self.published = date(int(y), month[m], int(d))

  def get_url(self):
    return self.url

  def get_day(self):
    return self.published.day

  def get_month(self):
    return self.published.month

  def get_year(self):
    return self.published.year

  def get_date(self):
    return '%d-%d-%d' % (self.published.month, self.published.day, self.published.year)

  def set_day(self, day):
    self.day = day

  def set_month(self, month):
    self.month = month

  def set_year(self, year):
    self.year = year

  def is_valid(self):
    """ Requirements specify to not crawl postings prior
        to Decemeber 1, 2014. """
    return self.published <= date(2014, 12, 1)


class Name:
  first = ''
  middle = ''
  last = ''

  def __init__(self, first, middle, last):
    self.first = first
    self.middle = middle
    self.last = last

  def __hash__(self):
      return hash((self.first, self.last))

  def __eq__(self, other):
      return (self.first, self.last) == (other.first, other.last)

  def __ne__(self, other):
    # Not strictly necessary, but to avoid having both x==y and x!=y
    # True at the same time
    return not(self == other)
