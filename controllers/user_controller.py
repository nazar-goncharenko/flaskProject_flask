from config import app, auth, db
from models import User
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/', methods=['GET'])
def index():
    return jsonify(status='Hello World'), 200


@auth.verify_password
def verify_password(email, password):
    if not (email and password):
        return False
    user_test = User.query.filter_by(email=email).first()
    if user_test is None:
        return False
    else:
        return check_password_hash(user_test.password, password)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    role = request.json.get('role', None)
    if username and password and email and role and User.query.filter_by(email=email).first() is None:
        if role != 'user' and role != 'moderator':
            return jsonify(status='wrong role'), 404
        new_user = User(userName=username, email=email, password=password, userStatus=23, role=role)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(status='created'), 200
    if User.query.filter_by(email=email).first() is not None:
        return jsonify(status='Email already used'), 400
    else:
        return jsonify(status='Bad data'), 204


@app.route('/users', methods=['PUT', 'DELETE'])
@auth.login_required
def modify_user():
    user_email = auth.current_user()
    user = User.query.filter_by(email=user_email).first()
    if request.method == 'PUT':
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)
        role = request.json.get('role', None)
        if role != 'user' and role != 'moderator':
            return jsonify(status='wrong role'), 404
        user_with_same_email = User.query.filter_by(email=email).first()
        if user_with_same_email is not None and user_with_same_email.id != user.id:
            return jsonify(status='email already used'), 400
        if username and password and email:
            user.userName = username
            user.email = email
            user.password = generate_password_hash(password)
            user.role = role
            db.session.commit()
            return jsonify(status='updated', name=user.userName, email=user.email, role=user.role), 202
        else:
            return jsonify(status='Bad data'), 204
    else:
        db.session.delete(user)
        db.session.commit()
        return jsonify(status='deleted', name=user.userName, email=user.email), 201


@app.route('/users', methods=['GET'])
@auth.login_required
def get_user():
    user_email = auth.current_user()
    user = User.query.filter_by(email=user_email).first()
    return jsonify(status='current User', name=user.userName, email=user.email, role=user.role), 200


def logout_user():
    return jsonify({"msg": "Successfully, you have logged out"}), 200
