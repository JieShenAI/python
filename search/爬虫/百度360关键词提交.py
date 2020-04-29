import requests
# kv={'wd':'python'}
# r = requests.get("http://www.baidu.com/s",params = kv)
# print(r.status_code)
# print(r.request.url)
# print(r.text[:1000])
keyword = 'python'
try:
    kv={'q':keyword}
    r=requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(r.text[:500])
except:
    print("爬取失败")