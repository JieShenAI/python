#coding = utf-8
# -*- coding:utf-8 -*-
import csv
class student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

tiffany = student(2,'snow',18)
# print(tiffany.name)

    # writer.writerows({'id': tiffany.id, 'name':tiffany.name, 'age': tiffany.age})

fieldnames = ['id', 'name', 'age']
dict = {'id': tiffany.id,'name':tiffany.name, 'age': tiffany.age}


def addDict_write_csv(path,fieldnames,dict):
    '''

    :param path: 文件路径 str
    :param fieldnames: 为列表,它是csv的首行标题栏
    :return: Null
    '''
    with open(path, 'a+',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dict)

def addwrite_csv(path,data_row):
    '''
    特点:可以不用写表头
    :param path:
    :param data_row: 要添加的数据列表
    :return:
    '''
    with open(path, 'a+',newline='') as f:
        csv_write = csv.writer(f)
        # data_row = ["10004","snow",19]
        csv_write.writerow(data_row)

L = [1,2,3,4,5]
addwrite_csv('data.csv','')
addwrite_csv('data.csv',L)
# addDict_write_csv('data.csv',fieldnames,dict)


# def addwrite_csv(path,data_row):
#     with open(path, 'a+',newline='') as f:
#         csv_write = csv.writer(f)
#         # data_row = ["10004","snow",19]
#         csv_write.writerow(data_row)

# def addDict_csv(path,row):


# for i in range(10):
#     addwrite_csv("data.csv")

