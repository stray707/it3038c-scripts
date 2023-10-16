For this lab, we will be going over the Python package "Beautiful Soup."
This package is designed for web scraping purposes and extracts particular details from HTML and XML files.

We will be going over 3 different features of this package:

- Scraping a particular type of string from the document, in this case, quotes from a sample web page designed for scrape testing.

- Scraping URLs from a web page.

- Detecting and editing specific parts from a web page.

First, we will need to make sure the packages are installed in the project directory using pip:

pip install bs4 requests

Again, this page is designed for scraping, but this can be tested on any html page.
http://quotes.toscrape.com/page/1/

quotescraper.py will print all the quotes found on the web page.

urlscraper.py will scrape the URLs from the page, specifically ones using the HTML 'a' tag.

htmlprettify.py will detect tags from samplepage.html and modify them based on preset tags in the python script. It will output the changes in the console, as well as create a separate sample HTML page in case you don't want to replace anything in the page immediately.