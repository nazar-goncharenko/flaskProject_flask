from config import app, db, auth
from models import *
from flask import request, jsonify, json


def check_moderator():
    user_email = auth.current_user()
    user = User.query.filter_by(email=user_email).first()
    return not (user.role != 'moderator' or user is None)


@app.route('/moderator/particle/<particle_id>', methods=['PUT', 'DELETE'])
@auth.login_required
def change_particle_by_id(particle_id):
    if not check_moderator():
        return jsonify(status='You have no permission to do this'), 404

    p_article = PArticle.query.filter_by(id=particle_id).first()
    if p_article is None:
        return jsonify(status='article not found'), 404

    if p_article.status == StatusEnum.done:
        return jsonify(status='Already changed'), 208

    if request.method == "PUT":
        article = Article.query.filter_by(id=p_article.article_id).first()
        article.text = p_article.text
        article.name = p_article.name
        p_article.status = StatusEnum.done
        db.session.commit()
        return jsonify(status='updated article'), 200
    else:
        db.session.delete(p_article)
        db.session.commit()
        return jsonify(status='deleted'), 201


@app.route('/moderator/particle', methods=['GET'])
@auth.login_required
def get_pending_articles():
    if not check_moderator():
        return jsonify(status='You have no permission to do this'), 404
    p_articles = PArticle.query.filter_by(status=StatusEnum.pending).all()
    p_articles_list = {'p_articles_list': []}
    for p_article in p_articles:
        p_articles_list['p_articles_list'].append({'id': p_article.id, 'text': p_article.text, 'name': p_article.name})
    return jsonify(p_articles_list), 200


@app.route('/moderator/particle/<particle_id>', methods=['GET'])
@auth.login_required
def get_pending_article_by_id(particle_id):
    if not check_moderator():
        return jsonify(status='You have no permission to do this'), 404

    p_article = PArticle.query.filter_by(id=particle_id).first()
    if p_article is None:
        return jsonify(status='article not found'), 404

    return jsonify(
        {'id': p_article.id, 'text': p_article.text, 'article_id': p_article.article_id, 'name': p_article.name}), 200
