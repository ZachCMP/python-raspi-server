import os
from flask import Flask, escape, request, render_template, jsonify
from gpiozero import RGBLED

from lib.Color import Color
from lib.ColorLed import ColorLed

app = Flask(__name__)

color = ColorLed() if os.getenv('IS_RASPI') else Color()

@app.route('/')
def index():
  global color
  c = color.color
  return render_template('index.html', red=c[0], green=c[1], blue=c[2])

@app.route('/color', methods=['POST'])
def change_color():
  global color
  red = int(request.form['red']) if 'red' in request.form else color[0]
  green = int(request.form['green']) if 'green' in request.form else color[1]
  blue = int(request.form['blue']) if 'blue' in request.form else color[2]
  color.setColor(red=red, green=green, blue=blue)
  resp = jsonify(success=True)
  return resp