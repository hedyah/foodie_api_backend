from flask import jsonify,request
from helper.dbhelpers import run_query
from app import app
import bcrypt
import sys

#Client API

@app.post('/api/client')
def client_post():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    image_url = data.get('image_url')
    if not email:
        return jsonify("missing required arguement: email "),422
    if not password:
        return jsonify("missing required arguement: password "),422
    if not username:
        return jsonify("missing required arguement: username "),422
    if not first_name:
        return jsonify("missing required arguement: firstName"),422
    if not last_name:
        return jsonify("missing required arguement: lastName "),422
    if not image_url:
        return jsonify("missing argument required: image_url")
    #hash password
    passwordinput = password
    salt =bcrypt.gensalt()
    hash_result = bcrypt.hashpw(passwordinput.encode(), salt)
    print(hash_result)
    #DB write
    run_query("INSERT INTO client (email,password,username,first_name,last_name) VALUE (?,?,?,?,?)", 
                [email,passwordinput,username,first_name,last_name,image_url])
    return jsonify("Post created sucsessfully!")

@app.get('/api/client')
def client_get():
    get_content = run_query("SELECT * from client")
    
    if not get_content:
        return jsonify("Error , couldn't process get request!"),422
    return jsonify(get_content),200

# @app.patch('/api/client')
# def client_patch():
#     data = request.json
#     password = data.get('password')
#     username = data.get('username')
#     first_name = data.get('firstName')
#     image_url = data.get('image_url')
    
#     if not password:
#         return jsonify("missing required arguement: password "),422
#     if not username:
#         return jsonify("missing required arguement: username "),422
#     if not first_name:
#         return jsonify("missing required arguement: firstName"),422
#     if not image_url:
#         return jsonify("missing required argument: image_url"),422
#     #db write
#     return jsonify("Updated sucsessfully!"),200

@app.delete('/api/client')
def client_delete():
    get_content = ()
    
    if not get_content:
        return jsonify('Error , couldnt process get request!'),422
    return jsonify(get_content),200
