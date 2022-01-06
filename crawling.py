from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime


def get_data(id):
    url = 'https://github.com/' + id

    resp = requests.get(url)
    soup = bs(resp.text, 'html.parser')
    name = soup.select_one('span.p-name').get_text().replace('\n', '').replace(' ', '').lower()
    nickname = soup.select_one('span.p-nickname').get_text().replace('\n', '').replace(' ', '').lower()
    # email = soup.select_one('.u-email.Link--primary').attrs
    # email = soup.find("li", itemprop="email").get_text()
    introduce = soup.select_one('div.p-note').get_text()
    followers = soup.select('span.text-bold')[0].get_text()
    followings = soup.select('span.text-bold')[1].get_text()
    repository = soup.select_one('span.Counter').get_text()

    return name, nickname, followers, followings, repository, introduce


