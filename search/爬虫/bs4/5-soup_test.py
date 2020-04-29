#oding = utf-8
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

#生成对象
soup = BeautifulSoup(open('python_1.html',encoding= 'utf-8' ),'lxml')
# print(type(soup))
# print(soup.a['title'])#1
# print(soup.a.attrs)
# print(soup.a.attrs['href'])#与1等价
# print(soup.a.text)
# print(soup.a.string)
# print(soup.a.get_text())
# print(soup.div.text)
# print(soup.div.string)#
# print(soup.div.get_text())
# print(soup.find('a'))
# print(soup.find('a',alt='alt'))
# print(soup.find('a',class_='song'))
# div = soup.find('div')
# print(soup.find('p').text)
# div = soup.find('div')
# print(len(div))
# print(div.find_all(['p','i','y'],limit=2))
# print(div)

# print(soup.select('div > name > p')[1])
# print(soup.select('#liqin'))
a = soup.select('#head')[0].find_all('a')
print(a)
for i in a:
    print(i['href'])