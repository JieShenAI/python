import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url0 = 'https://f.qianzhan.com/yuanqu/diqu/440112/?pg='
outfile='C:/Users/tiffa/Desktop/qz2.xls'
data=pd.read_excel(outfile)#读取xlsx文件
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
Columns=['序号','园区名称','省','市','区','详细地址','面积','企业数','详情']+['简介','园区企业名','注册资金','注册时间','经营范围']

for i in range(1,2):
    url = url0 + str(i)
    resp = requests.get(url,headers=header)
    html = resp.text
    soup = BeautifulSoup(html,'html.parser')
    infos = soup.find_all('tr')
    for info in infos:
        all = info.find_all('td')
        b=[]
        for i in all:
            b.append(i.get_text())
        
            if i.get_text()=='详情':
                href=re.findall('/yuanqu/item/\w{0,50}.html',str(i))
                href = 'https://f.qianzhan.com'+str(href[0])
                #进入链接
                
                resp2 = requests.get(href,headers=header,timeout=10)
                html2 = resp2.text
                soup2 = BeautifulSoup(html2,'html.parser')
                jianjie = soup2.find('meta',{'name':'description'}).attrs['content']
                b.append(jianjie)
                temp=b
                minglu = soup2.find('tbody')
                flag=0
                if len(str(minglu))==0:
                    flag=1
                    print('minglu不存在')
                    try:
                        data=pd.read_excel(outfile)#读取xlsx文件
                        df=pd.DataFrame([b],columns=Columns)
                        df=pd.concat([data,df],ignore_index=True)
                        df.to_excel(outfile, index = False) #数据写入
                    except:
                        print('打印出错')
                    continue

                try:    
                #添加公司简介
                    
                    all2 = minglu.find_all('tr')
                    for i in all2:
                        info2 = i.find_all('td')
                        count=0#为了不打印第二页的序号
                        for j in info2:
                            count += 1
                            information =  j.get_text()
                            if count!=1:
                                b.append(information)
                except:
                    b=temp
                
                    #分公司的一行统计完
                try:
                    data=pd.read_excel(outfile)#读取xlsx文件
                    df=pd.DataFrame([b],columns=Columns)
                    df=pd.concat([data,df],ignore_index=True)
                    df.to_excel(outfile, index = False) #数据写入
                except:
                    print('打印出错')
                if flag==1:
                    continue
                    #单个园区第一页爬完，进入链接
                    #从第二个分公司起添加空格
                b = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

        b = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']+[' ',' ',' ',' ']
        try:
            data=pd.read_excel(outfile)#读取xlsx文件
            df=pd.DataFrame([b],columns=Columns)
            df=pd.concat([data,df],ignore_index=True)
            df.to_excel(outfile, index = False) #数据写入
        except:
            pass
    



