from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=12, green=16, blue=21)

rgb = (100, 150, 50)

color = (rgb[0]/255, rgb[1]/255, rgb[2]/255)

while True:
  led.color = color
  print(color)
  sleep(1)