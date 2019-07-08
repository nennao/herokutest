import random
import requests
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/data/coin')
def get_coin_data():
    params = {'start': '2017-12-31',
              'end': '2018-01-15',
              }
    req = requests.get(url="https://api.coindesk.com/v1/bpi/historical/close.json", params=params)
    data = req.json()

    return data['bpi']


@app.route('/data/random', methods=["GET"])
def get_rand_data():
    return jsonify({'random': round(2+random.random()*3, 3)})


@app.route('/data/post', methods=["POST"])
def post_test():
    name = request.args["name"]
    test_str = f'congratulations, {name} on your successful request'
    return jsonify(f"post request for '{name}' was successful. {test_str}"), 200


if __name__ == '__main__':
    app.run()
