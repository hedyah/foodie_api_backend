from flask import jsonify,request
from helper.dbhelpers import run_query
from app import app
import bcrypt

#Client API

@app.get('/api/client')
def client_get():
    get_content = run_query("SELECT * from client")
    resp = []
    for content in get_content:
        obj ={}
        obj['id']= content[0]
        obj['email']= content[1]
        obj['password']= content[2]
        obj['username']= content[3]
        obj['firstName']= content[4]
        obj['lastName']= content[5]
        obj['created_at']= content[6]
        obj['image_url']= content[7]
        resp.append(obj)
    if not get_content:
        return jsonify("Error , couldn't process get request!"),422
    return jsonify(resp),200

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
        return jsonify("missing argument required: image_url"),422
    #hash password
    passwordinput = password
    salt =bcrypt.gensalt()
    hash_result = bcrypt.hashpw(passwordinput.encode(), salt)
    run_query("INSERT INTO client (email,password,username,first_name,last_name,image_url) VALUE (?,?,?,?,?,?)", 
                [email,password,username,first_name,last_name,image_url])
    return jsonify("Post created sucsessfully!"),200



@app.patch('/api/client')
def client_patch():
    data = request.json
    password = data.get('password')
    username = data.get('username')
    first_name = data.get('firstName')
    image_url = data.get('image_url')
    
    if not password:
        return jsonify("missing required arguement: password "),422
    if not username:
        return jsonify("missing required arguement: username "),422
    if not first_name:
        return jsonify("missing required arguement: firstName"),422
    if not image_url:
        return jsonify("missing required argument: image_url"),422
    #db write
    return jsonify("Updated sucsessfully!"),200

@app.delete('/api/client')
def client_delete():
    get_content = ()
    
    if not get_content:
        return jsonify('Error , couldnt process get request!'),422
    return jsonify(get_content),200
