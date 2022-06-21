from flask import jsonify,request
from helper.dbhelpers import run_query
from app import app

@app.post('/api/orders')
def orders_post():
    data = request.json
    is_canceled = data.get('is_canceled')
    is_confirmed = data.get('is_confirmed')
    is_completed = data.get('is_completed')
    client_id = data.get('client_id')
    restaurant_id = data.get('restaurant_id')
    
    if not is_confirmed:
        return jsonify("missing required arguement: is_confirmed "),422
    if not is_completed:
        return jsonify("missing required arguement: is_completed "),422
    if not is_canceled:
        return jsonify("missing required argument: is_canceled ")
    if not client_id:
        return jsonify("missing required arguement: client_id"),422
    if not restaurant_id:
        return jsonify('missing required argument: restaurant_id'),422
    
    #DB write
    run_query("INSERT INTO orders (is_confirmed, is_completed, is_canceled, client_id,restaurant_id ) VALUES (?,?,?,?,?)", 
                [is_confirmed, is_completed,client_id ,restaurant_id])
    return jsonify("Post created sucsessfully!"),200

@app.get('/api/orders')
def client_get():
    get_content = run_query("SELECT * from orders")
    resp = []
    for content in get_content:
        obj ={}
        obj['id']= content[0]
        obj['is_confirmed']= content[1]
        obj['is_completed']= content[2]
        obj['is_canceled']= content[3]
        obj['client_id']= content[4]
        obj['restaurant_id']= content[5]
        resp.append(obj)
    if not get_content:
        return jsonify("Error , couldn't process get request!"),422
    return jsonify(resp),200

@app.patch('/api/orders')
def orders_patch():
    data = request.json
    is_canceled = data.get('price')
    is_completed = data.get('name')
    is_confirmed = data.get('description')
    
    
    if not is_canceled:
        return jsonify("missing required arguement: price "),422
    if not is_completed:
        return jsonify("missing required arguement: name "),422
    if not is_confirmed :
        return jsonify("missing required arguement: description"),422
    
    #db write
    return jsonify("Updated sucsessfully!"),200