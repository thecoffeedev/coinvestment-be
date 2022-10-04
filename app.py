import flask
from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_session import Session
import requests  # for making API calls
import json
import urllib.parse
# from decouple import config  # for environment variables
from controllers.WalletController import WalletController
from controllers.CustomerController import CustomerController
from controllers.BundleController import BundleController

# initializing a variable of Flask
app = Flask(__name__)

# Cors configs
cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"

# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "firestore"
# sess = Session(app)
# sess.init_app(app)

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
# app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
# app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
# app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
# mysql.init_app(app)

WController = WalletController(app)
CController = CustomerController(app)
BController = BundleController(app)

sessionTokens = {}

def validateToken(req):
    if req.headers.get("Authorization") in sessionTokens.keys():
        # req["customerID"] = sessionTokens[req.headers.get("Authorization")]
        # customerID = sessionTokens[req.headers.get("Authorization")]
        return True
    else:
        return False


@app.route('/', methods=["GET"])
def home():
    return flask.make_response({
            "status": {
                "statusCode": "SUCCESS",
                "statusMessage": "Successfully reached the test route"
            }
        })


@app.route('/sign-up', methods=["POST"])
def sign_up():
    req = request.get_json()
    responseData = CController.signUp(req)

    if responseData.get("status")["statusCode"] == "SUCCESS":
        token = CController.generateToken()
        if "customerID" in responseData:
            sessionTokens[token] = responseData["customerID"]
            responseData["token"] = token
            del responseData["customerID"]

    resp = flask.make_response(responseData)
    return resp


@app.route('/sign-in', methods=["POST"])
def sign_in():
    reqData = request.get_json()
    responseData = CController.signIn(reqData)

    if responseData.get("status")["statusCode"] == "SUCCESS":
        token = CController.generateToken()
        if "customerID" in responseData:
            sessionTokens[token] = responseData["customerID"]
            responseData["token"] = token
            del responseData["customerID"]
    resp = flask.make_response(responseData)
    return resp


@app.route('/sign-out', methods=["POST"])
def sign_out():
    if validateToken(request):
        del sessionTokens[request.headers.get("Authorization")]
        res = \
            {
                "status": {
                    "statusCode": "SUCCESS",
                    "statusMessage": "Successfully signed out"
                }
            }
        return flask.make_response(res)

    else:
        return flask.make_response({
                "status": {
                    "statusCode": "FAILURE",
                    "statusMessage": "No valid token"
                }
            })


@app.route('/profile/customer-details', methods=["POST"])
def customer_details():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = CController.#the method to view all customer details(reqData)
        return flask.make_response(responseData)

    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })




@app.route('/list/all/cryptocurrencies', methods=["GET"])
def list_all_cryptocurrencies():
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


"""
Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "availableCryptocurrencies": [
        {
            "cryptocurrencyCode": "btc",
            "cryptocurrencyName": "name"
        }
    ],
    "availableBundles": [
        {
            "bundleName": "Low Risk",
            "bundleCryptocurrencies": [
                {
                    "cryptocurrencyCode": "code",
                    "cryptocurrencyName": "name",
                    "percentage": 30
                }
            ],
            "minimumHoldingPeriod": 5
        }
    ]
}
"""


@app.route('/list/all/bundles', methods=["GET"])
def list_all_bundles():
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


"""
Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "availableCryptocurrencies": [
        {
            "cryptocurrencyCode": "btc",
            "cryptocurrencyName": "name"
        }
    ],
    "availableBundles": [
        {
            "bundleName": "lowRisk",
            "bundleCryptocurrencies": [
                {
                    "cryptocurrencyCode": "code",
                    "cryptocurrencyName": "name",
                    "percentage": 30
                }
            ],
            "minimumHoldingPeriod": 5
        }
    ]
}
"""


@app.route('/list/all', methods=["GET"])
def list_all():
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View customer account and purchased wallets and bundles"
            }
    }
    return flask.make_response(response)


"""
Route: /account/customerdetails
Request JSON:
{
    "customerID": "customerID"
}

Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "customerID": "customerID",
    "registerDatetime": "registerDatetime",
    "emailAddress": "emailAddress",
    "previousSignInDatetime": "previousSignInDatetime",
    "currentSignInDatetime": "currentSignInDatetime",
    "name": "name"
}
"""


@app.route('/account/customerdetails', methods=["GET"])
def account_customerdetails(customerID):
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View customer account and purchased wallets and bundles"
            }
    }

    return flask.make_response(response)


"""
Route: /account/wallets
Request JSON:
{
    "customerID": "customerID"
}

Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "wallets": [
        {
            "walletAddress": "walletAddress",
            "customerID": "customerID",
            "initialBalance": "initialBalance",
            "currentBalance": "currentBalance",
            "cryptocurrencyCode": "cryptocurrencyCode",
            "holdingPeriod": "holdingPeriod"
        }
    ]
}
"""


@app.route('/account/wallets', methods=["GET"])
def account_wallets(customerID):
    data = request.get_json()
    print(data)
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View wallets for customer " + customerID
            }
    }
    # return the data for that bundle address
    return flask.make_response(response)


"""
Route: /account/bundles
Request JSON:
{
    "customerID": "customerID"
}

Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "bundles": [
        {
            "bundleAddress": "bundleAddress",
            "bundleID": "bundleID",
            "customerID": "customerID",
            "amount": "amount",
            "holdingPeriod": "holdingPeriod",
            "purchaseDatetime": "purchaseDatetime",
            "status": "status"
        }
    ]
}
"""


