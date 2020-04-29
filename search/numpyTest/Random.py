import numpy as np

#在后续得到的随机数和上次的是一样的
#只要使用随机种子，在本台电脑上，生成的结果永远都是一样的。
np.random.seed(11)
t = np.random.randint(0,20,(3,4))
print(t)