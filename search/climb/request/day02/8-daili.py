#oding = utf-8
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse

#创建handler
handler = urllib.request.ProxyHandler({'http':'ip:port'})#实现要补全
#创建opener
opener = urllib.request.build_opener(handler)

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',

}
request = urllib.request.Request(url,headers=headers)

response = opener.open(request)
#print(response.read().decode())

with open('ip.html','wb') as fp:
    fp.write(response.read())

