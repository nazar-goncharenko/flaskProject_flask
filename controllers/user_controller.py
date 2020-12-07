from app import app, db
from models import *
from flask import request, jsonify, json
from werkzeug.security import generate_password_hash


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

    if username and password and email and User.query.filter_by(email=email).first() is None:
        new_user = User(userName=username, email=email, password=password, userStatus=23)
        db.session.add(new_user)
        db.session.commit()

        return jsonify(status='created'), 200

    if User.query.filter_by(email=email).first() is not None:
        return jsonify(status='Email already used'), 400
    else:
        return jsonify(status='Bad data'), 204


@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def userId(id):
    """
    Get user by id
    :param: id
    :type: int
    :rtype: current user or not found
    """
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify(status='not found user'), 404

    if request.method == 'GET':
        return jsonify(status='current User', name=user.userName, email=user.email), 200

    if request.method == 'PUT':
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)
        email_id = User.query.filter_by(email=email).first()
        if email_id is not None:
            if email_id.id != user.id:
                return jsonify(status='email already used'), 400
        if username and password and email:
            user.userName = username
            user.email = email
            user.password = generate_password_hash(password)
            db.session.commit()
            return jsonify(status='updated', name=user.userName, email=user.email), 202
        else:
            return jsonify(status='Bad data'), 204

    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify(status='deleted', name=user.userName, email=user.email), 201


def login_user(username, password):  # noqa: E501
    """Logs user into the system
    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'

