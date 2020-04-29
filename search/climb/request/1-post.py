import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/sug'
word = input('请输入查询的英文单词:')
#构建post表单数据
form_data = {
    'kw':word,
}
#发送请求的过程
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
#构建请求对象
request = urllib.request.Request(url = post_url,headers=headers)
#处理post表单数据
form_data = urllib.parse.urlencode(form_data).encode()
print('form_data:',form_data)
#发送请求
response = urllib.request.urlopen(request,data=form_data)

print(response.read().decode())