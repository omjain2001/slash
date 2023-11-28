from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from src.app import db

import uuid

class User:
    
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
    
    def returnUser(self):
        return session['user']

    def signup(self):
        # Create user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "favorites": []  # Empty list of products as favorites
        }
        print('sssssss', request.form.get('name'))

        #Encrypt the password
        user["password"] = pbkdf2_sha256.hash(user['password'])

        #Check for existing user in db
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400
        
        if db.users.insert_one(user):
            return self.start_session(user)
        
        return jsonify({"error": "Signup failed"}), 400
    
    def login(self):
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        
        return jsonify({"error": "Invalid credentials"}), 401
    
    def signout(self):
        session.clear()
        return redirect('/')
    
    # def is_logged_in(self):
    #     if 'logged_in' in session and session['logged_in']:
    #         return True
    #     return False

    def getProfile(self):
        user = session['user']
        return jsonify(user), 200
    
    def addProduct(self, product):
        print('sssssss', product)
        # Check if the user is logged in
        if 'user' in session:
            user = session['user']
            
            # Assuming 'favorites' is a key in the user dictionary
            favorites = user.get('favorites', {})

            # Check if the product is already in the favorites list
            if product['title'] not in favorites:
                # Add the product to the favorites list
                favorites.append(product)

                # Update the user's favorites in the session
                user['favorites'] = favorites
                session.modified = True  # Mark the session as modified
                db.users.update_one({"_id": user["_id"]}, {"$set": {"favorites": favorites}})
                # You can also update the user's favorites in the database if needed
                # For example: db.users.update_one({"_id": user["_id"]}, {"$set": {"favorites": favorites}})

                return jsonify({"message": "Product added to favorites"}), 200
            else:
                return jsonify({"error": "Product already in favorites"}), 400
        else:
            return jsonify({"error": "User not logged in"}), 401
