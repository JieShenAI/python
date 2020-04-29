#coding = utf-8
# -*- coding:utf-8 -*-
import json
import pandas as pd

def one(qq_json):
    # qq_json = '{"ec":0,"ui":{"85203507":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=YofgEc2iaJHyyF6jqEbibuAg&amp;s=40&amp;t=1560149628","n":"2班-05-熊家齐-171"},"281412295":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=VFIQqBU4VRjeoPyWickZEGw&amp;s=40&amp;t=1557248567","n":"2班-19-赵浩轩-171"},"348543931":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=U092TYcZfibN5BMuknzuLIQ&amp;s=40&amp;t=1581616998","n":"2班-18-马文杰-171"},"570220785":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=StwibUfqcpibld6IXfA86icVA&amp;s=40&amp;t=1582285468","n":"2班-21-万锴文-171"},"704426491":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=Sw7rGPnKCWKruUvUceldkA&amp;s=40&amp;t=1583995285","n":"2班-34-杨楚云-171"},"714046445":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=E1ZnoQgYN5kR5uzMmO5xYw&amp;s=40&amp;t=1567386140","n":"2班-08-徐铎-171030"},"798102944":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=ILicsmPmNywfmWSW6nmYLMA&amp;s=40&amp;t=1583804342","n":"2班-28-赵茴-171030"},"813529168":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=LAC7U0VNtD2v6tEGRubF0w&amp;s=40&amp;t=1555453221","n":"2班-15-詹畅游-171"},"904840170":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=pn2UBia6aowPsuVAk7XJbsA&amp;s=40&amp;t=1581015054","n":"信安2邢胜泉"},"997046939":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=G9ALXlNwZAHicqZ4yFibj76w&amp;s=40&amp;t=1556491037","n":"2班－22－张羽翔"},"1014523538":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=3OclWh4TQHfdFR0TFdIvYQ&amp;s=40&amp;t=1562154716","n":"2班-04-尹涛-171030"},"1050455763":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=Js0NVeLVxTLIa11BgdzdJA&amp;s=40&amp;t=1584266327","n":"2班-23-宋王启翔-"},"1109551040":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=5se5QRro41VPSFOPYGicjew&amp;s=40&amp;t=1557547000","n":"2班-17-沈阳洋-171"},"1115303014":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=XpXLE4qFX8rS1FsVyOichuQ&amp;s=40&amp;t=1578755161","n":"2班-31-涂若欣-171"},"1150236294":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=hFTam0NGU95sibvKQCxTiaUg&amp;s=40&amp;t=1557470188","n":"信安二班周炘晨"},"1227071686":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=g0t7rnp0Ox1Ba597WeZtlg&amp;s=40&amp;t=1571029070","n":"2班-24-石康-171030"},"1239887042":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=vEyqYjzuj0JcrK6MhBWaFg&amp;s=40&amp;t=1557402306","n":"2班-12-卢伟康-171"},"1256031976":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=8icfzoXKxMXLUkH9awfwUmQ&amp;s=40&amp;t=1581684936","n":"2班-07-叶家豪-171"},"1277054093":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=rhOsVkJZ22baGzWA75Kumw&amp;s=40&amp;t=1566743434","n":"2班-03-周浩-171030"},"1279129340":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=l4ic1BpYv2E1VLrsFKmVnmg&amp;s=40&amp;t=1583479419","n":"2班-33-张璇-152718"},"1450329018":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=JkxnLkIibAXoWjaQZrBNxoA&amp;s=40&amp;t=1584439021","n":"信2章朝阳"},"1452366672":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=IAEIuucSBKj3jry18bp6aw&amp;s=40&amp;t=1583772453","n":"信安2谭杰17103001"},"1536485943":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=lrgJcib7lbctfz5SIp8hCcQ&amp;s=40&amp;t=1583820156","n":"2班-11-聂仁杰-171"},"1619432296":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=hw5EzNZEPFY2TBTZUFnbmQ&amp;s=40&amp;t=1556980764","n":"2班-27-许梦娇-171"},"1668774679":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=qgqyII4QOtbziaBwsibpVibuQ&amp;s=40&amp;t=1581766205","n":"阙超"},"1714877904":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=lQHB9eoQVbRg86WoEIpWzw&amp;s=40&amp;t=1579847845","n":"2班-21-刘潇-171030"},"1797485264":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=mw4Nl0pbqib6Z8us5LfA9SQ&amp;s=40&amp;t=1583312197","n":"2班-26-肖越-171083"},"1849791380":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=qZpXjd3q9Ix0kjxCm6EwEA&amp;s=40&amp;t=1556746231","n":"2班-35-胡章文-161"},"1970714059":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=CHvUpUQCwfXo5UIMicEVcvw&amp;s=40&amp;t=1559881270","n":"2班-06-郑一凡-171"},"1973563031":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=10ib56Yzic4LN1atOGapXpQA&amp;s=40&amp;t=1583681662","n":"2班-01-田昊-171010"},"2294738830":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=ticyn9YB6YZwQqib4GrATxOw&amp;s=40&amp;t=1584143838","n":"2班-13-贤昌民-171"},"2360467524":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=21SFY9LZUSI4ETOLtNpv7A&amp;s=40&amp;t=1572421649","n":"2班-09-沈杰-171030"},"2967106259":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=vPicI1Uq4aTYIWMHic0ptUNw&amp;s=40&amp;t=1575559498","n":"2班－32－马晓旭"},"3192476880":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=IicyOBE07m11BC4T0nzu9IA&amp;s=40&amp;t=1584589485","n":"2班-29-余婷-171030"},"3315371762":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&amp;k=Po0iaE6zjCo14LibsORvJXRw&amp;s=40&amp;t=1584144285","n":"2班-30-杨银淼-171"}}}'
    dict = json.loads(qq_json)
    ui = dict['ui']
    n = ''
    for u in ui:
        content = ui[u]
        for c in content:
            if c == 'n':
                # print(content[c])
                n += content[c]
    return n

