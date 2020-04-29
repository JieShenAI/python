import requests
import os
url='http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E6%9D%A8%E5%B9%82&hs=2&pn=0&spn=0&di=3230&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=2990040806%2C1464273340&os=2005128165%2C843447062&simid=3405666172%2C390740714&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=star&bdtype=11&oriquery=%E6%9D%A8%E5%B9%82&objurl=http%3A%2F%2Fpics0.baidu.com%2Ffeed%2F203fb80e7bec54e776e69255331662554fc26a23.jpeg'
root="E://vscode//蓝桥//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open (path,'wb') as f:
            f.write(r.content)
            f.close()
            print('图片写入完成')
    else:
        print('文件已存在')
except:
    print('爬取失败')
