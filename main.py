import pandas
import os

path = os.environ['USERPROFILE'] + '\\desktop\\'

pandas.set_option('display.unicode.east_asian_width', True)

pdOutput = []
pdErrorList = []


for i in range(2011, 2023):
    for j in range(1, 13):
        date = str(i) + '%02d'%j
        http = 'http://www.tianqihoubao.com/lishi/wuxi/month/%s.html' % date
        try:
            pdList = pandas.read_html(
                io=http, flavor='html5lib', encoding='gbk')
            for pd in pdList:
                pdOutput.append(pd)
        except:
            pdErrorList.append(date)
            continue
pandas.concat(pdOutput).to_excel(path + '123.xlsx')
