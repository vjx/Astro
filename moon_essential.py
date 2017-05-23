"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    essential dignities.
"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.dignities import essential
import time
import os
import socket
import datetime


data = datetime.datetime.utcnow()
d = data.strftime('%Y/%m/%d')
h = data.strftime('%H:%M:%S')
date = Datetime(d,h)

pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

moon = chart.get(const.MOON)

info = essential.EssentialInfo(moon)

print(moon)  
print(info.score)




