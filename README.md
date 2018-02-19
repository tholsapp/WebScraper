# WebScraper

This project uses requests and BeautifulSoup to scrape data from New York Social Diary (http://www.newyorksocialdiary.com/)
This website provides photographs from the social events that the socialites might attend. Each photo has a caption that
labels those who appear in the photo.

The scraper finds a unique list of the names of the total people who are annotated in the captions of the photos from the
parties before December 1st, 2014.
http://www.newyorksocialdiary.com/party-pictures


## Setting up the application

It is recommended to set up this project with virtualenv. To download virtualenv, please refer to https://pypi.python.org/pypi/virtualenv

Inorder to setup virtualenv:
```bash
virtualenv env
```

If you decide to not down virtualenv, be sure to download the dependencies: requests and BeautifulSoup
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

All the dependicies should be downloaded and you can now start the application.


## Starting the application

After you have setup the initial project, simply go into the scaper derectory and run:
```bash
python scraper.py
```

WARNING: Running his application takes approximately 30 minutes to run without any sleep intervals through the entire program
Although the sleep interval is set to zero, it is recommended to set this to 2, so that we do not flood the servers for the target url and during testing I found that we got more accurate numbers because it is less likely data will be lost.

The sleep intervals can be found at:
scarper.py     -> ln. 35
url_scraper.py -> ln. 47
