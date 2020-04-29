#coding = utf-8
# -*- coding:utf-8 -*-
N = int(input())
#data列表记录已经算出过的值，避免重复计算
data = [0]*1001
def dfs(N):
    #data为全局变量，记录下来修改过的data列表的值
    global data
    if(data[N] != 0):
        return data[N]
    if(N == 1):
        return 1
    if(N == 2):
        return 2
    # 把算出来的值添加进data列表
    data[N] = dfs(N-1) + dfs(N-2)
    return dfs(N-1) + dfs(N-2)
print(dfs(N))