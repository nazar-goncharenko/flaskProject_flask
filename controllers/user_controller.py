from functools import wraps


from app import app, db
from models import User
from flask import request, jsonify, json, make_response, abort
from app import auth
from werkzeug.security import generate_password_hash, check_password_hash


@auth.verify_password
def verify_password(email, password):
    if not (email and password):
        return False
    userTest = User.query.filter_by(email=email).first()
    if userTest is None:
        return False
    if userTest:
        return check_password_hash(userTest.password, password)
    return False


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/users', methods=['POST'])
def create_user():
    """
    Create user
    :param: username, password
    :type: json
    :rtype: json with status
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    role = request.json.get('role', None)

    if username and password and email and role and User.query.filter_by(email=email).first() is None:
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
def userId():
    """
    Get user by id
    :param: id
    :type: int
    :rtype: current user or not found
    """
    user_email = auth.current_user()
    user = User.query.filter_by(email=user_email).first()
    if user is None:
        return jsonify(status='not found user'), 404

    if request.method == 'PUT':
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)
        role = request.json.get('role', None)
        email_id = User.query.filter_by(email=email).first()
        if email_id is not None:
            if email_id.id != user.id:
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

    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify(status='deleted', name=user.userName, email=user.email), 201


@app.route('/users', methods=['GET'])
@auth.login_required
def get_user():
    user_email = auth.current_user()
    user = User.query.filter_by(email=user_email).first()
    if user is None:
        return jsonify(status='not found user'), 404

    if user.role != 'user' and user.role != 'moderator':
        return jsonify(status='wrong role'), 404

    return jsonify(status='current User', name=user.userName, email=user.email, role=user.role), 200


def login_user(username, password):  # noqa: E501
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    current_user = User.query.filter_by(email=email)
    for i in current_user:
        if check_password_hash(i.password, password):
            return jsonify({"status": "logged_in"}), 200
    else:
        return jsonify({"Error": "Wrong password"}), 401


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return jsonify({"msg": "Successfully, you have logged out"}), 200

