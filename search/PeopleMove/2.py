import requests
import pandas as pd

lst_date = ['20190130', '20190131', '20190201']
df_city = pd.read_excel('/home/kesci/中国城市代码对照表(4).xlsx')
city_lst = df_city['城市编码'].iloc[:300].tolist()
u = 'http://lbs.gtimg.com/maplbs/qianxi/20190502/44030016.js?callback=JSONP_LOADER&_=1558010723465'
# 通过网页生成某一天的不同数据
urllst = []  # 创建一个空的列表
for i in lst_date:  # i代表的是我们需要获取的日期，这里是指春节前三天的日期
    for j in city_lst:  # j代表的是城市编号
        urllst.append('http://lbs.gtimg.com/maplbs/qianxi/%s/%s16.js?' % (i, str(j)))
r = requests.get(urllst[0])
# 需要吧上面的信息处理成文本，就是需要吧（）前后的东西去掉
startn = r.text.index('(') + 1  # 用index方法来确认（是在第几个位置
# 获取尾括号的位置
endn = r.text.index(')')
datai = r.text[startn:endn]
datai = eval(datai)  # eval会运行这个datai,如果datai是一个列表形式，那么就可以直接定义datai


# 创建函数获取数据
def get_data(ui):
    ri = requests.get(url=ui)
    # 访问页面
    try:
        startn = ri.text.index("(") + 1
        endn = ri.text.index(")")
        datai = eval(ri.text[startn:endn])
        # 识别为list数据
        datalsti = []
        for i in datai:
            dic = {}
            dic['起点城市_城市编码'] = ui.split('/')[-1].split('.')[0]
            dic['终点城市'] = i[0]
            dic['日期'] = ui.split('/')[-2]
            dic['迁出量'] = i[1]
            dic['汽车占比'] = i[2]
            dic['飞机占比'] = i[2]
            dic['火车占比'] = i[3]
            datalsti.append(dic)
            # 获取迁出数据
        return datalsti
        # 创建函数采集数据
    except:
        print('数据识别失败')
        return []


print('函数构建完成')
# 批量采集数据
data_lst = []
n = 1
for u in urllst[:10]:
    data_lst.extend(get_data(u))
    print('成功实现第%i循环' % (n))
    n += 1
df = pd.DataFrame(data_lst)

df['起点城市_城市编码'] = df['起点城市_城市编码'].str[:6].astype(np.int)
df.columns = ['日期', '汽车占比', '火车占比', '终点城市', '起点城市_城市编码', '迁出量', '飞机占比']
# 数据整理与核心城市筛选 起点城市、终点城市经纬度匹配
df = pd.merge(df, df_city,
              left_on='起点城市_城市编码', right_on='城市编码',
              how='left')
df = df[['日期', '汽车占比', '火车占比', '飞机占比', '城市名称', '终点城市',
         '经度', '纬度', '迁出量']]
df.rename(columns={'城市名称': '起点城市', '经度': '起点城市_经度', '纬度': '起点城市_纬度'},
          inplace=True)
# 添加起点城市经纬度
df = pd.merge(df, df_city,
              left_on='终点城市', right_on='城市名称',
              how='left')
df = df[['日期', '汽车占比', '火车占比', '飞机占比', '起点城市', '终点城市',
         '起点城市_经度', '起点城市_纬度', '经度', '纬度', '迁出量']]
df.rename(columns={'经度': '终点城市_经度', '纬度': '终点城市_纬度'},
          inplace=True)
# 添加终点城市经纬度

df.head()