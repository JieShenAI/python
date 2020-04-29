import json
#将Python对象转换为json字符串

persons = [
    {
        'username':'zhiliao',
        'age':18,
        'country':'China'
    },
    {
        'username':'zhidao',
        'age':20,
        'country':'中国'
    }
]

# json_str = json.dumps(persons)
# print(type(json_str))
# print(json_str)
with open ('./person.json','w',encoding = 'utf-8') as fp:
    #fp.write(json_str)
    json.dump(persons,fp,ensure_ascii = False)#dump 和 dumps 区别



