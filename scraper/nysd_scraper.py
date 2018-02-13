#!env/bin/python

import requests
from bs4 import BeautifulSoup
import time

from data_models import URLDataStructure

URL_BASE = 'http://www.newyorksocialdiary.com'
URL_EXTS = '/party-pictures'

class Scraper:
  target_url = URL_BASE + URL_EXTS
  url_dict = dict()

  response = requests.get(target_url)
  soup = BeautifulSoup(response.text, "html.parser")

  def __init__(self):
    print('---   Starting CS122 Scraper   ---\n')


  def collect_page_content(self, page_number):
    if(page_number == 0):
      self.response = requests.get(self.target_url)
    else:
      payload = {'page' : page_number}
      self.response = requests.get(self.target_url, params=payload)
    print 'Scraping in progress..'
    print(self.response.url)
    print
    self.soup = BeautifulSoup(self.response.text, "html.parser")


  def add_new_url(self, url, year, month, day):
    self.url_dict[len(self.url_dict)] = URLDataStructure(url, year, month, day)

  def collect_all_urls(self):
    """ With the given data go through and find the
        urls and publishing dates and store them in
        dcitionary """
    las_url_ext = ''
    for div in self.soup.find_all('span',{"class":"field-content"}):
      if div is not None:
        if div.a is not None:
          last_url_ext = div.a.get('href')
        else:
          date = div.contents[0].split(" ")
          self.add_new_url(last_url_ext, date[3], date[1], date[2][:-1])
      else:
        print 'Break --- No Content on this page'
        break

  def find_all_urls(self):
    """ With each page within range collect all urls """
    for i in range(31):
      self.collect_page_content(i)
      self.collect_all_urls()
      time.sleep(3) # So we don't flood their server with requests

  def print_valid_urls(self):
    for data in self.url_dict:
      temp = self.url_dict[data]
      if temp.is_valid_url():
        print data, temp.get_url(), temp.get_date()


if __name__ == '__main__':

  scraper = Scraper()
  scraper.find_all_urls()
  scraper.print_valid_urls()

  #wait_time = 5

  #for data in datas:
  #main(url, data)
  #time.sleep(wait_time)
