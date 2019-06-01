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
print(soup.text.replace('\n', ' ')[0:1000])

print(soup.select(".content"))

for link in soup.select("td.content a"):
    print(link.text)

# links_html = soup.select('td.content a')
# urls = []
# for link in links_html:
#     url = link['href']
#     urls.append(url)
# print(urls)
# go through the soup, grab all the links that we care about. ( td tags with a content class that have an a tag inside them)
links_html = soup.select('td.content a')
# make an empty list called urls.
urls = []
# go through each url, get rid of 'blob/', and give me a link that adds the sub url to the base url. These will be links that actually work.
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)

# creates an empty list called corpus_texts
corpus_texts = []
# for each thing in urls, go through them
for url in urls:
    # print the url first.
    # print(url)
    # open the url and getting the html at it.
    html = request.urlopen(url).read()
    # convert the html we have into something we can use - a bunch of beautiful soup in this case.
    soup = BeautifulSoup(html, "lxml")
    # get all the text that we have. then take all the line breaks and replace them with nothing.
    text = soup.text.replace('\n', '')
    # take the text data and add it to the growing corpus.
    corpus_texts.append(text)
# print out the contents of the thing
print(corpus_texts)
