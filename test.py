import datetime
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const

data = datetime.datetime.utcnow()
d = data.strftime('%Y/%m/%d')
h = data.strftime('%H:%M')
date = Datetime(d,h,1)

pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

sun = chart.get(const.SUN)
moon = chart.get(const.MOON)
mercury = chart.get(const.MERCURY)
venus = chart.get(const.VENUS)
mars = chart.get(const.MARS)
jupiter = chart.get(const.JUPITER)
saturn = chart.get(const.SATURN)


print (date)
print(sun)
print (moon)
print (mercury)
print (venus)
print (mars)
print (jupiter)
print (saturn)
