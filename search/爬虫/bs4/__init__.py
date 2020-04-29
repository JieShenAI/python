#oding = utf-8
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
#使用方式:可以将一个html文档转换为指定对象，
# 然后通过对象的方法，或者属性去查找指定的内容

# 转化本地文件:
#     soup = BeautifulSoup(open('本地文件'),'lxml')
#转换网络文件
    # soup = BeautifulSoup('字符串类型或者字节类型','lxml')
'''
(1)通过标签名查找
soup.a 查找只能找到第一个标签
(2)获取属性
soup.a.attrs 获取所有的属性和值，返回一个字典
soup.a.attrs['href']
soup.a['href'] 也可简写为
(3)获取内容
soup.a.text
soup.a.string
soup.a.get_text()

如果标签里面还有标签,string获取到的结果为None,
而其他两个可以获取到

(4)find
soup.find('a') 找到第一个符合要求的a
soup.find('a',title="xxx")
soup.find('a',class_="xxx")#class后面一定要加_

不仅soup可以调用，普通的div对象也能调用，会取指定的div里面去查找符合要求的节点
div = soup.find('div')
print(soup.find('p').text)

(5)find_all
lt = soup.find_all('div')
print(len(lt))
不仅soup能调用,普通的对象也能调用
lt.find_all('a')

div = soup.find('div')
print(div.find_all(['p','i','y'])) 找多个

div.find_all('a',limit=2)找到所有去除前2个

(6)select
根据选择器选择指定的内容
常见的选择器:标签选择器，类选择器，id选择器,组合选择器，层级选择器
伪类选择器，属性选择器

a
.dudu
#lala
a,.dud,#lala,.meme 组合
div .dud #lala .meme .xixi 层级
    div > p > a > .lala  只能是下面一级
 input[name='lala']

select选择器返回的永远是列表，需要通过下表提取指定的对象，然后获取属性和节点

不仅soup能调用select，普通对象也能使用select
'''



