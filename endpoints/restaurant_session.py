from flask import Flask, jsonify,request
from helper.dbhelpers import run_query
from app  import app
import bcrypt
import uuid



#restaurant_session API
@app.post('/api/restaurant-session')
def restaurantSession_post():
    data = request.json
    user_email = data.get('email')
    user_password = data.get('password')
    print (uuid.uuid4)
    if not user_email: 
        return jsonify("missing arguement requirement: email"),422
    if not user_password:
        return jsonify("missing argument requirement: password"),422

    run_query("SELECT FROM restaurant WHERE email=? and password=? VALUES(?,?)",[user_email,user_password])
    return jsonify("User loggin in!"),200
    #db write select quiery that matches the email and password
    #if it matches create a session token with uuid.uuid4
    #if it doesnt match say "404: Error the is no profile found"