#oding = utf-8
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse

print('hello')

# post_url = 'https://fanyi.baidu.com/sug'
post_url = 'https://d.qianzhan.com/yuanqu/?p=%E5%8C%97%E4%BA%AC%E5%B8%82&c=%E6%B5%B7%E6%B7%80%E5%8C%BA&page=4'
# word = input('请输入查询的英文单词:')
#构建post表单数据
#发送请求的过程
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
#构建请求对象
request = urllib.request.Request(url = post_url,headers=headers)
#处理post表单数据
# form_data = urllib.parse.urlencode(form_data).encode()
# print('form_data:',form_data)
#发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())

def request_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.read().decode())
