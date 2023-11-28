from flask import Flask, request
from src.app import app, login_required
from src.user.models import User

@app.route('/user/signup/', methods = ['POST'])
def signup():
    return User().signup()

@app.route('/user/login/', methods = ['POST'])
def login():
    return User().login()

@app.route('/user/signout/')
def signout():
    return User().signout()

@app.route('/user/getProfile/', methods = ['GET'])
@login_required
def getProfile():
    return User().getProfile()

@app.route('/user/addProduct/', methods = ['POST'])
@login_required
def addProduct():
    product = {
        "title": request.args.get('title'),
        "rating": request.args.get('rating'),
        "imgSrc": request.args.get('imgSrc'),
		"marketplace": request.args.get('marketplace'),
		"price": request.args.get('price'),
		"currency": request.args.get('currency'),
		"productURL": request.args.get('productURL'),
		"noOfRatings": request.args.get('noOfRatings'),
		"paymentMode": request.args.get('paymentMode')
    }
    return User().addProduct(product)