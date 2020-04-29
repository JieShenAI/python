import json
import csv
json_str = 'jsonp_1581752748789_9414295({"errno":0,"errmsg":"SUCCESS","data":{"list":{"20190112":353.7092772,"20190113":312.9795936,"20190114":333.7403148,"20190115":304.6864896,"20190116":311.8322448,"20190117":323.6503716,"20190118":338.8797,"20190119":372.6619488,"20190120":345.076848,"20190121":366.9401088,"20190122":367.8382044,"20190123":389.247606,"20190124":405.4737204,"20190125":436.0823892,"20190126":502.639344,"20190127":495.849114,"20190128":513.5867532,"20190129":490.7215872,"20190130":490.6611612,"20190131":493.986762,"20190201":530.0219448,"20190202":527.0810292,"20190203":488.5993548,"20190204":414.3138012,"20190205":342.6116616,"20190206":545.0786136,"20190207":591.068988,"20190208":606.2593068,"20190209":637.1947296,"20190210":726.2124984,"20190211":687.9075336,"20190212":597.5534592,"20190213":563.8972788,"20190214":505.580616,"20190215":469.952766,"20190216":487.8620604,"20190217":445.0947084,"20190218":415.8890568,"20190219":345.338802,"20190220":395.8886016,"20190221":431.404866,"20190222":412.1937396,"20190223":463.749948,"20190224":478.0189404,"20190225":368.9358516,"20190226":327.3258924,"20190227":364.208724,"20190228":417.344238,"20190301":355.913676,"20200101":266.8720608,"20200102":251.204328,"20200103":397.885122,"20200104":448.8799356,"20200105":420.7530096,"20200106":398.7199404,"20200107":401.682078,"20200108":447.0274008,"20200109":497.460042,"20200110":438.973668,"20200111":481.0020084,"20200112":446.3765172,"20200113":436.1630004,"20200114":412.6136436,"20200115":431.4138732,"20200116":450.4974408,"20200117":479.9456712,"20200118":529.5260304,"20200119":525.4227648,"20200120":542.3144724,"20200121":621.2109996,"20200122":580.6973268,"20200123":551.6447328,"20200124":448.30989,"20200125":261.5466672,"20200126":287.4244176,"20200127":264.7354104,"20200128":225.8917632,"20200129":192.6017028,"20200130":183.7748412,"20200131":153.6096312,"20200201":130.643928,"20200202":142.4592036,"20200203":117.190152,"20200204":85.9585284,"20200205":81.3802464,"20200206":81.188244,"20200207":85.798116,"20200208":94.7500092,"20200209":111.1956336,"20200210":100.9839312,"20200211":74.7511092,"20200212":71.3811852,"20200213":73.1563812,"20200214":73.4141556}}})'
json_str = json_str.replace('jsonp_1581752748789_9414295(','')

json_str = json_str[:-1:]
# print(json_str)
persons = json.loads(json_str)
print(persons)
data = persons['data']
List  = data['list']
str = ''
new_list=[]

headers = ['date','value']
for i in List:
    dict = {'date':i,'value':List[i]}
    new_list.append(dict)
print(new_list)


#

with open('image.csv', 'w', encoding='utf8', newline='') as fp:
    writer = csv.DictWriter(fp,headers)
    writer.writeheader()
    writer.writerows(new_list)


# with open('./person.json','r',encoding = 'utf-8') as fp:
#     persons2 = json.load(fp)
#     print(type(persons2))
#     for person in persons2:
#         print(person)