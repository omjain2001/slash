from functools import wraps
import secrets
from flask import Flask, request, send_from_directory, redirect, session, render_template
from flask.json import jsonify
from src.scraper import driver
from dotenv import load_dotenv
import pymongo
import os

app = Flask(__name__, static_folder='./frontend', static_url_path='')
app.secret_key = b'\xc3\x08\xde\x13{E\xad\x0f\xf4T\x81\xc8\x92\x84\xe9\x14'

# Database config

load_dotenv()
os.environ['USERNAME'] = 'se_project3'
os.environ['PASSWORD'] = '1234'

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

# mongoURI = "mongodb+srv://" + username + ":" + password + \
#     "@cluster0.cfulwip.mongodb.net/?retryWrites=true&w=majority"
mongoURI = "mongodb+srv://se_project3:1234@cluster0.cfulwip.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongoURI)

db = client.slashUsers
# Routes

# Decorator method to make login required


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/signIn')

    return wrap


@app.route("/signIn")
def signIn():
    return render_template('loginpage.html')


@app.route('/signUp')
def signUp():
    return render_template('signup.html')


@app.route("/")
@login_required
def landingpage():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/search", methods=["POST", "GET"])
def product_search(new_product="", sort=None, currency=None, num=None):
    product = request.args.get("product_name")
    if product is None:
        product = new_product
    data = driver(product, currency, num, 0, False, None, True, sort)
    return jsonify(data)


@app.route("/filter", methods=["POST", "GET"])
def product_search_filtered():

    product = request.args.get("product_name")
    sort = request.form["sort"]
    currency = request.form["currency"]
    num = request.form["num"]

    if sort == "default":
        sort = None
    if currency == "usd":
        currency = None
    if num == "default":
        num = None
    return product_search(product, sort, currency, num)

from src.user import routes

if __name__ == "__main__":
    # app.config["SECRET_KEY"] = secrets.token_bytes(16)
    app.run()
