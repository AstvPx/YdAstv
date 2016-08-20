# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as Bs

def list_home():
    uri = 'http://www.gzastv.com/v/?q=&classid=59'
    rq = requests.get(uri)
    soup = Bs(rq.text, 'html.parser')
    rstli = []
    for ul in soup.find_all('ul', attrs={'class': 'v'}):
        link_tag = ul.find('li', attrs={'class': 'v_link'}).find('a')
        link = link_tag.get('href')
        link_id = str(link).split('/')[-1].replace('.html', '')
        dict_temp = {
            'link': link,
            'link_id': link_id,
            'mobile_link': 'http://cmsas.cdvcloud.com/e/extend/video/video.php?id=' + link_id,
            'title': link_tag.get('title'),
            'thumb': 'http://www.gzastv.com' + ul.find('li', attrs={'class': 'v_thumb'}).find('img').get('src')
        }
        rstli.append(dict_temp)
    return rstli

print list_home()
