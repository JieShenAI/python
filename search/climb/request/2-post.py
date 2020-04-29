import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'
word = 'wolf'
form_data = {
    'form':'en',
    'to':'zh',
    'query':word,
    'transtype':'realtime',
    'token':'',
    #...
}
headers = {
    #请求头加全
    'Host':'fanyi.baidu.com',
    #'Content-Length':'120',可以不加，会自动算的
    #'''
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    #'Accept-Encoding':'gzip,deflate',#这个头不能加，要不然返回给我们的数据是压缩后的数据

}

request = urllib.request.Request(url = post_url,headers=headers)

formdata = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(request,formdata)
print(response.read().decode())