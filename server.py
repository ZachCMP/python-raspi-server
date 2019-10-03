from flask import Flask, escape, request, render_template, jsonify
from gpiozero import RGBLED

app = Flask(__name__)

color = (0, 0, 0)

@app.route('/')
def index():
  global color
  return render_template('index.html', red=color[0], green=color[1], blue=color[2])

@app.route('/color', methods=['POST'])
def change_color():
  global color
  red = int(request.form['red']) if 'red' in request.form else color[0]
  green = int(request.form['green']) if 'green' in request.form else color[1]
  blue = int(request.form['blue']) if 'blue' in request.form else color[2]
  color = (red, green, blue)
  resp = jsonify(success=True)
  return resp