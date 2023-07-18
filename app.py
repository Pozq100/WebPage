from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import main_replacement as mainfile
import csv
from time import time
import DataGeneration
from flask import Flask, render_template, make_response
app = Flask(__name__)
csvfile = "Alldatas.csv"
line = 3
state = -1
@app.route('/', methods=["GET", "POST"])
def temp_html():
    global line
    line = 3
    return render_template('test_index.html')

@app.route('/index.html')
def index_html():
    global line
    line = 3
    return render_template('index.html')

@app.route('/temperature.html')
def temperature_html():
    global line
    line = 3
    return render_template('temperature.html')

@app.route('/humidity.html')
def humidity_html():
    global line
    line = 3
    return render_template('humidity.html')

@app.route('/ec.html')
def ec_html():
    global line
    line = 3
    return render_template('ec.html')

@app.route('/ph.html')
def ph_html():
    global line
    line = 3
    return render_template('ph.html')

@app.route('/light.html')
def light_html():
    global line
    line = 3
    return render_template('light.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
    global line
    ListofDatas = DataGeneration.ReadLine(csvfile,line)
    if ListofDatas:
        line += 1
        data = ListofDatas
        response = make_response(json.dumps(data))
    else:
        response = make_response(json.dumps([]))
    response.content_type = 'application/json'
    return response

def get_latest_data():
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) > 1:
            latest_row = data[-1]
            return latest_row
        else:
            return None

@app.route('/data_current', methods=["GET"])
def data_current():
    latest_data = get_latest_data()
    if latest_data:
        data = latest_data
        response = make_response(json.dumps(data))
    else:
        response = make_response(json.dumps([]))
    response.content_type = 'application/json'
    return response

@app.route('/switch-state', methods=["GET", "POST"])
def switch_state():
    global state
    state *= -1
    while state == 1:
        print("hello")
    response_switch = make_response(json.dumps(state))
    return response_switch

if __name__ == "__main__":
    app.run(debug=True)
