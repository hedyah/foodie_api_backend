
from flask import Flask, jsonify, request
from app import app
from helper.dbhelpers import run_query
import bcrypt



#Restaurant API

@app.post('/api/restaurant')
def restaurant_post():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    address = data.get('address')
    city = data.get('city')
    phone_number = data.get('phone_number')
    profile_url = data.get('profile_url')
    banner_url=data.get('banner_url')
    bio = data.get('bio')
    if not email:
        return jsonify("missing required arguement: email "),422
    if not password:
        return jsonify("missing required arguement: password "),422
    if not name:
        return jsonify("missing required arguement: name "),422
    if not address:
        return jsonify("missing required arguement: address"),422
    if not city:
        return jsonify("missing required arguement: city "),422
    if not phone_number:
        return jsonify('missing required argument: phone_number'),422
    #hash password
    passwordinput = password
    salt =bcrypt.gensalt()
    hash_result = bcrypt.hashpw(passwordinput.encode(), salt)
    
    #DB write
    run_query("INSERT INTO restaurant (email,password,name, phone_number, address, bio,city, banner_url, profile_url ) VALUES (?,?,?,?,?,?,?,?,?)", 
                [email,hash_result,name,address,city,phone_number,bio,profile_url,banner_url])
    return jsonify("Post created sucsessfully!"),200

@app.get('/api/restaurant')
def restaurant_get():
    get_content = run_query("SELECT * from restaurant")
    
    if not get_content:
        return jsonify('Error , couldnt process get request!'),422
    return jsonify(get_content),200

@app.patch('/api/client')
def client_patch():
    data = request.json
    password = data.get('password')
    name = data.get('name')
    address = data.get('address')
    city = data.get('city')
    profile_url = data.get('profile_url')
    banner_url = data.get('banner_url')
    
    if not password:
        return jsonify("missing required arguement: password "),422
    if not name:
        return jsonify("missing required arguement: username "),422
    if not address:
        return jsonify("missing required arguement: firstName"),422
    if not city:
        return jsonify("missing required argument: city"),422
    if not profile_url:
        return jsonify("missing required argument: image_url"),422
    #db write
    return jsonify("Updated sucsessfully!"),200


@app.delete('/api/restaurant')
def restaurant_delete():
    get_content = ()
    
    if not get_content:
        return jsonify('Error , couldnt process get request!'),422
    return jsonify(get_content),200
