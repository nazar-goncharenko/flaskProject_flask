from config import app, auth, db
from models import *
from flask import request, jsonify, json


@app.route('/articles', methods=['POST'])
@auth.login_required
def add_article():
    name = request.json.get('name', None)
    text = request.json.get('text', None)
    if name and text:
        db.session.add(Article(name=name, text=text))
        db.session.commit()
        return jsonify(status='added'), 201
    return jsonify(status='Bad input data'), 400


@app.route('/articles/<article_id>', methods=['DELETE'])
@auth.login_required
def delete_article(article_id):
    article = Article.query.filter_by(id=article_id).first()
    if article is None:
        return jsonify(status='article not found'), 404

    p_article_list = PArticle.query.filter_by(article_id=article.id)
    for var in p_article_list:
        db.session.delete(var)
    db.session.delete(article)
    db.session.commit()
    return jsonify(status='deleted'), 201


@app.route('/articles/<article_id>', methods=['GET'])
@auth.login_required
def get_article_by_id(article_id):
    article = Article.query.filter_by(id=article_id).first()
    if article is None:
        return jsonify(status='article not found'), 404
    return jsonify(article={'id': article.id, 'text': article.text, 'name': article.name}), 200


@app.route('/articles', methods=['GET'])
@auth.login_required
def get_all_articles():
    articles = Article.query.all()
    articles_list = {'articles_list': []}
    for article in articles:
        articles_list['articles_list'].append({'id': article.id, 'text': article.text, 'name': article.name})
    return jsonify(articles_list), 200


@app.route('/articles/<article_id>', methods=['PUT'])
@auth.login_required
def update_article(article_id):
    article = Article.query.filter_by(id=article_id).first()
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
