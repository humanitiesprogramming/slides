# get all the libraries that we need.
from bs4 import BeautifulSoup
from urllib import request

# store the base_url
url = "https://github.com/humanitiesprogramming/scraping-corpus"
# using that url, get the HTML from it.
html = request.urlopen(url).read()
# take the html that we have, and turn it into some beautiful soup that we can work with.
soup = BeautifulSoup(html, 'lxml')

print(soup)