from flask import Blueprint, request, jsonify
from post import add_post, get_posts, like_post, dislike_post
from comment import add_comment, get_comments

posts_routes = Blueprint("posts_routes", __name__)


@posts_routes.route('/')
def hello_world():
    return 'Hello, World!'


@posts_routes.route('/posts', methods=['POST'])
def create_post():
    return add_post()


@posts_routes.route('/posts', methods=['GET'])
def list_posts():
    return get_posts()


@posts_routes.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    return add_comment(post_id)


@posts_routes.route('/posts/<int:post_id>/comments', methods=['GET'])
def list_comments(post_id):
    return get_comments(post_id)


@posts_routes.route('/posts/<int:post_id>/like', methods=['POST'])
def like_a_post(post_id):
    return like_post(post_id)


# @posts_routes.route('/posts/<int:post_id>/like', methods=['GET'])
# def list_likes(post_id):
#     return get_likes(post_id)

@posts_routes.route('/posts/<int:post_id>/dislike', methods=['POST'])
def dislike_a_post(post_id):
    return dislike_post(post_id)

# @posts_routes.route('/posts/<int:post_id>/dislike', methods=['GET'])
# def list_dislikes(post_id):
#     return get_dislikes(post_id)
