import sys
sys.path.append('E:\analyse\search\PeopleMove\gaode')
from adcode import *
print(adcodes)

#name = input('city_name:')
def search(adcode,name):
    for i in adcodes:
        citys  = i['city']
        for city in citys:
            if city['adcode']==adcode or city['name'] == name:
                print(city)
                return

adc = [310000,320100,320200,320400,320500,320600,320900,321000,321100,321200,330100,330200,330600,330500,330400,330700,330900,331000,340100,340200,340500,340700,340800,341800,341700,341100]
# search('500000',0)
for i in adc:
    search(str(i),0)





