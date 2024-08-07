#!/usr/bin/python3
"""
5. API Security and Authentication Techniques
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Datos de usuario en memoria
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin_password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

def admin_required(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        identity = get_jwt_identity()
        if identity['role'] != 'admin':
            return jsonify({"msg": "Admins only!"}), 403
        return fn(*args, **kwargs)
    return wrapper

@app.route('/admin-only')
@admin_required
def admin_only():
    return jsonify(message="Admin Access: Granted")

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing Authorization Header"}), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"msg": "Invalid Token"}), 401

@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"msg": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_response(callback):
    return jsonify({"msg": "Token has been revoked"}), 401

if __name__ == "__main__":
    app.run()
