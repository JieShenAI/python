import numpy as np
file_path = "./us.csv"
t1 = np.loadtxt(file_path,delimiter=',',dtype="int",skiprows=0)
#t2 = np.loadtxt(file_path,delimiter=',',dtype="int",unpack=True)
#unpack 转置
print(t1)
# print(t1[1])
#取连续的多行
# print(t1[1:])
#取不连续的多行
# print(t1[[1,0]])

#取列
# print(t1[1,:])
# print(t1[2::])
# print(t1[[2,0],:])

# a = t1[1,2]
# print(a)
# print(type(a))
#取多个点(0,0) (2,1)  和平常不一样，要注意
# a = t1[[0,2],[0,1]]
# a = t1[[0,2],1]
# print(a)
