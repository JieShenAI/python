import urllib.request
import urllib.parse

post_url = 'https://d.qianzhan.com/yuanqu/yqmap?center=116.314538,39.984805&zoom=15&poly=&yid=17783423ab53e35a'

#发送请求的过程
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
#构建请求对象
request = urllib.request.Request(url = post_url,headers=headers)
#处理post表单数据
#form_data = urllib.parse.urlencode(form_data).encode()
#print('form_data:',form_data)
#发送请求
response = urllib.request.urlopen(request)

print(response.read())