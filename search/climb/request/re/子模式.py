#oding = utf-8
# -*- coding:utf-8 -*-
import re
# string = '<p><div><span>猪八戒</span></div></p>'
string = '<div>如来</div></div></div>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
pattern = re.compile('<div>.*?</div>')
ret = pattern.search(string)
# print(ret)
print(ret.group())

def patternEg(string,r):
    pattern = re.compile(r,re.M)
    ret = pattern.findall(string)
    print(ret.group())

string = '''hate is a beautifui feel
love you very much
love she
love her smile
'''
# r = '^love'

# re.
pattern = re.compile(r'^love',re.M)
ret = pattern.findall(string)
print(ret)
# patternEg(string,r)

string2 = 'I love you,you love me!'
pattern = re.compile(r'love')
# ret = pattern.sub('hate',string2)
#或者
ret = re.sub(pattern,'hate',string2)
print(ret)


string1 = '''<div>沁园春
北国风光
千里冰封
</div>
'''

# . 不能匹配换行符，加了 re.S  .就能匹配换行符了
pattern = re.compile(r'<div>(.+)</div>',re.S)
ret = pattern.findall(string1)
print(ret)


def fn(height):
    # return str(int(height) - 10)
    ret = int(height.group())
    # print(ret)
    return str(ret - 10)
string4 = '我喜欢身高为170的女孩'
# 170 -> 160 减10
pattern = re.compile(r'\d+')
ret = pattern.sub(fn,string4)
print(ret)


