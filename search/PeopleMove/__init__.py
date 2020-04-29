import urllib.parse
import urllib.request
#url = 'https://heat.qq.com/api/getLbsMigrateDataByBeijing.php?city=%E5%8C%97%E4%BA%AC&direction=1&type=6&date=2020-02-13'
url = 'https://heat.qq.com/api/getLbsMigrateDataByBeijing.php?city=%e6%ad%a6%e6%b1%89&direction=1&type=6&date=2020-02-13'
#e58c97e4baac
formdata = {
    'city':'北京',
    'direction':'1',
    'type':'6',
    'data':'2020-02-13',
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}

#构建请求对象
request = urllib.request.Request(url = url,headers=headers)
#处理post表单数据
form_data = urllib.parse.urlencode(formdata).encode()
#print('form_data:',form_data)
#发送请求
response = urllib.request.urlopen(request)#,data=form_data

print(response.read().decode())
