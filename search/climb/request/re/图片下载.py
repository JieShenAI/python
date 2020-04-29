#oding = utf-8
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re


def handle_request(url,page):
    url = url + str(page) + '/'
    # print(url)
    headers = {

    }
    request = urllib.request.Request(url = url,headers=headers)
    return request

def download_page(content):
    pattern = re.compile(r'<div class="thumb"><img src="(.*?).*?"></div>')
    lt = pattern.findall(content)
    print(lt)


def main():
    url = ''
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page,end_page):
        #生成请求对象
        request = handle_request(url,page)
        #发送请求对象，获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        #若编码是utf则不用动

        #解析内容，提取所有的图片链接，下载图片
        download_image(content)
    pass

if __name__ == '__main__':
    main()