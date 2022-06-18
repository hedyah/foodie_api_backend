from flask import Flask, jsonify, request
from helper.dbhelpers import run_query
from app import app


#client_session API
@app.post('/api/client-session')
def clientSession_post():
    data = request.json
    email = data.get('email')
    password = data.get('password')