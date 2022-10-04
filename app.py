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
        responseData = CController.getCustomerDetails(reqData)
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


@app.route('/account/wallets', methods=["POST"])
def account_wallets():
    print("account_wallets entry")
    jsonReqData = request.get_json()
    print("jsonReqData : ", jsonReqData)
    response = WController.getAllWalletsFromCustomerID(jsonReqData)
    print("account_wallets exit")
    return flask.make_response(response)


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


@app.route('/account/wallets/walletAddress', methods=["POST"])
def account_walletdetails():
    print("account_walletdetails entry")
    jsonReqData = request.get_json()
    print("jsonReqData : ", jsonReqData)
    response = WController.getAllWalletDetailsFromWalletAddress(jsonReqData)
    print("account_walletdetails entry")
    return flask.make_response(response)


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

@app.route('/account/purchase/wallet', methods=["GET"])
def account_purchasewallet():
    print("account_purchasewallet entry")
    jsonReqData = request.get_json()
    print("jsonReqData : ", jsonReqData)
    response = WController.purchaseWallet(jsonReqData)
    print("account_purchasewallet entry")
    return flask.make_response(response)

@app.route('/account/sell/wallet', methods=["POST"])
def account_sellwallet():
    print("account_sellwallet entry")
    jsonReqData = request.get_json()
    print("jsonReqData : ", jsonReqData)
    response = WController.sellWallet(jsonReqData)
    print("account_sellwallet exit")
    return flask.make_response(response)


if __name__ == "__main__":
    app.run()
