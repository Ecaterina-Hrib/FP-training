from flask import request, jsonify
from models import db
from models.comment import Comment
from models.post import Post

def add_comment(post_id):
    content = request.json.get('content')

    if not content:
        return jsonify({'error': 'Content is required'}), 400

    post = Post.query.get_or_404(post_id)
    comment = Comment(content=content, post_id=post.id)
    db.session.add(comment)
    db.session.commit()

    return jsonify({'id': comment.id, 'content': comment.content, 'created_at': comment.created_at, 'post_id': comment.post_id}), 201

def get_comments(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post.id).all()
    result = []
    for comment in comments:
        result.append({
            'id': comment.id,
            'content': comment.content,
            'created_at': comment.created_at,
        })
    return jsonify(result)
