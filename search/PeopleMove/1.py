import re
import urllib.request
import xlwt
import xlrd

date = "20171016"
cityList = xlrd.open_workbook("E:/city.xls").sheet_by_index(0).col_values(0) # ['city', '南昌', '景德镇', '萍乡', ...
cityCodeList = xlrd.open_workbook("E:/city.xls").sheet_by_index(0).col_values(1) # ['cityCode', '360100', '360200',...
direction = ["0","1"]
header = ["from","to","number","car","train","plane"]
dInd = 0
for cityIndex in range(1,len(cityCodeList)):
    for dInd in range(2):
        url = "https://lbs.gtimg.com/maplbs/qianxi/" + date + "/" + cityCodeList[cityIndex] + direction[dInd] + "6.js" # "0 迁入": result-city,"1 迁出:city-result
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("result")
        for i in range(len(header)):
            sheet.write(0,i,header[i])
        ptRow = re.compile('(\[".*?\])')
        ptCity = re.compile("")
        try:
            data = urllib.request.urlopen(url).read().decode("utf8") # JSONP_LOADER&&JSONP_LOADER([["重庆",198867,0.000,0.300,0.700],["上海",174152,0.160,0.390,0.450],[...
            dataList = re.findall(ptRow,data) # ['["重庆",198867,0.000,0.300,0.700]', '["上海",174152,0.160,0.390,0.450]',[...
            for i in range(len(dataList)):
                colList = str(dataList[i]).split(",") # colList[4] = 0.700]
                if direction[dInd] == "0":
                    sheet.write(i + 1, len(header) - 6, str(colList[0]).replace("[","").replace('"',"")) # city
                    sheet.write(i + 1, len(header) - 5, cityList[cityIndex])
                else:
                    sheet.write(i + 1, len(header) - 6, cityList[cityIndex])
                    sheet.write(i + 1, len(header) - 5, str(colList[0]).replace("[","").replace('"',"")) # city
                sheet.write(i + 1, len(header) - 4, colList[1]) # number
                sheet.write(i + 1, len(header) - 3, colList[2]) # car
                sheet.write(i + 1, len(header) - 2, colList[3]) # train
                sheet.write(i + 1, len(header) - 1, str(colList[4]).replace("]","")) # plane
        except Exception as e:
            print(e)
        workbook.save("E:/qianxi/" + str(cityList[cityIndex]) + direction[dInd] + date + ".xls")
print("Done!")