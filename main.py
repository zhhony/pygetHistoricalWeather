import pandas

pandas.set_option('display.unicode.east_asian_width', True)

pdOutput = pandas.read_html(io='http://www.tianqihoubao.com/lishi/wuxi/month/202211.html',flavor='html5lib',encoding='gbk')


for i in range(2011,2022):
    for j in range(1,13):
        date = str(i)  +  str(j)
        http = 'http://www.tianqihoubao.com/lishi/wuxi/month/%s.html'%date
        pd = pandas.read_html(io=http,flavor='html5lib',encoding='gbk')