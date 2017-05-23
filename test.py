import datetime
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const
from flatlib.dignities import essential
import time
import os
import socket

host = '127.0.0.1'
port = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:

  data = datetime.datetime.utcnow()
  d = data.strftime('%Y/%m/%d')
  h = data.strftime('%H:%M:%S')
  date = Datetime(d,h)

  pos = GeoPos('38n32', '8w54')
  chart = Chart(date, pos)

  sun = chart.get(const.SUN)
  moon = chart.get(const.MOON)
  mercury = chart.get(const.MERCURY)
  venus = chart.get(const.VENUS)
  mars = chart.get(const.MARS)
  jupiter = chart.get(const.JUPITER)
  saturn = chart.get(const.SATURN)  

  sol = 'sol '
  sol += str(sun.sign)
  sol += ' '
  sol += str(sun.signlon)
  sol += ' '
  sol += str(sun.lon)
  sol += ';'
  s.send(sol.encode())

  lua = 'lua '
  lua += str(moon.sign)
  lua += ' '
  lua += str(moon.signlon)
  lua += ' '
  lua += str(moon.lon)
  lua += ' '
  lua += str((essential.EssentialInfo(moon)).score)
  lua += ';'
  s.send(lua.encode())

  mercurio = 'mercurio '
  mercurio += str(mercury.sign)
  mercurio += ' '
  mercurio += str(mercury.signlon)
  mercurio += ' '
  mercurio += str(mercury.lon)
  mercurio += ';'
  s.send(mercurio.encode())

  veenus = 'veenus '
  veenus += str(venus.sign)
  veenus += ' '
  veenus += str(venus.signlon)
  veenus += ' '
  veenus += str(venus.lon)
  veenus += ';'
  s.send(veenus.encode())

  marte = 'marte '
  marte += str(mars.sign)
  marte += ' '
  marte += str(mars.signlon)
  marte += ' '
  marte += str(mars.lon)
  marte += ';'
  s.send(marte.encode())

  juupiter = 'juupiter '
  juupiter += str(jupiter.sign)
  juupiter += ' '
  juupiter += str(jupiter.signlon)
  juupiter += ' '
  juupiter += str(jupiter.lon)
  juupiter += ';'
  s.send(juupiter.encode())

  saturno = 'saturno '
  saturno += str(saturn.sign)
  saturno += ' '
  saturno += str(saturn.signlon)
  saturno += ' '
  saturno += str(saturn.lon)
  saturno += ';'
  s.send(saturno.encode())



  

  time.sleep(0.1)

s.shutdown(0)
s.close()
