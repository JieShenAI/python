from bs4 import BeautifulSoup
import requests
import re
url='https://www.baidu.com'
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    #print(r.text[:1000])
except:
    print("爬取失败")
demo=r.text
#print(demo)
soup = BeautifulSoup(demo,"html.parser")
#print (soup.prettify())
# for link in soup.find_all('a'):
#     print(link.get('href'))

# for tag in soup.find_all(True):
#     print(tag.)
#soup.find_all('a','baidu')
text1=soup.find_all(id=re.compile('on'))
soup1 = BeautifulSoup(text1,"html.parser")
print (soup1.prettify())
'''
tag() 等价于 <tag>.find_all
soup() 等价于 soup.find_all
'''


