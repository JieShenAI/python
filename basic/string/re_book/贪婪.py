import re

s = "<b>Hello</b><i>world</i><a b><abc\n\n>"

# 1. 贪婪模式
# 1.1 贪婪模式下，匹配最长的字符串

# .* 匹配任意字符，任意次数
print(
    re.findall("<[.]*>", s)
)

# .*? 匹配任意字符，任意次数，非贪婪模式
print(
    re.findall("<.|\s*?>", s)
)