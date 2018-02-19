
import re

from util import Name

class NameScraper:
  target_url = ''

  caption_list = []
  name_list = []
  title_list = ['Doctor', 'Director',
                'Assistant', 'Professor', 'Producer', 'Dr.',
                'Chef', 'C-CAP', 'Photographer', 'Executive',
                'Artist', 'President']

  def __init__(self, caption_list):
    self.format_caption_list(caption_list)

  def format_caption_list(self, caption_list):
    """ Formats input for name parser to work """
    last_line = ''
    for cap in caption_list:
      if len(cap) > 0:
        caption = cap[0]
        if isinstance(caption, basestring):
          caption = self.format_caption(caption)
          if len(caption.split()) == 1:
            last_line = last_line + ' ' + caption
          else:
            self.caption_list.append(last_line+caption + ',')
            last_line = ''

  def is_title(self, title):
    return re.match('^([A-Z]\.?)+$',title.strip())

  def parse_name(self, name):
    """Titles are separated from each other and from names with ","
    We don't need these, so we remove them """
    # Split name to process data
    name = name.split()

    ret_name = Name(None, None, None)
    """ Parsing Logic """
    #First string is always a first name
    if len(name) == 2:  # John Doe
      if name[0] != 'and':
        ret_name = Name(name[0], None, name[1])
    elif len(name) == 3:
      if name[0] == 'and':
        ret_name = Name(name[1], None, name[2])
      elif name[0] in self.title_list:
        ret_name = Name(name[1], None, name[2])
      else:
        ret_name = Name(name[0], name[1], name[2])
    elif len(name) == 4:
      if name[0] in self.title_list:
        ret_name = Name(name[1], name[2], name[3])
    return ret_name

  def combine_names(self, names):
    if not names[0]['last']:
      names[0]['last'] = names[1]['last']

  def format_caption(self, string):
    ret = []
    string = string.strip() # Remove any leading/trailing zeros
    string = re.sub(' +',' ',string)  # Remove any duplicate spaces
    string = re.sub('with', ',', string) # Replace all 'with' with ','
    string = re.sub('\([^)]*\)', ' ', string) # Remove anything within paranthesis
    string = re.sub('(!\s+and\s+)(\s+[a-z]\s)', ' ',string)
    return string

  def print_names(self):
    for caption in self.caption_list:
      self.name_list.append(self.parse_string(caption[0]))
    for nl in self.name_list:
      for names in nl:
        print names['first'], names['last']

  def find_all_names(self):
    """ Finds all the names in caption_list """
    name_count = dict()
    for cap in self.caption_list:
      for segment in cap.split(','):
        # Check for Mr. and Mrs. case
        temps = segment.split()
        if temps == 4:
          # If true, append names to caption_list
          if temps[0] == 'Mr.' and temps[2] == 'Mrs.' \
              or temps[0] == 'Mrs.' and temps[2] == 'Mr.':
            self.caption_list.append(temps[0] + ' ' + temps[3])
            self.caption_list.append(tmemps[2] + ' ' + temps[3])
        # parse names in caption_list
        name = self.parse_name(segment)
        if name not in name_count:
          name_count[name] = 1
        else:
          name_count[name] = name_count[name] + 1
    return name_count
