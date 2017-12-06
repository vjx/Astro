import datetime
import time
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const
from flatlib import aspects

# Build a chart for a date and location
data = datetime.datetime.utcnow()
d = data.strftime('%Y/%m/%d')
h = data.strftime('%H:%M:%S')
date = Datetime(d,h)
pos = GeoPos('38n43', '9w8')
chart = Chart(date, pos)

# Retrieve the Sun and Moon 
sun = chart.get(const.SUN)
moon = chart.get(const.MOON)
venus = chart.get(const.VENUS)

# Get the aspect
aspect1 = aspects.getAspect(sun, moon, const.MAJOR_ASPECTS)
aspect2 = aspects.getAspect(sun, venus, const.ALL_ASPECTS)
print(aspect1) 
print(aspect2xsc) 