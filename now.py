import datetime
import time
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const



data = datetime.datetime.utcnow()
d = data.strftime('%Y/%m/%d')
h = data.strftime('%H:%M:%S')
date = Datetime(d,h)
pos = GeoPos('38n43', '9w8')
chart = Chart(date, pos)

sun  = chart.get(const.SUN)
moon = chart.get(const.MOON)
asc  = chart.get(const.ASC)
house1 = chart.get(const.HOUSE1)

srchart = chart.solarReturn(2017)

print(srchart.date)
print(sun)
print(moon)
print(asc)
# print(house1)

