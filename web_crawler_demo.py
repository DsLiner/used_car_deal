import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://docs.python.org/3/library/csv.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        print(soup)
        for link in soup.select('li > a'):
            href = "http://creativeworks.tistory.com" + link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_article(href)
        page += 1

def get_single_article(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    for contents in soup.select('p > span'):
        print(contents.text)

spider(2)