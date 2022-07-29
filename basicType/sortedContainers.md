* 官方文档：https://grantjenks.com/docs/sortedcontainers/sortedlist.html
* Github：https://github.com/grantjenks/python-sortedcontainers



> 引入的原因，在`leetcode`中，可以调用这个这个列表的二分查找



在leetcode中引入

`from sortedcontainers import SortedDict`

> 参考题目：https://leetcode.cn/problems/my-calendar-i/



- [`SortedList.bisect_left()`](https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.bisect_left)
- [`SortedList.bisect_right()`](https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.bisect_right)



比较一下上述两个二分查找的区别：

### 例子1

```
s1 = SortedList("abbcccddddeeeee")
```

```
[(idx,v) for idx,v, in enumerate("abbcccddddeeeee")]
```

> [(0, 'a'), (1, 'b'), (2, 'b'), (3, 'c'), (4, 'c'), (5, 'c'), 
>
> (6, 'd'), (7, 'd'), (8, 'd'), (9, 'd'),
>
>  (10, 'e'), (11, 'e'), (12, 'e'), (13, 'e'), (14, 'e')]

`bisect_left` 返回的是，假设 这个值在列表中，那么它下标位置应该是多少:

* bisect_left , 假设插入在左边
* bisect_right，假设插入在右边

`s1.bisect_left('d')` 

> 6

`s1.bisect_right('d')` 

> 10



### 例子2

```python
s2 = SortedList("abcdef")
```

`s1.bisect_left('d')`  

> 3

`s2.bisect_right('d')`

> 4



## SortedDict

基础的方法查看官方文档

### 应用

假设查找一个比 `v` 小的key，并获得它的值

```python
sd = SortedDict({1:10,2:20,3:30,5:50})
```



```python
 i = sd.bisect_left(4)
 i
```

> 3

> Dict , bisect_left 返回的是下标



要得到对应的值

> i - 1，i 的下表需要减1后才是比当前值小的key

```
sd.item()[i-1][1]
```

