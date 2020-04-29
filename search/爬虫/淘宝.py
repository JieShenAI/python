import requests
import re
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
cookies='thw=cn; t=3b37823edd60619724888ac682a3fd17; cna=Ft0kFmA3/SYCAXE5uSUBCa9R; uc3=vt3=F8dByuqirFj5jgRpDc0%3D&id2=UNN%2BwPAFqw0WSQ%3D%3D&nk2=qh1Se4%2FBVd8%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; lgc=%5Cu6C88%5Cu67700001; uc4=nk4=0%40qCetrVNCeVC0mrW5%2BPVH2UJiRA%3D%3D&id4=0%40UgQ2hnAAA3SSoaNJ6V2ud7CjkCQR; tracknick=%5Cu6C88%5Cu67700001; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=mECFsvGszvhnRkvgcIgEv%2FnPzifuDTnN7b7Wm5ILC1l84zw5fhfr5tgzQdNkYdfjXxgJMyObmbHpWkS7V6gunA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=6_1; v=0; cookie2=536a6ef08d2d89c7df553d048e7fa82d; _tb_token_=f16d5784e3517; uc1=cookie14=UoTbmhDYmW9aSQ%3D%3D; UM_distinctid=16f3115e69d7b0-0c514a76dc26da-6701b35-144000-16f3115e69e8aa; CNZZDATA1256648337=1199836435-1577071980-%7C1577071980; CNZZDATA1261698472=1661365475-1577072265-%7C1577072265; c_s=1274813293; c_a=121061; CNZZDATA1274813293=1728943913-1577072505-%7C1577072505; isg=BL6-y5sebGkDHbuKOoY-B87qD9QA_4J5JGvLwWjGw4HqC17l0I_SieSjh9fHM3qR; l=dBO3aCVIqffCRevsBOfaKurza77TCIdb8sPzaNbMiICPOD5wxnlVWZcYZiYeCnGVHsnyR3PBVv73BoTF8yCL5ly2WAaZk_DmndC..'
url='https://zhaopin.taobao.com/index.htm?spm=a21bo.2017.201867-links-15.69.5af911d9p0CVmX&aid=121061&cid=1274813293'

def getHTMLText(url):
    r = requests.get(url,timeout = 30,header=headers,cookie=cookies)#
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
    return r.text
getHTMLText(url)
# def parsePage(ilt,html):
#     try:
#         plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
#         tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(tlt[i].split(':')[1])
#             ilt.append([price,title])
#     except:
#         print("404")
# def printGoodsList(ilt):
#     tplt = "{:4}\t{:8}\t{:16}"
#     print(tplt.format("序号","价格","商品名称"))
#     count = 0
#     for g in ilt:
#         count = count + 1
#         print(tplt.format(count,g[0],g[1]))
# def main():
#     goods='书包'+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191221&ie=utf8'
#     depth=2
#     start_url = 'https://s.taobao.com/search?q='+goods
#     infoList = []
#     for i in range(depth):
#         try:
#             url = start_url + '&s=' + str(44*i)
#             html = getHTMLText(url)
#             parsePage(infoList,html)
#         except:
#             continue
#     printGoodsList(infoList)
    
# main()
