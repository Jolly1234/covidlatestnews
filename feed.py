import feedparser
import json
from pprint import pprint
from bs4 import BeautifulSoup

url = "http://news.google.com/news?q=covid-19karnataka&hl=en-US&sort=date&gl=US&num=20&output=rss"


def clean(html):
    '''
    Get the text from html and do some cleaning
    '''
    soup = BeautifulSoup(html)
    text = soup.get_text()
    text = text.replace('\xa0', ' ')
    return text


def parsefeed(event,context):
    feeds = feedparser.parse(url).entries
    newslist = [{'Description': clean(f.get("description", "")),'Published Date': f.get("published", ""),
            'Title': f.get("title", ""),
            'Url': f.get("link", "")} for f in feeds]
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(newslist)
    return responseObject


