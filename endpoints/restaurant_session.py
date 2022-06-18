from flask import Flask, jsonify,request
from helper.dbhelpers import run_query
from app  import app
import bcrypt
import hashlib
import uuid



#restaurant_session API
@app.post('/api/restaurant-session')
def restaurantSession_post():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print (uuid.uuid4)