def get_name(str):
    file = 'C:/Users/tiffa/Desktop/信息安全2班.xlsx'  # 含有名单的文件
    data = pd.read_excel(file)  # 读取xlsx文件
    data1 = data['姓名']  # 读取名单文件，属性为姓名的列（读取名单）
    not_vote = []
    vote = []
    for i in data1:#获得名字
        if i in str:#如果名字在字符串内
            vote.append(i)
            print(i,"已投票")
        else:
            not_vote.append(i)
            print(i, "******************未投票")
    return vote,not_vote

def xinan_1():
    json_str = input()
    str = one(json_str)
    print("投票人：", str)
    # a, b = get_name(str)

    file = 'C:/Users/tiffa/Desktop/信息安全1班.xlsx'  # 含有名单的文件
    data = pd.read_excel(file)  # 读取xlsx文件
    data1 = data['姓名']  # 读取名单文件，属性为姓名的列（读取名单）
    not_vote = []
    vote = []
    for i in data1:  # 获得名字
        if i in str:  # 如果名字在字符串内
            vote.append(i)
            print(i, "已投票")
        else:
            not_vote.append(i)
            print(i, "******************未投票")
    if len(vote) == 34:
        print('所有成员全部投票完毕')
    else:
        print(34 - len(vote), "人还未投票，名单如下")
        print(not_vote)
    # return vote, not_vote