@app.route('/account/bundles', methods=["GET"])
def account_bundles():
    data = request.get_json()
    print(data)
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View bundles for: "
            }
    }
    # return the data for that wallet address
    return flask.make_response(response)


"""
Route: /account/wallets/<wallet_adddress>
Request JSON:
{
    "customerID": "customerID",
    "walletAddress": "walletAddress"
}

Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "wallets": {
        "walletAddress": "walletAddress",
        "customerID": "customerID",
        "initialBalance": "initialBalance",
        "currentBalance": "currentBalance",
        "cryptocurrencyCode": "cryptocurrencyCode",
        "holdingPeriod": "holdingPeriod"
    },
    "walletTransactions": [
        {
            "transactionID": "transactionID",
            "transactionDateTime": "transactionDateTime",
            "chargeApplied": "chargeApplied",
            "amount": "amount",
            "action": "action",
            "cardNumber": "cardNumber",
            "expiry": "expiry",
            "unitsSold": "unitsSold",
            "initialRate": "initialRate"
        }
    ]
}
"""


@app.route('/account/wallets/<walletAddress>', methods=["GET"])
def account_walletdetails(walletAddress):
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
Route: /account/bundles/<bundle_address>
Request JSON:
{
    "customerID": "customerID",
    "bundleAddress": "bundleAddress"
}

Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "bundles": {
        "bundleAddress": "bundleAddress",
        "bundleID": "bundleID",
        "customerID": "customerID",
        "amount": "amount",
        "holdingPeriod": "holdingPeriod",
        "purchaseDatetime": "purchaseDatetime",
        "status": "status"
    },
    "bundleTransactions": [ 
        {
            "transactionID": "transactionID",
            "transactionDateTime": "transactionDateTime",
            "chargeApplied": "chargeApplied",
            "amount": "amount",
            "action": "action",
            "cardNumber": "cardNumber",
            "expiry": "expiry",
            "initialRate": "initialRate"
        }
    ]
}
"""


@app.route('/account/bundles/<bundle_address>', methods=["GET"])
def account_bundledetails(bundleAddress):
    data = request.get_json()
    print(data)
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View details for wallet " + bundleAddress
            }
    }
    # return the data for that wallet address
    return flask.make_response(response)


"""
Route: /account/bundles/<bundle_address>
Request JSON:
{
    "customerID": "customerID"
}

Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "customer": {
        "customerID": "customerID",
        "registerDatetime": "registerDatetime",
        "emailAddress": "emailAddress",
        "previousSignInDatetime": "previousSignInDatetime",
        "currentSignInDatetime": "currentSignInDatetime",
        "name": "name"
    },
    "wallets": {
        "walletAddress": "walletAddress",
        "customerID": "customerID",
        "initialBalance": "initialBalance",
        "currentBalance": "currentBalance",
        "cryptocurrencyCode": "cryptocurrencyCode",
        "holdingPeriod": "holdingPeriod",
        "walletTransactions": [
            {
                "transactionID": "transactionID",
                "transactionDateTime": "transactionDateTime",
                "chargeApplied": "chargeApplied",
                "amount": "amount",
                "action": "action",
                "cardNumber": "cardNumber",
                "expiry": "expiry",
                "unitsSold": "unitsSold",
                "initialRate": "initialRate"
            }
        ]
    },
    "bundles": {
        "bundleAddress": "bundleAddress",
        "bundleID": "bundleID",
        "customerID": "customerID",
        "amount": "amount",
        "holdingPeriod": "holdingPeriod",
        "purchaseDatetime": "purchaseDatetime",
        "status": "status",
        "bundleTransactions": [ 
            {
                "transactionID": "transactionID",
                "transactionDateTime": "transactionDateTime",
                "chargeApplied": "chargeApplied",
                "amount": "amount",
                "action": "action",
                "cardNumber": "cardNumber",
                "expiry": "expiry",
                "initialRate": "initialRate"
            }
        ]
    }
}
"""


@app.route('/account', methods=["GET"])
def account():
    data = request.get_json()
    print(data)
    response = {
        "status":
            {
                "status code": "SUCCESS",
                "status message": "View details for user "
            }
    }
    # return the data for that wallet address
    return flask.make_response(response)


"""
Route: /account/purchase/wallet
Request JSON:
{
    "wallet": {
        "customerID": "customerID",
        "initialBalance": "initialBalance",
        "cryptocurrencyCode": "cryptocurrencyCode",
        "holdingPeriod": "holdingPeriod"
    },
    "walletTransaction": [
        {
            "initialRate": "initialRate",
            "amount": "amount",
            "cardNumber": "cardNumber",
            "expiry": "expiry"
        }
    ]
}
Response JSON:
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "wallet": {
        "walletAddress": "walletAddress",
        "customerID": "customerID",
        "initialBalance": "initialBalance",
        "currentBalance": "currentBalance",
        "cryptocurrencyCode": "cryptocurrencyCode",
        "holdingPeriod": "holdingPeriod"
    },
    "walletTransaction": [
        {
            "transactionID": "transactionID",
            "transactionDateTime": "transactionDateTime",
            "chargeApplied": "chargeApplied",
            "amount": "amount",
            "action": "action",
            "cardNumber": "cardNumber",
            "expiry": "expiry",
            "unitsSold": "unitsSold",
            "initialRate": "initialRate"
        }
    ]
}
"""


@app.route('/account/purchase/wallet', methods=["GET"])
def account_purchasewallet():
    print("account_purchasewallet entry")
    jsonReqData = request.get_json()
    print("jsonReqData : ", jsonReqData)
    response = cWallet.purchaseWallet(jsonReqData)
    print("account_purchasewallet entry")
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
