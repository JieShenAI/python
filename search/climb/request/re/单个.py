#coding = utf-8
# -*- coding:utf-8 -*-
import re
#匹配某个字符串
# text = "af3@"
# ret = re.search('\W',text)
#
# print(ret.group())

#组合方式，只要满足[]中的字符，就可以匹配
# text = '0731-88888aaaaaadfga3'
# ret = re.match('[\-\d\-]+',text)
# print(ret.group())

#[]代替\d
# text = '0731-dfasf88888aaaaaadfga3'
# ret = re.search('[1-9 ]+',text)
# print(ret.group())

#[]代替\w
text = '073saASW1_-dfasf88888aaaaaadfga3'
ret = re.search('[^a-zA-Z0-9_]+',text)
print(ret.group())