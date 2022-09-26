import flask
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
# import requests
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


# decorating index function with the app.route with url as /login
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
            "status message": "Successfully signed up."
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
            "status message": "Successfully signed in."
        },
        "name": "Welcome user"
    }
    return flask.make_response(response)

@app.route('/view-cryptocurrencies', methods=["GET"])
def view_cryptocurrencies():
    return render_template('search.html')


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


if __name__ == "__main__":
    app.run()
