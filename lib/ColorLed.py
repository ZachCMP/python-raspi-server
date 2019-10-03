import os
from gpiozero import RGBLED
from lib.Color import Color 

class ColorLed(Color):
  def __init__(self, *args, **kwargs):
    super(self.__class__, self).__init__(*args, **kwargs)
    red_pin = int(os.getenv('RED_PIN'))
    green_pin = int(os.getenv('GREEN_PIN'))
    blue_pin = int(os.getenv('BLUE_PIN'))
    self.led = RGBLED(red=red_pin, green=green_pin, blue=blue_pin)
    self.setLedColor()
    
  def setColor(self, **kwargs):
    super().setColor(**kwargs)
    self.setLedColor()

  def setLedColor(self):
    self.led.color = (self.color[0]/255, self.color[1]/255, self.color[2]/255)