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

def write_csv_title(path, fieldnames):
    '''

    :param path: 文件路径 str
    :param fieldnames: 为列表
    :return: Null
    '''
    with open(path, 'w', newline='') as csvfile:
        # fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # writer.writerow({'id': tiffany.id, 'name': tiffany.name, 'age': tiffany.age})

def addwrite_csv(path,data_row):
    '''
    特点:可以不用写表头
    :param path:
    :param data_row: 要添加的数据列表
    :return:
    '''
    with open(path, 'a+',newline='') as f:
        csv_write = csv.writer(f)
        # data_row = ["10004","snow",19]
        csv_write.writerow(data_row)

def re_search(text,match):
    ret = re.search(match,text)
    return ret.group()

def addDict_write_csv(path,fieldnames,dict):
    '''

    :param path: 文件路径 str
    :param fieldnames: 为列表,它是csv的首行标题栏
    :return: Null
    '''
    with open(path, 'a+',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dict)


def center_poly(url):
    '''
    从map_url找出中心点和边界点
    :param url:
    :return: （）
    '''
    ploy = 'poly=&'
    if ploy in url:
        #只分割出center
        # print(url)
        center = re_search(url,'center=(.*?)&')
        center = center[:-1:]
        return ['('+center[7::]+')']
    else:
        print('多边形地图')
        center = re_search(url, 'center=(.*?)&')
        center = center[:-1:]
        poly = re_search(url, 'poly=(.*?)&')
        poly = poly[:-1:]
        poly = poly[5::]
        poly_list = []
        poly_str = poly.split(';')
        Polt_Str = ''
        for p in poly_str:
            Polt_Str += '('+p+')'
        poly_list.append(Polt_Str)
        # return (center[7::],poly[5::])
        return ['('+center[7::]+')'] + poly_list

def seek_company_info(url_industrial, headers):
    '''
    通过 url_industrial 找到 company_info_url
    :param soup:
    :param headers:
    :return: company_info_url_list
    '''
    soup = soup_url(url_industrial)
    company_info_url_list = []
    li = soup.select('div > div > ul > li')
    for i in li:
        keys = i.attrs.keys()
        for k in keys:
            if k == 'onclick':
                onclick = i.attrs['onclick']
                a, b, c = onclick.split('\'')
                company_info_url = 'https://d.qianzhan.com/yuanqu/YQCompDetail?comId=' + b
                company_info_url_list.append(company_info_url)
    return company_info_url_list

def company_info_url_list(soup,headers):
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
                    key = key[:4:]
            else:
                value += t.text
            count = 1
        Dict[key] = value.replace('\n','')
    addDict_write_csv(filename,fieldnames,Dict)


#上面函数段


header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

#企业csv的表头
fieldnames = ['园区','企业名称','曾用名', '统一信用代码', '注册号', '法定代表人', '企业类型', '成立日期', '注册资本', '联系电话','公司网站', '注册地址', '经营范围', '所属行业', '股东信息', '成员信息']

title_name = ["序号","园区名称","省份","城市/区","占地面积(亩)","企业数(家)","详情","链接","中心","多个顶点"]

#给 园区.csv 加表头
# write_csv_title('d.qianzhan.com.csv',title_name)

#先给 企业.csv 加表头
# write_csv_title('企业.csv',fieldnames)

for page in range(1,16):
    print('page %d loading...'%page)
    url = 'https://d.qianzhan.com/yuanqu/?p=%e5%8c%97%e4%ba%ac%e5%b8%82&c=%e6%b5%b7%e6%b7%80%e5%8c%ba'
    url += '&page='+str(page)
    soup = soup_url(url,header)
    #找到所有企业
    #能够通过详情跳转
    tr = soup.select('tbody > tr')
    # print(soup.select('tbody > tr'))
    for Td in tr:
        td = Td.find_all('td')
        content = []
        for text in td:
            content.append(text.text)

        url_industrial = Td.find('a')['href']
        url_industrial = 'https://d.qianzhan.com/' + url_industrial
        content.append(url_industrial)
        soup_Url = soup_url(url_industrial,header)
        map_url = soup_Url.find('iframe')['src']
        # for point in center_poly(map_url):
        #     content.append(point)
        #地图边界坐标拼接处
        content += center_poly(map_url)
        addwrite_csv('d.qianzhan.com.csv', content)

        #获取每个园区内含有企业信息的url
        company_info_url_List = company_info_url_list(soup_Url,header)
        # 添加园区名
        # addwrite_csv('企业.csv', str(content[1]))
        industrial_dict = {'园区':str(content[1])}
        addDict_write_csv('企业.csv',fieldnames,industrial_dict)

        # print(content)
        #content[5] == 0 则没必要进去
        if content[5] != '0':
            for info_url in company_info_url_List:
                companyInfo_to_write('企业.csv',fieldnames,info_url,header)
        # 添加空行，以示区别
        addwrite_csv('企业.csv', '')










