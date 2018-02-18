#!env/bin/python

import requests
from bs4 import BeautifulSoup
import time

from util import URL

class URLScraper:
  target_url = ''
  url_dict = dict()

  response = None
  soup = None

  def __init__(self, target):
    self.target_url = target

  def url_add_new(self, url, year, month, day):
    """ Helper function to add new data to dictionary """
    self.url_dict[len(self.url_dict)] = URL(url, year, month, day)

  def url_update_content(self, page_number):
    """ Collect data from the given page number """
    if(page_number == 0):
      self.response = requests.get(self.target_url)
    else:
      payload = {'page' : page_number}
      self.response = requests.get(self.target_url, params=payload)
    print '\nScraping in progress..'
    print(self.response.url + '\n')
    self.soup = BeautifulSoup(self.response.text, "html.parser")

  def url_find_all(self):
    """ With the given data go through and find the urls and
    publishing dates and store them in dcitionary """
    for i in range(31):
      ext = ''
      self.url_update_content(i)     # update request content
      for div in self.soup.find_all('span',{"class":"field-content"}):
        if div is not None:
          if div.a is not None:
            ext = div.a.get('href')
          else:
            date = div.contents[0].split(" ")
            self.url_add_new(ext, date[3], date[1], date[2][:-1])
      time.sleep(0) # Avoid flooding servers
    return self.url_dict

  def find_all_links(self):
    """ Find every link """
    links = self.url_find_all()
    return links

