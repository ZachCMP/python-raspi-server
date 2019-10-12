import requests
import random
import signal
import sys
from time import sleep

def signal_handler(sig, frame):
  print('Closing process')
  requests.post(url=URL, data={ 'red': 0, 'green': 0, 'blue': 0 })
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

URL = 'http://10.0.0.195:5000/color'

color = {
  'red': 0,
  'green': 0,
  'blue': 0,
}

points = (
  (0, 0),
  (0.0, 0.0),
  (0.58, 1.0),
  (1, 1),
)

def interpFn(t):
  p1 = [ ((1 - t)**3) * v for v in points[0] ]
  p2 = [ (3*((1 - t)**2)*t) * v for v in points[1] ]
  p3 = [ (3*(1 - t)*(t**2)) * v for v in points[2] ]
  p4 = [ (t**3) * v for v in points[3] ]
  res = [ 0, 0 ]
  for p in [ p1, p2, p3, p4 ]:
    res = [ res[0] + p[0], res[1] + p[1] ]
  # print(t, res)
  return res[1]

step = int(input('Set step (int): '))
rate = float(input('Set rate (float): '))

def loop(val):
  # color['red'] = int(val)
  color['green'] = int(val)
  color['blue'] = int(val)
  print(color)
  requests.post(url=URL, data=color)

while True:
  for i in range(step):
    val = interpFn(i / step) * 255
    loop(val)
    sleep(rate)

  for i in range(step):
    val = interpFn((step-(i+1)) / step) * 255
    loop(val)
    sleep(rate)


