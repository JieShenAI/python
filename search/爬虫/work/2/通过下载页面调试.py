#coding = utf-8
# -*- coding:utf-8 -*-

import re,requests
import csv
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def request_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request,timeout=10)
    # print(response.read().decode())
    return response.read()

def soup_url(url,header):
    '''

    :param url:
    :param header:
    :return: soup
    '''
    resp = requests.get(url, headers=header,timeout=10)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def load_html(filename,url,headers):
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filename, 'wb') as fp:
        fp.write(response.read())

def read_soup_localhtml(filename):
    soup = BeautifulSoup(open(filename, encoding='utf-8'), 'lxml')
    return soup

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
# soup = read_soup_localhtml('中发智能.html')
# print(soup)
def write_csv_title(path, fieldnames):
    '''

    :param path: 文件路径 str
    :param fieldnames: 为列表
    :return: Null
    '''
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def seek_company_info(soup,headers):
    '''

    :param soup:
    :param headers:
    :return: company_info_url_list
    '''
    company_info_url_list = []
    li  = soup.select('div > div > ul > li')
    for i in li:
        keys = i.attrs.keys()
        for k in keys:
            if k == 'onclick':
                onclick = i.attrs['onclick']
                a,b,c = onclick.split('\'')
                company_info_url = 'https://d.qianzhan.com/yuanqu/YQCompDetail?comId='+b
                company_info_url_list.append(company_info_url)
    return company_info_url_list

#url 没有最后一个数据
# url = 'https://d.qianzhan.com/yuanqu/YQCompDetail?comId=5ad13274d80170f76d1e3c7e1ae4547faf3d2a721a07966888180525479608e9&_=1582440895166'
# url = 'https://d.qianzhan.com/yuanqu/YQCompDetail?comId=a48b158f60f19577482f3fcdb9b4da84335378c0e7c430435ae05db508041c8b&_=1582441030333'

def addDict_write_csv(path,fieldnames,dict):
    '''

    :param path: 文件路径 str
    :param fieldnames: 为列表,它是csv的首行标题栏
    :return: Null
    '''
    with open(path, 'a+',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dict)

def companyInfo_to_write(filename,fieldnames,company_info_url,headers):#
    '''
    不会主动添加标题，需要提前添加好标题
    :param filepath:
    :param fieldnames:
    :param dict:
    :param company_info_url:
    :param headers:
    :return:
    '''
    soup = soup_url(company_info_url,headers)
    tr = soup.find_all('tr')
    Dict = {}
    for i in tr:
        td = i.find_all('td') #列表
        #开始进入
        count = 0
        value = ''
        for t in  td:
            if count == 0:
                key = t.text
                if ('成员信息' in key) or ('股东信息' in key):
                    key = key[:-1:]
            else:
                value += t.text
            count = 1
        Dict[key] = value.replace('\n','')
    addDict_write_csv(filename,fieldnames,Dict)

# fieldnames = ['企业名称', '统一信用代码', '注册号', '法定代表人', '企业类型', '成立日期', '注册资本', '联系电话','公司网站', '注册地址', '经营范围', '所属行业', '股东信息', '成员信息']
#
# url = 'https://d.qianzhan.com/yuanqu/YQCompDetail?comId=5ad13274d80170f76d1e3c7e1ae4547faf3d2a721a07966888180525479608e9'
# write_csv_title('first_info.csv',fieldnames)
# companyInfo_to_write('first_info.csv',fieldnames,url,headers)

def re_search(text,match):
    ret = re.search(match,text)
    return ret.group()
def center_poly(url):
    '''
    从map_url找出中心点和边界点
    :param url:
    :return: （）
    '''
    ploy = 'poly=&'
    if ploy in url:
        #只分割出center
        print(url)
        center = re_search(url,'center=(.*?)&')
        center = center[:-1:]
        return ['('+center[7::]+')']
    else:
        print('多边形地图')
        center = re_search(url, 'center=(.*?)&')
        center = center[:-1:]
        poly = re_search(url, 'poly=(.*?)&')
        poly = poly[:-1:]

        return (center[7::],poly[5::])


url = 'https://d.qianzhan.com/yuanqu/yqmap?center=114.179623,22.691883&zoom=17&poly=114.179557,22.6908;114.178514,22.691125;114.17923,22.692877;114.180737,22.692575;114.180855,22.692391;114.180303,22.6916;114.179557,22.6908&yid=c672af0c00e964eb'

# center_poly(url)
poly = '114.179557,22.6908;114.178514,22.691125;114.17923,22.692877;114.180737,22.692575;114.180855,22.692391;114.180303,22.6916;114.179557,22.6908'
# p = point.split(';')
# L = []
# for i in p:
#     L.append('('+i+')')
# print(L)


# List = ['(114.179557,22.6908)', '(114.178514,22.691125)', '(114.17923,22.692877)', '(114.180737,22.692575)']
# point_str = ''
# for i in List:
#     point_str += i
# print(point_str)
# str = '(114.179557,22.6908)(114.178514,22.691125)(114.17923,22.692877)(114.180737,22.692575)'
# L=[]
# L.append(str)
# print(L)
a = ['('+'dsf'+')']
print(type(a))
poly_list= []
poly_str = poly.split(';')
Polt_Str = ''
for p in poly_str:
    Polt_Str += '(' + p + ')'
poly_list.append(Polt_Str)
# return (center[7::],poly[5::])
print(['(' + 'dsf' + ')'] + poly_list)
