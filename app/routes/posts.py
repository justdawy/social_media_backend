from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import Post
from app.extensions import db

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/create', methods=['POST'])
@jwt_required()
def create_post():
    data = request.json
    current_user_id = get_jwt_identity()

    content = data.get('content')
    if not content:
        return jsonify(message='Content is required'), 400
    
    title = data.get('title')

    try:
        post = Post(title=title, content=content, user_id=current_user_id)
        db.session.add(post)
        db.session.commit()

        return jsonify(message='Post created successfully!', post=post.to_json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(message='Failed to create post')