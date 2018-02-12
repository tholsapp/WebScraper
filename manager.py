
import sys

from scraper import Scraper

""" Define the function block """
# Starts the scraper
def run_scraper():
  

# Map the inputs to the function blocks
options = {
    'run-scraper' : run_scraper,
}


if __name__ == '__main__':

  if len(sys.argv) > 1:
    if sys.argv[1] in options:
      options[sys.argv[1]]()
    #scraper = Scraper()
    #scraper.collect_page_content(31)
    #scraper.print_current_content()

    #wait_time = 5

    #for data in datas:
    #main(url, data)
    #time.sleep(wait_time)
  else:
    print "Usage 'python manager.py <arg>'"
