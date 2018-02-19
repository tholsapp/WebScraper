#!env/bin/python

import requests
from bs4 import BeautifulSoup
import time

from util import URL
from url_scraper import URLScraper
from caption_scraper import CaptionScraper
from name_scraper import NameScraper

URL_BASE = 'http://www.newyorksocialdiary.com'
URL_EXT = '/party-pictures'
URL_TARGET = URL_BASE + URL_EXT

class Scraper:
  target_url = URL_TARGET
  url_dict = dict()
  name_dict = dict()

  def __init__(self):
    print('---   Starting CS122 Scraper   ---')

  def find_all_names(self):
    print('Finding all links...')
    count = 0
    self.url_dict = URLScraper(self.target_url).find_all_links()
    for val in self.url_dict:
      url = self.url_dict[val]
      if url.is_valid():
        link = URL_BASE + url.get_url()
        print link
        captions = CaptionScraper(link).find_all_captions()
        self.name_dict = NameScraper(captions).find_all_names()
        time.sleep(0)

    with open('output.txt', 'w') as outfile:
      for name in self.name_dict:
        if name is not None \
            and name.first is not None \
            and name.last is not None:
          string = ''
          string += str(self.name_dict[name])
          string += ' ' + name.first + ' ' + name.last + '\n'
          string = string.encode('utf-8')
          print self.name_dict[name], name.first, name.last
          outfile.write(string)
      print len(self.name_dict)


if __name__ == '__main__':

  scraper = Scraper()
  scraper.find_all_names()

