import requests
from bs4 import BeautifulSoup

url = 'https://bj.lianjia.com/ershoufang/pg/'

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
resp = requests.get(url,headers=header)
html = resp.text
soup = BeautifulSoup(html,'html.parser')
#print(soup)
infos = soup.find('div',{'class':'bigImgList'}).find_all('div')
for info in infos:
    try:
    #temp1 = name.find('div',{'class':'price'})
        temp1 = info.find('a',{'class':'img'}).find('div',{'class':'price'}).get_text()
        temp2 = info.find('div',{'class':'info'}).get_text()
        #temp3 = name.find('div',{'class':'info'})
        print(temp1,temp2)
        with open(r'E:\vscode\蓝桥\链家.csv','a',encoding='utf-8') as f:
            f.write('{},{}\n'.format(temp1,temp2))
    except:
        continue

#print(infos)

