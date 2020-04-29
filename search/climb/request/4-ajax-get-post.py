import urllib.parse
import urllib.request
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
city = input('请输入要查询的城市:')
page = input('请输入第几页:')
size = input('请输入要多少个:')
formdata = {
    'cname':city,
    'pid':'',
    'pageIndex':page,
    'pageSize':size,
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}

#构建请求对象
request = urllib.request.Request(url = url,headers=headers)
#处理post表单数据
form_data = urllib.parse.urlencode(formdata).encode()
print('form_data:',form_data)
#发送请求
response = urllib.request.urlopen(request,data=form_data)

print(response.read().decode())
