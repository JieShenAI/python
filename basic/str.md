# 字符串



## re



```python
import re
res = re.search(r'第(\d+)章'， line)

# 抽取出 \d+ 的值，str类型
# res = match.group(1) if match else None
```

> <u>待续</u>： re从字符串开头开始匹配



* **match(pattern,string)：在字符串开始处匹配模式**
* **search(pattern,string)：在字符串中寻找模式**

获得某个匹配得到的字符串



* `第(.{1,4})章` 使用{2}，{1,4} 限制re匹配字符串的长度



## index

'我喜欢吃西瓜，我喜欢打羽毛球' target = '我'

```
def find_all_index(s, target):
    index_list = []
    index = s.find(target)
    while index != -1:
        index_list.append(index)
        index = s.find(target, index + 1)
    return index_list
```

`find_all_index`: 获得字符串所有target的下标