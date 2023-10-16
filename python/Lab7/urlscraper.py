import requests
from bs4 import BeautifulSoup

URL = 'http://quotes.toscrape.com/'
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

# Set to store unique URLs
unique_urls = set()

# Extracting URLs from anchor tags
for anchor in soup.find_all('a'):
    href = anchor.get('href')

    # If href is not None and it's relative, makes it absolute instead
    if href and href.startswith("/"):
        href = URL + href.lstrip('/')

    if href:  # Filtering out None or empty hrefs
        unique_urls.add(href)

# Printing unique URLs
for url in unique_urls:
    print(url)