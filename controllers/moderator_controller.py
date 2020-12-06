from app import app
from models import *
from flask import request, jsonify, json


@app.route('/moderator/pendarticle/<id>', methods=['PUT', 'DELETE'])
def change_pending_p_article_by_id(id):  # noqa: E501
    """get list of pending article

    get pending article # noqa: E501

    :param id: The name that needs to be fetched. Use user1 for testing.
    :type id: int

    :rtype: PArticle
    """
    p_article = PArticle.query.filter_by(id=id).first()
    if p_article is None:
        return jsonify(status="Bad id"), 404

    if p_article.status == StatusEnum.done:
        return jsonify(status='Already changed'), 400

    if request.method == 'DELETE':
        db.session.delete(p_article)
        db.session.commit()
        return jsonify(status='deleted'), 201

    if request.method == "PUT":
        article = Article.query.filter_by(id=p_article.article_id).first()
        if article is None:
            return jsonify(status='article not found'), 404
        article.text = p_article.text
        article.name = p_article.name
        p_article.status = StatusEnum.done
        db.session.commit()
        return jsonify(status='updated article')


@app.route('/moderator/pendarticle/', methods=['GET'])
def get_pending_articles():  # noqa: E501
    """get list of pending article
    :rtype: PArticle[]
    """
    p_articles = PArticle.query.filter_by(status=StatusEnum.pending).all()
    p_articles_list = {'p_articles_list': []}
    for p_article in p_articles:
        p_articles_list['p_articles_list'].append({'id': p_article.id, 'text': p_article.text, 'name': p_article.name})
    return jsonify(p_articles_list)


@app.route('/moderator/pendarticle/<id>', methods=['GET'])
def get_pending_article_by_id(id):  # noqa: E501
    """get list of pending article

    get pending article # noqa: E501

    :param id: The name that needs to be fetched. Use user1 for testing.
    :type id: int

    :rtype: PArticle
    """
    p_article = PArticle.query.filter_by(id=id).first()
    if p_article is None:
        return jsonify(status="Bad id"), 404

    return jsonify(
        {'id': p_article.id, 'text': p_article.text, 'article_id': p_article.article_id, 'name': p_article.name})
