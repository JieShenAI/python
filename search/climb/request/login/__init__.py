#oding = utf-8
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import http.cookiejar #保存cookie

#真实模拟浏览器，当发送完post请求的时候，将cookie保存到代码中
#创建一个cookiejar对象
cj = http.cookiejar.CookieJar()

#通过cookiejar创建handler
handler = urllib.request.HTTPCookieProcessor(cj)

#根据handler创建一个opener
opener = urllib.request.build_opener(handler)

#参数都用opener发送

post_url = ''

formdata = {
    '':'',
}

headers = {

}

request = urllib.request.Request(url = post_url,headers=headers)

formdata = urllib.request.urlopen(request,data=formdata)

response = urllib.request.urlopen(request,data=formdata,timeout=10)

print(response.read().decode())
print('*' * 50)

get_url = ''#登陆后要访问的url
request = urllib.request.Request(url=get_url,headers=headers)
reponse = opener.open(request)
print(response.read().decode())