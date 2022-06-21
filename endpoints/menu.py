from flask import jsonify,request
from helper.dbhelpers import run_query
from app import app

@app.post('/api/menu')
def menu_post():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    image_url = data.get('image_url')
    restaurant_id = data.get('restaurant_id')
    
    if not name:
        return jsonify("missing required arguement: name "),422
    if not description:
        return jsonify("missing required arguement: description "),422
    if not price:
        return jsonify("missing required arguement: price "),422
    if not image_url:
        return jsonify("missing required arguement: image_url"),422
    if not restaurant_id:
        return jsonify('missing required argument: restaurant_id'),422
    
    #DB write
    run_query("INSERT INTO menu (name, description, price, image_url, restaurant_id ) VALUES (?,?,?,?,?)", 
                [name,description, price,image_url,restaurant_id])
    return jsonify("Post created sucsessfully!"),200

@app.get('/api/menu')
def menu_get():
    get_content = run_query("SELECT * from menu")
    resp = []
    for content in get_content:
        obj ={}
        obj['id']= content[0]
        obj['name']= content[1]
        obj['description']= content[2]
        obj['price']= content[3]
        obj['image_url']= content[4]
        obj['restaurant_id']= content[5]
        resp.append(obj)
    if not get_content:
        return jsonify("Error , couldn't process get request!"),422
    return jsonify(resp),200

@app.patch('/api/menu')
def menu_patch():
    data = request.json
    price = data.get('price')
    name = data.get('name')
    description = data.get('description')
    image_url = data.get('image_url')
    
    if not price:
        return jsonify("missing required arguement: price "),422
    if not name:
        return jsonify("missing required arguement: name "),422
    if not description:
        return jsonify("missing required arguement: description"),422
    if not image_url:
        return jsonify("missing required argument: image_url"),422
    #db write
    return jsonify("Updated sucsessfully!"),200


