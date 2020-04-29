# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:27:39 2019

@author: tiffa
"""

import os
import pandas as pd
aim_file ="C:\\Users\\tiffa\\Desktop\\17信安2"#aim_Path:装有文件的文件夹
file='C:/Users/tiffa/Desktop/信息安全2班.xlsx'#含有名单的文件
# outfile='C:/Users/tiffa/Desktop/out.xlsx'#空文件来输出
def readname(filePath):
    name = os.listdir(filePath)
    return name
s=''#存放文件夹下全部的文件名
data=pd.read_excel(file)#读取xlsx文件
data1=data['姓名']#读取名单文件，属性为姓名的列（读取名单）
print(data1)
if __name__ == "__main__":
    name = readname(aim_file)
    print(name)
    for i in name:
        #统计文件长度30以下的文件名（含有名字的文件名一般不会超过30）
        if len(i)<30:
            #把多个文件名拼接成一个字符串
            s+=i[:-4:]#去掉文件后缀
    #输出文件夹下面长度在30以内的文件名
    print(s) 
    
    b=[]#把已交和未交写到输出文档对应名字后面
    md=[]#输出未交名单
    yj= []
    # weijiao_count=0
    for i in data1:#获得名字
        if i in s:#如果名字在字符串内
            b.append('已交')
            yj.append(i)

        else:
            b.append('未交')
            md.append(i)
    # r = pd.concat([data, pd.Series(b)], axis=1)
    # r.columns = list(data.columns) + [u'Bool']
    # r.to_excel(outfile, index = False) #数据写入
    # data=pd.read_excel(outfile)
    # print(data)
    print('未交名单:',md,sep='')
    print('已交名单:', yj, sep='')
