
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
    phone_number = data.get('phone_number')
    profile_url = data.get('profile_url')
    banner_url=data.get('banner_url')
    bio = data.get('bio')
    city = data.get('city')
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
    run_query("INSERT INTO restaurant (email,password,name, phone_number, address, bio, banner_url, profile_url, city ) VALUE (?,?,?,?,?,?,?,?,?)", 
                [email,password,name,address,phone_number,bio,profile_url,banner_url,city])
    return jsonify("Post created sucsessfully!"),200

@app.get('/api/restaurant')
def restaurant_get():
    headers = request.headers
    tokens = headers.get("token")
    if not tokens :
        
        return jsonify("user is not authorized"),401
    
    checkuser = run_query("SELECT restaurant_id FROM restaurant_session WHERE token=?", [tokens])
    if checkuser == []:
        return jsonify("user does not have access!"),401
    client_id = checkuser[0][0]
    get_content = run_query("SELECT id, email, name, phone_number, address, bio, city, profile_url, banner_url FROM restaurant WHERE id=?",[client_id])
    
    res = []
    for content in get_content:
        obj={}
        obj['id']=content[0]
        obj['email']=content[1]
        obj['password']=content[2]
        obj['name']=content[3]
        obj['phone_number']=content[4]
        obj['address']=content[5]
        obj['description']=content[6]
        obj['banner_url']=content[7]
        obj['profile_url']=content[8]
        res.append(obj)
    if not get_content:
        return jsonify("Error, couldn't process get request!"),422
    return jsonify(res),200

@app.patch('/api/client')
def restaurant_patch():
    headers = request.headers
    tokens = headers.get("token")
    if not tokens :
        
        return jsonify("user is not authorized"),401
    
    checkuser = run_query("SELECT restaurant_id FROM restaurant_session WHERE token=?", [tokens])
    if checkuser == []:
        return jsonify("user does not have access!"),401
    client_id = checkuser[0][0]
    run_query("SELECT id, email, name, phone_number, address, bio, city, profile_url, banner_url FROM restaurant WHERE id=?",[client_id])
    
    data = request.json
    banner_url = data.get('banner_url')
    name = data.get('name')
    address = data.get('address')
    city = data.get('city')
    profile_url = data.get('profile_url')
    banner_url = data.get('banner_url')
    
    #db write
    run_query("UPDATE restaurant SET profile_url=? banner_url=? WHERE id=?", 
                [profile_url,banner_url])
    return jsonify("Updated sucsessfully!"),200


@app.delete('/api/restaurant')
def restaurant_delete():
    headers = request.headers
    tokens = headers.get("token")
    if not tokens :
        
        return jsonify("user is not authorized"),401
    
    checkuser = run_query("SELECT restaurant_id FROM restaurant_session WHERE token=?", [tokens])
    if checkuser == []:
        return jsonify("user does not have access!"),401
    client_id = checkuser[0][0]
    run_query("SELECT id, email, name, phone_number, address, bio, city, profile_url, banner_url FROM restaurant WHERE id=?",[client_id])
    
    data = request.json
    restaurant_id= data.get('restaurant_id')
    if not restaurant_id:
        return jsonify('Error , couldnt process get request!'),422
    #DB write
    run_query("DELETE FROM restaurant WHER id=?", [restaurant_id])
    return jsonify("Deleted the restaurant sucessfully!"),200
