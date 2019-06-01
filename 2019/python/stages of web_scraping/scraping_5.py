# get all the libraries that we need.
from bs4 import BeautifulSoup
from urllib import request

# store the base_url
url = "https://github.com/humanitiesprogramming/scraping-corpus"
# using that url, get the HTML from it.
html = request.urlopen(url).read()
# take the html that we have, and turn it into some beautiful soup that we can work with.
soup = BeautifulSoup(html, 'lxml')
# take that soup and find all the anchor tags (the links)
links = soup.find_all('a')[0:10]
# go through the soup and get all the text (first 2000 characters)
text = soup.text[0:2000]

links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href']
    urls.append(url)
print(urls)