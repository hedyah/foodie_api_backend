import uuid
from flask import jsonify, request
from helper.dbhelpers import run_query
from app import app


#client_session API
@app.post('/api/client-session')
def clientSession_post():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email: 
        return jsonify("missing arguement requirement: email"),422
    if not password:
        return jsonify("missing argument requirement: password"),422

    run_query("SELECT FROM client WHERE email=? and password=? VALUES(?,?)",[email,password])
    
    #db write select quiery that matches the email and password
    token = uuid.uuid4
    print(uuid.uuid4)
    run_query("INSERT INTO client_session (token) VALUES(?,?),"[token])
    #if it matches create a session token with uuid.uuid4
    
    #if it doesnt match say "404: Error the is no profile found"
    return jsonify("User loggin in!"),200