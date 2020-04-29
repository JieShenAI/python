import pandas as pd

file='C:/Users/tiffa/Desktop/qz3.xls'#含有名单的文件


data=pd.read_excel(file)#读取xlsx文件
data1=data['序号']#读取名单文件，属性为姓名的列（读取名单）
num= [i for i in range(1,206)]
num_2 = []
num_3=[]

for i in data1:
    num_2.append(i)

print(num_2)
num_3=[]
for i in num_2:
    if i!=' ':
        num_3.append(i)
print(num_3)
count=0
s=[]
for i in num:
    if i not in num_3:
        count+=1
        s.append(i)
        #print(i)
print(count)
print(s)

        
