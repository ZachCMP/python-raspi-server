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

# step = int(input('Set step (int): '))
# rate = float(input('Set rate (float): '))
# dark = float(input('Set dark time (float): '))

# while True:
#   for c in ['red', 'green', 'blue']:
#     for i in range(step):
#       color[c] = int((i+1)/step * 255)
#       print(color)
#       requests.post(url=URL, data=color)
#       sleep(rate)

#   for c in ['red', 'green', 'blue']:
#     for i in range(step):
#       color[c] = int((step-(i+1))/step * 255)
#       print(color)
#       requests.post(url=URL, data=color)
#       sleep(rate)

#   sleep(dark)

rate = float(input('Set rate (float): '))
rng = int(input('Set random range (int): '))

while True:
  for c in ['red', 'green', 'blue']:
    change = random.randint(-rng, rng)
    val = color[c] + change
    if (val < 0):
      val = 0
    if (val > 255):
      val = 255
    color[c] = val

  print(color)
  requests.post(url=URL, data=color)

  sleep(rate)


