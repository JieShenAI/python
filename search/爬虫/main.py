import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
# url='https://item.jd.com/2967969.html'
# try:
#     r=requests.get(url)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")
# import requests
# url = "https://fanyi.baidu.com"
# res = requests.get(url)
# print (res.cookies)
# print (type(res.cookies))
# from selenium import webdriver
# import time

# def main():
#     b = webdriver.Chrome()
#     b.get('https://www.baidu.com')
#     time.sleep(5)
#     b.quit()

# if __name__ == '__main__':
#     main()
href = 'https://f.qianzhan.com/yuanqu/item/7e872843fbadf143.html'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
outfile='C:/Users/tiffa/Desktop/qz2.xls'
resp2 = requests.get(href,headers=header,timeout=30)
html2 = resp2.text
soup2 = BeautifulSoup(html2,'html.parser')
jianjie = soup2.find('meta',{'name':'description'}).attrs['content']
minglu = soup2.find('tbody')
all = minglu.find_all('tr')
#子公司个数
num = len(all)
Columns2=['园区企业名','注册资金','注册时间','经营范围']
#columns2 = list(data2.columns) + Columns2
for i in all:
    info2 = i.find_all('td')
    b2=[]
    count=0
    for j in info2:
        count += 1
        information =  j.get_text()
        if count!=1:
            b2.append(information)
    
        #写入文件
        try:
            data2=pd.read_excel(outfile)#读取xlsx文件
            df2=pd.DataFrame([b2],columns=Columns2)
            df2=pd.concat([data2,df2],ignore_index=True)
            df2.to_excel(outfile, index = False) #数据写入
        except:
            pass
        #单个园区第一页爬完，进入链接