import numpy as np
#加载
us = "./us.csv"
uk = "./uk.csv"

#添加
us_data = np.loadtxt(us,delimiter=",",dtype = int)
uk_data = np.loadtxt(uk,delimiter=",",dtype = int)

#拼接两组数据
# zeros_data = np.zeros((us_data.shape)).astype(int)
# ones_data = np.ones((uk_data.shape[0],1)).astype(int)
#
# us_data = np.hstack((us_data,zeros_data))
print(np.zeros((3,2)).astype(int))
print(us_data)
#分别添加一列全为0，1的数组
# us_data = np.hstack((us_data,zeros_data))
# uk_data = np.hstack((uk_data,ones_data))

# print("uk_data:",uk_data,end='\n')
# #拼接两组数据
# final_data = np.hstack((us_data,uk_data))
# print(final_data)
#
# print("shape:",final_data.shape[0])