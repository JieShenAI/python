#coding = utf-8
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

#详情里面的数据爬取

# soup = BeautifulSoup(open('气象局小区.html',encoding= 'utf-8' ),'lxml')
# body = soup.find('body')
# body.find('div',id="rightBox")
# print(soup.select('#mapDiv'))
# str = str(soup.select('#mapDiv')[0])
# print(str)
def re_search(text,match):
    ret = re.search(match,text)
    # print(ret.group())
    return ret.group()
# url2 = re_search(str,r'/yuanqu/yqmap\?center=(.+)yid=[a-zA-Z0-9]*')
# print(url2)

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
def soup_url(url,header):
    resp = requests.get(url, headers=header)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup



#/yuanqu/yqmap?center=116.330750,39.947801&zoom=15&poly=&yid=b8d528d942785397
url2 = 'https://d.qianzhan.com/yuanqu/dtl/b8d528d942785397.html'
map_url = soup_url(url2,header).find('iframe')['src']
print(map_url)
print(type(map_url))
# url2 = 'https://d.qianzhan.com/yuanqu/yqmap?center=116.303547,40.043444&zoom=18&poly=116.303084,40.042838;116.304449,40.043335;116.304033,40.044035;116.302647,40.043575;116.303084,40.042838&yid=e27b3f183b4d6a53'
def center_poly(url):
    ploy = 'poly=&'
    if ploy in url:
        #只分割出center
        center = re_search(url,'center=(.*?)&')
        center = center[:-1:]
        return (center[7::])
    else:
        center = re_search(url, 'center=(.*?)&')
        center = center[:-1:]
        poly = re_search(url, 'poly=(.*?)&')
        poly = poly[:-1:]
        print('此图有边界')
        return (center[7::],poly[5::])
print(center_poly(map_url))



