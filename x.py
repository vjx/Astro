import datetime
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const


date = Datetime('1981/05/22', '08:30', '+01:00')

pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

sun = chart.get(const.SUN)
moon = chart.get(const.MOON)

srchart = chart.solarReturn(2017)


print(sun)
print(srchart.date)


