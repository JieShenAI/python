import urllib.request
import urllib.error
import urllib.parse
import csv
import json

import sys
sys.path.append('E:\analyse\search\PeopleMove\gaode')
from adcode import *
#print(adcodes)

#post_url = 'https://trp.autonavi.com/crossCityStatis/queryCrossCrossLines.do?date=2020-02-13&isIn=false&adcodes%5B%5D=310000'
# post_url = 'https://trp.autonavi.com/crossCityStatis/queryCrossCrossLines.do'
# date = '2020-01-02'
# isIn = True

for i in adcodes:
    citys = i['city']
    for city in citys:
        print(city['name'] + 'loading...')

        date = '2020-01-02'
        isIn = True
        try:
            form_data = {
                'date':date,
                'isIn':isIn,
                'adcodes':city['adcode']
            }
            post_url = 'https://trp.autonavi.com/crossCityStatis/queryCrossCrossLines.do'
            #保护原始url
            post_url_temp = post_url

            #构建请求对象
            headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            'cookie': 'user_unique_id=8b04ffae6fa915a90170437a30be1618; UM_distinctid=170437a43d418-06daf8c483ee85-313f69-144000-170437a43d52bf; SESSION=cae49928-33cc-4e9d-b39f-d06120b2477a; CNZZDATA1256662931=480773626-1581675979-https%253A%252F%252Ftrp.autonavi.com%252F%7C1581724874'
            }
            request = urllib.request.Request(url = post_url_temp,headers=headers)
            #处理post表单数据
            #发送请求

            form_data = urllib.parse.urlencode(form_data).encode()
            print('form_data:', form_data)
            # 发送请求
            response = urllib.request.urlopen(request, data=form_data,timeout=10)
            json_str = response.read().decode()
            #json转python
            py = json.loads(json_str)
            #print(py)
            headers = ['fromCity','toCity','fromAdcode','toAdcode','duration','distance','hot']
            filename = city['name']
            with open('../'+str(filename), 'w', encoding='utf8', newline='') as fp:
                writer = csv.DictWriter(fp, headers)
                # 写入表头信息需要调用writeheader方法
                writer.writeheader()
                writer.writerows(py)
        except urllib.error.HTTPError as e:
            print(e)
            print(e.code)
            continue
        except urllib.error.URLError as e:
            print(e)
            continue