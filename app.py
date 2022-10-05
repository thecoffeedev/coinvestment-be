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


@app.route('/profile/customer-details', methods=["GET"])
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


@app.route('/profile/change-password', methods=["POST"])
def change_password():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = CController.changePassword(reqData)
        del sessionTokens[request.headers.get("Authorization")]
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })


@app.route('/profile/change-emailaddress', methods=["POST"])
def change_emailAddress():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = CController.changeEmailAddress(reqData)
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


# @app.route('/account', methods=["GET"])
# def account():
#     if validateToken(request):
#         reqData = request.get_json()
#         reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
#         responseData = CController.getCustomerDetails(reqData)
#         return flask.make_response(responseData)
#     else:
#         return flask.make_response({
#             "status": {
#                 "statusCode": "FAILURE",
#                 "statusMessage": "No valid token"
#             }
#         })


@app.route('/account/wallets', methods=["GET"])
def account_wallets():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = WController.getAllWalletsFromCustomerID(reqData)
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })


@app.route('/account/bundles', methods=["GET"])
def account_bundles():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = WController.getAllBundlesFromCustomerID(reqData)
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })


@app.route('/account/wallets/wallet-address', methods=["GET"])
def account_walletdetails():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = WController.getAllWalletDetailsFromWalletAddress(reqData)
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })


@app.route('/account/bundles/bundle-address', methods=["GET"])
def account_bundledetails():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = BController.getAllBundleDetailsFromBundleAddress(reqData)
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })


@app.route('/account/purchase/wallet', methods=["POST"])
def account_purchasewallet():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = WController.purchaseWallet(reqData)
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })

@app.route('/account/sell/wallet', methods=["POST"])
def account_sellwallet():
    if validateToken(request):
        reqData = request.get_json()
        reqData["customerID"] = sessionTokens[request.headers.get("Authorization")]
        responseData = WController.sellWallet(reqData)
        return flask.make_response(responseData)
    else:
        return flask.make_response({
            "status": {
                "statusCode": "FAILURE",
                "statusMessage": "No valid token"
            }
        })

if __name__ == "__main__":
    app.run()
