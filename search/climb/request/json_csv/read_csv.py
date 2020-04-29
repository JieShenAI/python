import csv

def read_csv_demo1():
    with open('../test.csv', 'r', encoding='gbk') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        next(reader)  # 跳到下一行
        for x in reader:
            # 只获取某个属性的数据
            name = x[2]
            age = x[-1]
            print({'name': name, 'age': age})



def read_csv_demo2():
    with open('../test.csv', 'r', encoding='gbk') as fp:
        #使用DictReader创建的reader对象
        #不会包含标题那行的数据
        #reader是一个迭代器，遍历这个迭代器，返回来的是一个 字典
        reader = csv.DictReader(fp)
        for x in reader:
            print({'name':x['name'],'age':x['age']})

if __name__ == '__main__':
    read_csv_demo2()

