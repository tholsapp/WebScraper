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

  def find_all_urls(self):
    las_url_ext = ''
    for div in self.soup.find_all('span',{"class":"field-content"}):
      if div is not None:
        if div.a is not None:
          last_url_ext = div.a.get('href')
        else:
          date = div.contents[0].split(" ")
          self.url_dict[len(self.url_dict)] = URLDataStructure(last_url_ext, date[3], date[1], date[2][:-1])
      else:
        print 'Break --- No Content on this page'
        break

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



if __name__ == '__main__':

  scraper = Scraper()
  i = 0
  for i in range(30,31):
    time.sleep(2) # Respect urls we are scraping
    scraper.collect_page_content(i)
    scraper.find_all_urls()
    i = i + 1

  for urlds in scraper.url_dict:
    print urlds, scraper.url_dict[urlds].get_url(), scraper.url_dict[urlds].get_date()


  #wait_time = 5

  #for data in datas:
  #main(url, data)
  #time.sleep(wait_time)
