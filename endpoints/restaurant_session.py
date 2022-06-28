from flask import Flask, jsonify,request
from helper.dbhelpers import run_query
from app  import app
import uuid
import bcrypt
import uuid



#restaurant_session API
@app.post('/api/restaurant-session')
def restaurantSession_post():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print (uuid.uuid4().hex)
    if not email: 
        return jsonify("missing arguement requirement: email"),422
    if not password:
        return jsonify("missing argument requirement: password"),422

    checkuser = run_query("SELECT * FROM restaurant WHERE email=? and password=?",[email,password])
    if checkuser == []:
        return jsonify("user not found!"),401
    user_id = checkuser[0][0]
    #db write select quiery that matches the email and password
    create_token = uuid.uuid4().hex
    print(uuid.uuid4().hex)
    run_query("INSERT INTO restaurant_session (token,restaurant_id) VALUES(?,?)",[create_token, user_id])
    #if it matches create a session token with uuid.uuid4
    
    #if it doesn't match say "404: Error the is no profile found"
    return jsonify("User loggin in!"),200