from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime


def get_data(id):

    try:
        url = 'https://github.com/' + id
        
        resp = requests.get(url)
        soup = bs(resp.text, 'html.parser')
        name = soup.select_one('span.p-name').get_text().replace('\n', '').replace(' ', '').lower()
        
        if name == '':
            name = 'No Data'

        nickname = soup.select_one('span.p-nickname').get_text().replace('\n', '').replace(' ', '').lower()
        introduce = soup.select_one('div.p-note').get_text()

        if introduce == '':
            introduce = 'No Data' 
        
        followers = soup.select('span.text-bold')[0].get_text()
        followings = soup.select('span.text-bold')[1].get_text()
        repository = soup.select_one('span.Counter').get_text()
        contribution = soup.select('h2.text-normal')[1].get_text().replace('\n','').replace(' ', '').replace('contributionsinthelastyear', '').replace(',', '')
        time = datetime.now()
            

        return  name, nickname, int(followers), int(followings), int(repository), introduce, str(time)[:19], int(contribution)

    except: return False
    
