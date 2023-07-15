from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import csv
import pandas as pd
from time import time
import DataGeneration
from flask import Flask, render_template, make_response
app = Flask(__name__)
csvfile = "Alldatas.csv"
line = 2
@app.route('/', methods=["GET", "POST"])
def temp_html():
    global line
    line = 2
    return render_template('test_index.html')

@app.route('/index.html')
def index_html():
    global line
    line = 2
    return render_template('index.html')

@app.route('/temperature.html')
def temperature_html():
    global line
    line = 2
    return render_template('temperature.html')

@app.route('/humidity.html')
def humidity_html():
    global line
    line = 2
    return render_template('humidity.html')

@app.route('/ec.html')
def ec_html():
    global line
    line = 2
    return render_template('ec.html')

@app.route('/ph.html')
def ph_html():
    global line
    line = 2
    return render_template('ph.html')

@app.route('/light.html')
def light_html():
    global line
    line = 2
    return render_template('light.html')
@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
    global line
    line += 1
    current_time = (time() + 28800000) * 1000
    data = [current_time] + DataGeneration.ReadLine(csvfile, line)
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response
if __name__ == "__main__":
    app.run(debug=True)
