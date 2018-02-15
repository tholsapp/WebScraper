#!env/bin/python

import requests
from bs4 import BeautifulSoup
import time

from data_models import URLDataStructure
from name_analyzer import NameAnalyzer

URL_BASE = 'http://www.newyorksocialdiary.com'
URL_EXT = '/party-pictures'
URL_TARGET = URL_BASE + URL_EXT

class Scraper:
  target_url = URL_TARGET
  url_dict = dict()

  response = requests.get(target_url)
  soup = BeautifulSoup(response.text, "html.parser")

  def __init__(self):
    print('---   Starting CS122 Scraper   ---')

  """ URL SCRAPER """

  def url_add_new(self, url, year, month, day):
    """ Helper function to add new data to dictionary """
    self.url_dict[len(self.url_dict)] = URLDataStructure(url, year, month, day)

  def url_collect_page(self, page_number):
    """ Collect data from the given page number """
    if(page_number == 0):
      self.response = requests.get(self.target_url)
    else:
      payload = {'page' : page_number}
      self.response = requests.get(self.target_url, params=payload)
    print '\nScraping in progress..'
    print(self.response.url + '\n')
    self.soup = BeautifulSoup(self.response.text, "html.parser")

  def url_collect_all(self):
    """ With the given data go through and find the urls and
    publishing dates and store them in dcitionary """
    ext = ''
    for div in self.soup.find_all('span',{"class":"field-content"}):
      if div is not None:
        if div.a is not None:
          ext = div.a.get('href')
        else:
          date = div.contents[0].split(" ")
          self.url_add_new(ext, date[3], date[1], date[2][:-1])
      else:
        print 'Break --- No Content on this page'
        break

  def url_find_all(self):
    """ With each page within range collect all urls """
    for i in range(30,31):
      self.url_collect_page(i)
      self.url_collect_all()
      time.sleep(1) # So we don't flood their server with requests

  def url_print_all(self):
    for data in self.url_dict:
      temp = self.url_dict[data]
      print data, temp.get_url(), temp.get_data()

  def url_print_all_valid(self):
    for data in self.url_dict:
      temp = self.url_dict[data]
      if temp.is_valid():
        print data, temp.get_url(), temp.get_date()

  """ CAPTION SCRAPER """
  def cap_find(self, ext):
    print URL_BASE+ext
    r = requests.get(URL_BASE+ext)
    soup = BeautifulSoup(r.text, "html.parser")
    # Some pages display captions in different ways
    for div in soup.find_all('font'):
      print str(div.contents)
    for div in soup.find_all('div',{"class":"photocaption"}):
      print str(div.contents[0])

  def find_all_names(self, ext):
    NameAnalyzer(URL_BASE + ext).print_captions()


if __name__ == '__main__':

  scraper = Scraper()
  scraper.url_find_all()
  #scraper.url_print_all_valid()

  #scraper.cap_find(scraper.url_dict[0].get_url())

  scraper.find_all_names(scraper.url_dict[0].get_url())

  #for x in scraper.url_dict:
    #scraper.cap_find(scraper.url_dict[x].get_url())

