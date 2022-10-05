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
    responseData = WController.getAllAvailableCryptocurrencies()
    return flask.make_response(responseData)


@app.route('/list/all/bundles', methods=["GET"])
def list_all_bundles():
    # List all bundles with their names and ID
    responseData = BController.getAllAvailableBundles()
    return flask.make_response(responseData)


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


@app.route('/account/bundles/bundle_address', methods=["GET"])
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
