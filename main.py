import pandas

pandas.set_option('display.unicode.east_asian_width', True)

pdOutput = []
pdErrorList = []


for i in range(2011, 2022):
    for j in range(1, 13):
            date = str(i) + str(j)
            http = 'http://www.tianqihoubao.com/lishi/wuxi/month/%s.html' % date
            try:
                pdOutput.append(pandas.read_html(
                    io=http, flavor='html5lib', encoding='gbk'))
            except:
                pdErrorList.append(date)
                continue
