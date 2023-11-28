from functools import wraps
from flask import Flask, request, send_from_directory, redirect, session, render_template, session
from flask.json import jsonify
from src.scraper import driver, condense_helper, searchGoogleShopping
from dotenv import load_dotenv
import pymongo, os
import certifi

app = Flask(__name__, static_folder='./frontend', static_url_path='')
app.secret_key = b'\xc3\x08\xde\x13{E\xad\x0f\xf4T\x81\xc8\x92\x84\xe9\x14'
#Database config

load_dotenv()
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
mongoURI = f"mongodb+srv://se_project3:1234@cluster0.cfulwip.mongodb.net/?retryWrites=true&w=majority&tlsCAFile={certifi.where()}"
client = pymongo.MongoClient(mongoURI)

db = client.slashUsers
#Routes
#from src.user import routes

#Decorator method to make login required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else: 
            return redirect('/signIn')
    
    return wrap

from src.user import routes

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
@login_required
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

@app.route("/navigateToRecommendations")
def recommendPage():
    return send_from_directory(app.static_folder, 'recommendations.html')

@app.route("/getRecommendations")
@login_required
def getRecommendations():
    try:
        user = session['user']
        #titles = [x[0] for x in user['favorites']]
        #print('ssssssss', titles)
        query="iphone+shoes"
        products=searchGoogleShopping(query, 0, None)
        result_condensed = []
        condense_helper(result_condensed, products, 50)
        result_condensed = [p for p in result_condensed if p.get('images') != 'None']
        for p in result_condensed:
            link = p["link"]
            if p["website"] == "Etsy":
                link = link[12:]
                p["link"] = link
            elif "http" not in link:
                link = "http://" + link
                p["link"] = link
                
        return jsonify(result_condensed) 
        
    except Exception as err:
        print(err)
        return jsonify({"error": "Internal server error"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
