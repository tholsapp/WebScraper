#!env/bin/python

import requests
from bs4 import BeautifulSoup

class CaptionScraper:
  target_url = ''

  def __init__(self,target_url):
    self.target_url = target_url

  def find_all_captions(self):
    captions = []
    r = requests.get(self.target_url)
    soup = BeautifulSoup(r.text, "html.parser")
    # Some pages display captions in different ways
    for cap in soup.find_all('font'):
      captions.append(cap.contents)
    for cap in soup.find_all('div',{"class":"photocaption"}):
      captions.append(cap.contents)
    return captions


