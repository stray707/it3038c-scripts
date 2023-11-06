import requests
from bs4 import BeautifulSoup

URL = 'http://quotes.toscrape.com/page/1/'
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

# Extracting quotes and authors
for quote in soup.find_all('div', class_='quote'):
    quote_text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{quote_text}" - {author}')