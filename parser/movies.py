import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/?filter=last'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='b-content__inline_item')
    news = []
    for item in items:
        news.append({
            'title': item.find('div', class_='b-content__inline_item-link').find('a').getText(),
            'desc': item.find('div', class_='b-content__inline_item-link').find('div').getText(),
            'link': item.find('div', class_='b-content__inline_item-cover').find('a').get("href")
        })
    return news

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for p in range(1, 3):
            html = get_html(f"https://rezka.ag/page/{p}/?filter=last")
            news.extend(get_data(html.text))
        return news

    else:
        raise Exception("Error 404 of Parser")


print(parser())