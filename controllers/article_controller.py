from app import app
from models import *
from flask import request, jsonify, json


@app.route('/articles', methods=['POST'])
def add_article():  # noqa: E501
    """adds an inventory item

    Adds an item to the system
    """
    name = request.json.get('name', None)
    text = request.json.get('text', None)
    if name and text:
        db.session.add(Article(name=name, text=text))
        db.session.commit()
        return jsonify(status='added'), 201
    return jsonify(status='Bas input data'), 400


@app.route('/articles/<id>', methods=['DELETE'])
def delete_article(id):  # noqa: E501
    """Delete article

    This can only be done by moderator. # noqa: E501

    :param id: The article that needs to be deleted
    :type id: int

    """
    article = Article.query.filter_by(id=id).first()
    if article is None:
        return jsonify(status='article not found'), 404

    db.session.delete(article)
    db.session.commit()
    return jsonify(status='deleted'), 201


@app.route('/articles/<id>')
def get_article_by_id(id):
    article = Article.query.filter_by(id=id).first()
    if article is None:
        return jsonify(status='article not found'), 404

    return jsonify(article={'id': article.id, 'text': article.text, 'name': article.name}), 200


@app.route('/articles', methods=['GET'])
def get_all_articles():  # noqa: E501
    """searches inventory

     # noqa: E501


    :rtype: None
    """
    articles = Article.query.all()
    articles_list = {'articles_list': []}
    for article in articles:
        articles_list['articles_list'].append({'id': article.id, 'text': article.text, 'name': article.name})
    return jsonify(articles_list)


@app.route('/articles/<id>', methods=['PUT'])
def update_article(id):  # noqa: E501
    """Updated article

    This can only be done by the logged in user. # noqa: E501

    :param id: The article that need to be updated
    :type id: int

    :rtype: None
    """
    article = Article.query.filter_by(id=id).first()
    if article is None:
        return jsonify(status='article not found'), 404

    new_name = request.json.get('name', None)
    new_text = request.json.get('text', None)
    if new_name and new_text:
        particle = PArticle(name=new_name, text=new_text, status=StatusEnum.pending, article=article)
        db.session.add(particle)
        db.session.commit()
        return jsonify(status='added to pArticle'), 202
    else:
        return jsonify(status='Bad input data'), 204
