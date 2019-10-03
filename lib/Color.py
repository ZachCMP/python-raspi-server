class Color():
  def __init__(self, **kwargs):
    self.color = (0, 0, 0)

  def setColor(self, **kwargs):
    if ('hex' in kwargs):
      self.color = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    else:
      red = kwargs['red'] if 'red' in kwargs else self.color[0]
      green = kwargs['green'] if 'green' in kwargs else self.color[1]
      blue = kwargs['blue'] if 'blue' in kwargs else self.color[2]
      self.color = (red, green, blue)
