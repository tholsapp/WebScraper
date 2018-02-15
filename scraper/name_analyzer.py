import re
import requests
from bs4 import BeautifulSoup

class NameAnalyzer:
  url = 'http://www.newyorksocialdiary.com/party-pictures'
  ext = '/2007/music-to-our-ears'
  target = url + ext

  caption_list = []
  name_list = []

  def __init__(self, target_url):
    print self.target
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text,'html.parser')
    # Some pages are formatted differently
    for div in soup.find_all('font'):
      self.caption_list.append(div.contents)
    for div in soup.find_all('div',{'class':'photocaption'}):
      self.caption_list.append(div.contents)

  def is_title(self, title):
    return re.match('^([A-Z]\.?)+$',title.strip())

  def parse_name(self, name):
    """Titles are separated from each other and from names with ","
    We don't need these, so we remove them """
    name = name.replace(',',' ')
    # Split name and titles on spaces,
    # combining adjacent spaces
    name = name.split()

    # Return object
    ret_name = {"first":None,
                "middle":None,
                "last":None,
                "titles":[] }

    """ Parsing Logic """
    #First string is always a first name
    ret_name['first'] = name[0]
    if len(name) == 2:  # John Doe
      ret_name['last'] = name[1]
    if len(name)>2: #John Johnson Smith/PhD
      if self.is_title(name[2]): #John Smith PhD
        ret_name['last']   = name[1]
        ret_name['titles'] = name[2:]
      else:#John Johnson Smith, PhD, MD
        ret_name['middle'] = name[1]
        ret_name['last']   = name[2]
        ret_name['titles'] = name[3:]
    return ret_name

  def combine_names(self, names):
    if not names[0]['last']:
      names[0]['last'] = names[1]['last']

  def parse_string(self, string):
    # Names are combined with "&" or "and"
    string = string.replace("&","and")
    # Split names apart
    string = re.split("\s+and\s+",string)
    string = map(self.parse_name,string)
    self.combine_names(string)
    return string

  def print_captions(self):
    for caption in self.caption_list:
      self.name_list.append(self.parse_string(caption[0]))
    for nl in self.name_list:
      for names in nl:
        print names['first'], names['last']


if __name__ == '__main__':
  NameAnalyzer().print_captions()
