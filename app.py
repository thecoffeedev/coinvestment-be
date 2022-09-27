import flask
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import requests # for making API calls
import json
import urllib.parse
# from decouple import config  # for environment variables

mysql = MySQL()

# initializing a variable of Flask
app = Flask(__name__)

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
# app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
# app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
# app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
mysql.init_app(app)


@app.route('/', methods=["GET"])
def home():
    return flask.make_response("test")


@app.route('/sign-up', methods=["POST"])
def sign_up():
    data = request.get_json()
    print(data["email address"])
    response = \
    {
        "status":
        {
            "status code": "SUCCESS",
            "status message": "Successfully signed up"
        },
        "name": data["name"],
        "email address": data["email address"]
    }
    return flask.make_response(response)


@app.route('/sign-in', methods=["POST"])
def sign_in():
    data = request.get_json()
    print(data["email address"])
    print(data["password"])
    response = \
    {
        "status":
        {
            "status code": "SUCCESS",
            "status message": "Successfully signed in"
        },
        "name": "Welcome <name>"
    }
    return flask.make_response(response)


@app.route('/view-available-cryptocurrencies', methods=["GET"])
def view_available_cryptocurrencies():
    url = "https://api.coingecko.com/api/v3/search/trending"
    trendingCoins = requests.get(url).json()
    availableCryptocurrencies = []
    for coin in trendingCoins["coins"]:
        x = {
            "cryptocurrency code": coin["item"]["symbol"],
            "cryptocurrency name": coin["item"]["name"],
            "iconPNG": coin["item"]["large"]
        }
        availableCryptocurrencies.append(x)
    print(availableCryptocurrencies)
    response = \
        {
            "status":
            {
                "status code": "SUCCESS",
                "status message": "List of coins with code, name and symbol"
            },
            "available cryptocurrencies": availableCryptocurrencies
        }

    return flask.make_response(response)


@app.route('/view-available-bundles', methods=["GET"])
def view_available_bundles():
    availableBundles = [
                            {
                                "Low risk":
                                {
                                    "Minimum holding period": 6,
                                    "Bundles":
                                    [
                                        {
                                            "cryptocurrency code": "btc",
                                            "cryptocurrency name": "Bitcoin",
                                            "percentage": 50
                                        },
                                        {
                                            "cryptocurrency code": "eth",
                                            "cryptocurrency name": "Ethereum",
                                            "percentage": 50
                                        }
                                    ]
                                },
                                "Medium risk":
                                {
                                    "Minimum holding period": 12,
                                    "Bundles":
                                    [
                                        {
                                            "cryptocurrency code": "btc",
                                            "cryptocurrency name": "Bitcoin",
                                            "percentage": 25
                                        },
                                        {
                                            "cryptocurrency code": "eth",
                                            "cryptocurrency name": "Ethereum",
                                            "percentage": 15
                                        },
                                        {
                                            "cryptocurrency code": "xrp",
                                            "cryptocurrency name": "Ripple",
                                            "percentage": 15
                                        },
                                        {
                                            "cryptocurrency code": "ltc",
                                            "cryptocurrency name": "Litecoin",
                                            "percentage": 25
                                        },
                                        {
                                            "cryptocurrency code": "xmr",
                                            "cryptocurrency name": "Monero",
                                            "percentage": 20
                                        }
                                    ]
                                },
                                "High risk":
                                {
                                    "Minimum holding period": 12,
                                    "Bundles":
                                    [
                                        {
                                            "cryptocurrency code": "doge",
                                            "cryptocurrency name": "Dogecoin",
                                            "percentage": 20
                                        },
                                        {
                                            "cryptocurrency code": "shib",
                                            "cryptocurrency name": "Shiba Inu",
                                            "percentage": 20
                                        },
                                        {
                                            "cryptocurrency code": "etc",
                                            "cryptocurrency name": "Ethereum Classic",
                                            "percentage": 30
                                        },
                                        {
                                            "cryptocurrency code": "ape",
                                            "cryptocurrency name": "ApeCoin",
                                            "percentage": 30
                                        }
                                    ]
                                }
                            }
                        ]

    response = {
                    "status":
                    {
                        "status code": "SUCCESS",
                        "status message": "List of bundles with code, name and percentage"
                    },
                    "available bundles": availableBundles
        }

    return flask.make_response(response)


@app.route('/account', methods=["GET"])
def account():
    response = {
                    "status":
                    {
                        "status code": "SUCCESS",
                        "status message": "View customer account and purchased wallets and bundles"
                    }
                }

    return flask.make_response(response)


@app.route('/bundle/<bundleAddress>', methods=["GET"])
def view_bundle(bundleAddress):
    data = request.get_json()
    print(data)
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View details for bundle " + bundleAddress
            }
    }
    # return the data for that bundle address
    return flask.make_response(response)


@app.route('/wallet/<walletAddress>', methods=["GET"])
def view_bundle(walletAddress):
    data = request.get_json()
    print(data)
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View details for wallet " + walletAddress
            }
    }
    # return the data for that wallet address
    return flask.make_response(response)


"""
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    date_time = ""
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['pass']

            # API for date and time ---------------------------------------------------------------------------
            url = "http://worldtimeapi.org/api/timezone/Europe/London"
            response = requests.get(url).json()
            print("" + str(response))  # response details
            # retrieve response details form the attribute, datetime
            date_time = response["datetime"]
            # -------------------------------------------------------------------------------------------------

            con = mysql.connect()
            cur = con.cursor()

            cur.execute('INSERT INTO user (username, email, password)VALUES( %s,  %s, %s)',
                        (username, email, password))

            con.commit()
            msg = "You have signed up today (UK Time)"

        except:
            con.rollback()
            msg = "The sign up operation failed."

        finally:
            # return render_template("result.html", msg=msg, date_time=date_time)
            return render_template("result.html", msg=msg, date_time=date_time)
            con.close()


@app.route('/viewrec', methods=['POST', 'GET'])
def viewrec():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['pass']
            con = mysql.connect()
            cur = con.cursor()
            cur.execute('SELECT username, email FROM User WHERE username=%s AND password=%s',
                        (username, password))
            rows = cur.fetchall()
            con.commit()

        except:
            con.rollback()

        finally:
            return render_template("view.html", rows=rows)
            con.close()


@app.route('/updaterec', methods=['POST', 'GET'])
def updaterec():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['pass']
            email = request.form['email']

            con = mysql.connect()
            cur = con.cursor()
            cur.execute('UPDATE User SET email=%s WHERE username=%s AND password=%s',
                        (email, username, password))
            con.commit()

            cur.execute(
                'SELECT username, email FROM User WHERE username=%s', username)
            rows = cur.fetchall()
            con.commit()

        except:
            con.rollback()

        finally:
            return render_template("view.html", rows=rows)
            con.close()


@app.route('/removerec', methods=['POST', 'GET'])
def removerec():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['pass']
            con = mysql.connect()
            cur = con.cursor()
            cur.execute('DELETE FROM User WHERE username=%s AND password=%s',
                        (username, password))
            con.commit()

            cur.execute(
                'SELECT username, email FROM User WHERE username=%s', username)
            rows = cur.fetchall()
            con.commit()

        except:
            con.rollback()

        finally:
            return render_template("view.html", rows=rows)
            con.close()
"""

if __name__ == "__main__":
    app.run()
