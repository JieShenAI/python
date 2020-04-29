import urllib.parse
import urllib.request
import os
url = 'http://tieba.baidu.com/f?ie=utf-8&'

#输入吧名，输入起始页码，结束密码，然后创建 吧名文件夹，
# 里面是每一页的html，文件名是_page.html
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
ba_name = input('输入爬取的吧名:')
start_page = int(input('爬取起始页码:'))
end_page = int(input('结束页码:'))
#创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)
#循环 依次爬取页面
for page in range(start_page,end_page + 1):
    data = {
        'kw':ba_name,
        'pn':(page - 1) * 50,
    }
    data = urllib.parse.urlencode(data)
    url_temp = url + data
    print(url_temp)
    #构建请求对象
    request = urllib.request.Request(url = url_temp,headers=headers)
    #处理post表单数据
    # form_data = urllib.parse.urlencode(data).encode()
    #发送请求
    print('第%s页开始下载......' % page)
    response = urllib.request.urlopen(request)
    #生成文件名
    filename = ba_name + '_' + str(page) + '.html'

    filepath = ba_name + '/' + filename
    with open(filepath,'wb') as fp:
        fp.write(response.read())
    print('第%s页结束下载......' % page)