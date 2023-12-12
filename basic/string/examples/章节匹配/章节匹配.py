import re
from pprint import pprint

data = open('data.txt').read()
# data = open('data_%d.txt').read()

level = '章节'


def cut(content, value):
    data = re.findall(
        f"(第[一二三四五六七八九十]+{value}.*)\n*([\s\S]*?)(?=第[一二三四五六七八九十]+{value}|\Z)",
        content,
    )
    d = {}
    idx = level.index(value)
    for title, content in data:
        d[title] = content.strip() if idx == len(level) - 1 else cut(content, level[idx + 1])
    return d


res = cut(data, '章')
pprint(res)

# https://blog.csdn.net/sjxgghg/article/details/134947123