if __name__ == '__main__':
    # json_str = '{"ec":0,"ui":{"85203507":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=YofgEc2iaJHyyF6jqEbibuAg&s=40&t=1560149628","n":"2班-05-熊家齐-171"},"281412295":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=VFIQqBU4VRjeoPyWickZEGw&s=40&t=1557248567","n":"2班-19-赵浩轩-171"},"348543931":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=U092TYcZfibN5BMuknzuLIQ&s=40&t=1581616998","n":"2班-18-马文杰-171"},"377859553":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=aToTVrHl5GhsTflT4uAYsg&s=40&t=1556367003","n":"1班-25-解世伟-161"},"570220785":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=StwibUfqcpibld6IXfA86icVA&s=40&t=1582285468","n":"2班-21-万锴文-171"},"704426491":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=Sw7rGPnKCWKruUvUceldkA&s=40&t=1583995285","n":"2班-34-杨楚云-171"},"714046445":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=E1ZnoQgYN5kR5uzMmO5xYw&s=40&t=1567386140","n":"2班-08-徐铎-171030"},"798102944":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=ILicsmPmNywfmWSW6nmYLMA&s=40&t=1583804342","n":"2班-28-赵茴-171030"},"813529168":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=LAC7U0VNtD2v6tEGRubF0w&s=40&t=1555453221","n":"2班-15-詹畅游-171"},"904840170":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=pn2UBia6aowPsuVAk7XJbsA&s=40&t=1581015054","n":"信安2邢胜泉"},"997046939":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=G9ALXlNwZAHicqZ4yFibj76w&s=40&t=1556491037","n":"2班－22－张羽翔"},"1014523538":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=3OclWh4TQHfdFR0TFdIvYQ&s=40&t=1562154716","n":"2班-04-尹涛-171030"},"1050455763":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=Js0NVeLVxTLIa11BgdzdJA&s=40&t=1584266327","n":"2班-23-宋王启翔-"},"1109551040":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=5se5QRro41VPSFOPYGicjew&s=40&t=1557547000","n":"2班-17-沈阳洋-171"},"1115303014":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=XpXLE4qFX8rS1FsVyOichuQ&s=40&t=1578755161","n":"2班-31-涂若欣-171"},"1150236294":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=hFTam0NGU95sibvKQCxTiaUg&s=40&t=1557470188","n":"信安二班周炘晨"},"1227071686":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=g0t7rnp0Ox1Ba597WeZtlg&s=40&t=1571029070","n":"2班-24-石康-171030"},"1239887042":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=vEyqYjzuj0JcrK6MhBWaFg&s=40&t=1557402306","n":"2班-12-卢伟康-171"},"1256031976":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=8icfzoXKxMXLUkH9awfwUmQ&s=40&t=1581684936","n":"2班-07-叶家豪-171"},"1277054093":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=rhOsVkJZ22baGzWA75Kumw&s=40&t=1566743434","n":"2班-03-周浩-171030"},"1279129340":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=l4ic1BpYv2E1VLrsFKmVnmg&s=40&t=1583479419","n":"2班-33-张璇-152718"},"1450329018":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=JkxnLkIibAXoWjaQZrBNxoA&s=40&t=1584439021","n":"信2章朝阳"},"1452366672":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=IAEIuucSBKj3jry18bp6aw&s=40&t=1583772453","n":"信安2谭杰17103001"},"1536485943":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=lrgJcib7lbctfz5SIp8hCcQ&s=40&t=1583820156","n":"2班-11-聂仁杰-171"},"1619432296":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=hw5EzNZEPFY2TBTZUFnbmQ&s=40&t=1556980764","n":"2班-27-许梦娇-171"},"1668774679":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=qgqyII4QOtbziaBwsibpVibuQ&s=40&t=1581766205","n":"阙超"},"1714877904":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=lQHB9eoQVbRg86WoEIpWzw&s=40&t=1579847845","n":"2班-21-刘潇-171030"},"1797485264":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=mw4Nl0pbqib6Z8us5LfA9SQ&s=40&t=1583312197","n":"2班-26-肖越-171083"},"1849791380":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=qZpXjd3q9Ix0kjxCm6EwEA&s=40&t=1556746231","n":"2班-35-胡章文-161"},"1970714059":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=CHvUpUQCwfXo5UIMicEVcvw&s=40&t=1559881270","n":"2班-06-郑一凡-171"},"1973563031":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=10ib56Yzic4LN1atOGapXpQA&s=40&t=1583681662","n":"2班-01-田昊-171010"},"2294738830":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=ticyn9YB6YZwQqib4GrATxOw&s=40&t=1584143838","n":"2班-13-贤昌民-171"},"2360467524":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=21SFY9LZUSI4ETOLtNpv7A&s=40&t=1572421649","n":"2班-09-沈杰-171030"},"2967106259":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=vPicI1Uq4aTYIWMHic0ptUNw&s=40&t=1575559498","n":"2班－32－马晓旭"},"3192476880":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=IicyOBE07m11BC4T0nzu9IA&s=40&t=1584589485","n":"2班-29-余婷-171030"},"3315371762":{"f":"http:\/\/thirdqq.qlogo.cn\/g?b=sdk&k=Po0iaE6zjCo14LibsORvJXRw&s=40&t=1584144285","n":"2班-30-杨银淼-171"}}}'
    # json_str = input()
    # str = one(json_str)
    # print("投票人：",str)
    # a,b = get_name(str)
    # if len(a) == 35:
    #     print('所有成员全部投票完毕')
    # else:
    #     print(35 - len(a),"人还未投票，名单如下")
    #     print(b)
    xinan_1()