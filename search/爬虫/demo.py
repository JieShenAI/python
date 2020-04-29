# import scrapy

# class MybooksSpider(scrapy.Spider):
#     name = 'mybooks'
#     start_urls = ['http://books.toscrape.com/']

#     def parse(self, response):
#         #提取一页的数据
#         books_name = response.xpath('//img/@alt').extract()
#         books_price = response.xpath('//p[@class="price_color"]/text()').extract()
#         for i, j in zip(books_name, books_price):
#             #美元价格兑换成人民币
#             j = float(j[1:]) * 6.6866
#             #人民币价格保留两位小数
#             j = round(j, 2)
#             yield {
#                 'name': i,
#                 'price': j,
#             }

#         #提取下一页的URL
#         next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
#         if next_url:
#             #用什么方法不是重点，重点在于构造完整的URL
#             next_url = response.urljoin(next_url)
#             yield scrapy.Request(next_url, callback = self.parse)
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
                try:
                    resp2 = requests.get(href,headers=header,timeout=10)
                    html2 = resp2.text
                    soup2 = BeautifulSoup(html2,'html.parser')
                    jianjie = soup2.find('meta',{'name':'description'}).attrs['content']
                    b.append(jianjie)
                    minglu = soup2.find('tbody')
                    all2 = minglu.find_all('tr')
                    
                except:
                    print('跳出循环')
                    try:
                        data=pd.read_excel(outfile)#读取xlsx文件
                        df=pd.DataFrame([b],columns=Columns)
                        df=pd.concat([data,df],ignore_index=True)
                        df.to_excel(outfile, index = False) #数据写入
                    except:
                        pass
                    continue
                #子公司个数
                num = len(all2)
                #添加公司简介
                
                for i in all2:
                    info2 = i.find_all('td')
                    count=0#为了不打印第二页的序号
                    for j in info2:
                        count += 1
                        information =  j.get_text()
                        if count!=1:
                            b.append(information)
                
                    #分公司的一行统计完
                    try:
                        data=pd.read_excel(outfile)#读取xlsx文件
                        df=pd.DataFrame([b],columns=Columns)
                        df=pd.concat([data,df],ignore_index=True)
                        df.to_excel(outfile, index = False) #数据写入
                    except:
                        pass
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
    



#保护
