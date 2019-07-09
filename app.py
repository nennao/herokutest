import os
import random
import pymysql
import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from sqlalchemy.engine.url import make_url

app = Flask(__name__)
CORS(app)
DATA = []

DB_URL = os.environ.get('CLEARDB_DATABASE_URL') or os.environ.get('LOCAL_DATABASE_URL')


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


@app.route('/data/post2', methods=["POST"])
def post_test2():
    price = float(request.args["price"])
    DATA.append(price)
    recommendation = make_recommendation(price)
    return jsonify(f"post request for '{price}' was successful. {DATA}. Recommendation: {recommendation}"), 200


@app.route("/position", methods=["GET"])
def get_position():
    account_id = request.args["accountId"]
    with SQLConnection(DB_URL) as conn:
        cursor, db = conn.cursor, conn.db
        sql = f"SELECT BALANCE FROM ACCOUNTS WHERE ACC_NAME='{account_id}';"
        cursor.execute(sql)
        try:
            balance, = cursor.fetchone()
        except TypeError:
            return jsonify(f"Account not found: {account_id}"), 404

        sql = f"SELECT STOCK, QTY FROM STOCKS WHERE ACC_NAME='{account_id}';"
        cursor.execute(sql)
        stock = {stock: qty for stock, qty in cursor.fetchall()}

    return jsonify({
        "cash": balance,
        "stock": stock,
    })


if __name__ == '__main__':
    app.run()


def make_recommendation(price):
    if price > 3:
        return "this is good, you should sell"
    else:
        return "this is bad, don't sell"


class SQLConnection(object):
    def __init__(self, url):
        self.url = make_url(url)

    def __enter__(self):
        self.db = pymysql.connect(
            db=self.url.database, host=self.url.host, user=self.url.username, password=self.url.password
        )
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, *exc):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()
