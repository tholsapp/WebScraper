#!env/bin/python

import requests
from bs4 import BeautifulSoup
import time

class Person:
  first_name = ''
  last_name = ''

  def __init__(self):
    first_name = ''
    last_name = ''

class Data:
  data = ''

  def __init__(self):
    data = ''

URL_BASE = 'http://www.newyorksocialdiary.com'
URL_EXTS = '/party-pictures'
# datetime.strptime
class Scraper:
  target_url = URL_BASE + URL_EXTS

  response = requests.get(target_url)
  soup = BeautifulSoup(response.text, "html.parser")

  def __init__(self):
    print('Beginning CS122 Scraper...\n')

  """ Collect URLs """
  def find_target_pages(self):
    return

  def is_before_date(self):
    return

  def create_url_mapping():
    return

  def collect_page_content(self, page_number):
    if(page_number == 0):
      self.response = requests.get(self.target_url)
    else:
      payload = {'page' : page_number}
      self.response = requests.get(self.target_url, params=payload)
    print(self.response.url)
    self.soup = BeautifulSoup(self.response.text, "html.parser")

  def print_current_content(self):
    #TODO if page has no links, then there is not <span> class=field-content
    for div in self.soup.find_all('span',{"class": "field-content"}):
      if div is not None:
        if div.a is not None:
          print div.a.get('href')
        else:
          print div.contents
      else:
        break

  """ Collect from URLs """



if __name__ == '__main__':

  scraper = Scraper()
  scraper.collect_page_content(31)
  scraper.print_current_content()

  #wait_time = 5

  #for data in datas:
  #main(url, data)
  #time.sleep(wait_time)
