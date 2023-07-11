from flask import Flask,render_template,url_for,request,redirect, make_response
import random as rng
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]

    Temperature = round(rng.uniform(20, 40), 1)
    Humidity = round(rng.uniform(0, 100), 1)
    """EC_level = round(rng.uniform(0, 1), 0)
    pH_level = round(rng.uniform(0, 14), 0)
    light_level = round(rng.uniform(0, 1023), 0)"""
    current_time = time() + 28800000

    data = [current_time * 1000, Temperature, Humidity] #, EC_level, pH_level, light_level

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
