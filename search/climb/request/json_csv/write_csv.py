import csv

def write_csv_demo1():
    headers = ['username','age','height']
    value = [
        ('张三',16,170),
        ('李四',18,175),
        ('王五',19,170)
    ]
    #注意newline默认'\n' 自动换行
    with open('../classroom.csv','w',encoding='utf8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(value)


def write_csv_demo2():
    #headers = ['username','age','height']
    headers = ['fromCity', 'toCity', 'fromAdcode', 'toAdcode', 'duration', 'distance', 'hot']
    value = [
        {'username': '张三', 'age':16, 'height':170},
        {'username': '李四', 'age':16, 'height':170},
        {'username': '王五', 'age':16, 'height':170},
    ]
    gaode = [
        {'fromCity': '苏州', 'toCity': '上海', 'fromAdcode': 320500, 'toAdcode': 310000, 'duration': 96.409256, 'distance': 60.35642, 'hot': 25},
        {'fromCity': '上海', 'toCity': '苏州', 'fromAdcode': 310000, 'toAdcode': 320500, 'duration': 94.16591, 'distance': 64.302864, 'hot': 13},
        {'fromCity': '南通', 'toCity': '上海', 'fromAdcode': 320600, 'toAdcode': 310000, 'duration': 166.86824, 'distance': 144.19525, 'hot': 7},
        {'fromCity': '嘉兴', 'toCity': '上海', 'fromAdcode': 330400, 'toAdcode': 310000, 'duration': 116.14116, 'distance': 87.88935, 'hot': 7},
        {'fromCity': '无锡', 'toCity': '上海', 'fromAdcode': 320200, 'toAdcode': 310000, 'duration': 163.64055, 'distance': 144.89748, 'hot': 5},
        {'fromCity': '盐城', 'toCity': '上海', 'fromAdcode': 320900, 'toAdcode': 310000, 'duration': 267.72095, 'distance': 313.7765, 'hot': 4},
        {'fromCity': '南京', 'toCity': '上海', 'fromAdcode': 320100, 'toAdcode': 310000, 'duration': 267.2375, 'distance': 298.25278, 'hot': 4},
        {'fromCity': '上海', 'toCity': '南通', 'fromAdcode': 310000, 'toAdcode': 320600, 'duration': 130.44095, 'distance': 127.9968, 'hot': 4},
        {'fromCity': '杭州', 'toCity': '上海', 'fromAdcode': 330100, 'toAdcode': 310000, 'duration': 224.85477, 'distance': 193.7935, 'hot': 3},
        {'fromCity': '常州', 'toCity': '上海', 'fromAdcode': 320400, 'toAdcode': 310000, 'duration': 202.74414, 'distance': 200.63893, 'hot': 3
         }]

    with open('../classroom.csv', 'w', encoding='utf8', newline='') as fp:
        writer = csv.DictWriter(fp,headers)
        #写入表头信息需要调用writeheader方法
        writer.writeheader()
        writer.writerows(gaode)

if __name__ == '__main__':
    write_csv_demo2()