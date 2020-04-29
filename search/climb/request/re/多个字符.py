#oding = utf-8
# -*- coding:utf-8 -*-
import re

def re_match(text,eg):
    ret = re.match(eg,text)
    print(ret.group())
# text = ';123'
# ret = re.search('[\d]?',text)
# print(ret.group())
# + 1个到多个   * 0个到多个  ? 0个或1个


# {m} 匹配m个字符
# text = '123'
# ret = re.search('[\d]{2}',text)
# print(ret.group())

# {m,n} 匹配 m-n 个字符
# text = '123'
# ret = re.search('[\d]{1,3}',text)
# print(ret.group())

#手机号匹配
# text = '15271616200.html'
# # ret = re.search('1[34578]\d{9}\.html',text)
# # print(ret.group())

#验证邮箱
# text = 'taafr@qq.com'
# ret = re.match('\w+@[a-zA-Z0-9]+\.[a-z]+',text)
# print(ret.group())

#验证url
# text = 'https://www.hbut.edu.cn'
# ret = re.match('(http|https|ftp)://[^\s]+.cn',text)
# print(ret.group())

#验证身份证
# text = '42811518880204125x'
# ret = re.match('\d{17}[\dxX]',text)
# print(ret.group())

#****************************************
#开始或结束的语法
#^表示以...开始，在[]表示取反
# text = 'hello'
# ret = re.match('',text)
# print(ret.group())


# re_eg('42811518880204125x','\d{17}[\dxX]')

# re_match('hello','^a')
def re_search(text,match):
    ret = re.search(match,text)
    print(ret.group(1))

# re_search('hello','^(hel)lo')

#$表示以...结尾
# re_match('xxx.@163.com','\w+.@163.com$')

# \ 匹配多个字符串 或表达式

#默认采用贪婪模式，匹配最多的条件
# re_match('0123456','\d+?')
#非贪婪
# re_match('<h1>标题<h1>','<.+?>')

#匹配 0 - 100 , 09不允许出现
# re_match('1001','0|[1-9][0-9]$|100$')

#*****************************************
#转义字符和原生字符
# re_search('apple price is $10','\$\d*')
# re_search('\n','\\\\n')
# re_search('\\n',r'\\n')
# print(r'\\n')#r   raw原生

#***********************************************分组
# re_search('apple\'s price is $99,orange\'s price is $10','(.*)?\$\d+$')

# text = 'apple\'s price is $99,orange\'s price is $10'
# ret = re.search('(.*?)(\$\d+)',text)#(.*)(\$\d+)
# # for i in range(2):
# #     print(ret.group(i))
# # print(ret.group(0,1))
# print(ret.groups())

#find_all 函数
# text = 'apple\'s price is $99,orange\'s price is $10'
# ret = re.findall('\$\d+',text)
# print(ret)

#sub 函数
# text = 'apple\'s price is $99,orange\'s price is $10'
# ret = re.sub('\$\d+','0',text)
# print(ret)

# html = '''
#     <div class="c-abstract">快速查询用户的<em>IP</em>和浏览器、操作系统。可以批量查询<em>IP</em>地址所在地,可以解析域名的多个<em>IP</em>地址。已完美支持IPv6查询。</div>'
# '''
# ret = re.sub('<.*?>','',html)
# print(ret)

#split函数
# text = 'hello&world ni hao!'
# ret = re.split('[^a-zA-Z]',text)
# print(ret)

#compile函数
text = 'the number is 2050'
# r = re.compile('\d+\.?\d*')

#  注释写法，注意，！！！！！！！！！！！！！！！！！！！！！！
r = re.compile(r'''
    \d+#
    \.?#
    \d+#
''',re.VERBOSE)
ret = re.search(r,text)
print(ret.group())


