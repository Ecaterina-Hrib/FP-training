from flask import jsonify
from controllers import post_controller

def add_post():
    post = post_controller.create_post()
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content, 'likes': post.likes, 'dislikes': post.dislikes, 'created_at': post.created_at}), 201

def get_posts():
    posts = post_controller.get_all_posts()
    result = []
    for post in posts:
        result.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'likes': post.likes,
            'dislikes': post.dislikes,
            'created_at': post.created_at
        })
    return jsonify(result)

def like_post(id):
    post = post_controller.like_post(id)
    return jsonify({'message': 'Post liked', 'likes': post.likes})

def dislike_post(id):
    post = post_controller.dislike_post(id)
    return jsonify({'message': 'Post disliked', 'dislikes': post.dislikes})
