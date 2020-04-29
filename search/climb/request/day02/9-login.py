#oding = utf-8
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse

#url = 'http://xg.hbut.edu.cn/xg/student/toTableInfo?typeid=info&studentId=1710300522&method=edit'
url = 'http://run.hbut.edu.cn/StuGrade/Index?SemesterName=20182&SemesterNameStr=2018%E5%AD%A6%E5%B9%B4%20%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Cookie':'Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1577678751,1577931700; ASP.NET_SessionId=033gb5jnigffos3vge0bvq14; userObjFullName=xqnKHxY0dy1n05fMzsMCvw%3d%3d; .ASPXAUTH=82FEAF127DB9BF47AA3A10968E8CA8C040346BD975062C7A2D3695056444EE7AB7F515EF228B3578AE081F156FD09412DA356D9226FD421C7A4E220D8E5377487C91EFD2531757F0033DC113FB03E966E00B2702AF62CC3EEBB38062723947D0B220E577C046B94E417BBDF89A1A723FF6851A9B2F6BA8FED6CC3DFA352429D5C689F9BED8233361A3D1480D9789C8F8; Role=hDyQ1ftt1PVWjS0lJlcvzuu6WSkwALe3; CurrentSemaster=hDyQ1ftt1PXrQCHRZpN1NzlZq4d6BDjXuY%2fRcFFxGck%2bP1r6O4PV6A%3d%3d',
}

request = urllib.request.Request(url = url,headers=headers)

response = urllib.request.urlopen(request)
print(response.read().decode())
with open('hbut_scores.html','wb') as fp:
    fp.write(response.read())