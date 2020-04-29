#oding = utf-8
# -*- coding:utf-8 -*-

#oding = utf-8
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def load_html(filename,url,headers):
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filename, 'wb') as fp:
        fp.write(response.read())

def read_soup_localhtml(filename):
    soup = BeautifulSoup(open(filename, encoding='utf-8'), 'lxml')
    return soup
