from flask import jsonify, request
from services import (
    create_post, get_post, get_all_posts,
    update_post, delete_post,
    like_post_by_id, love_post_by_id,
    get_post_likes, get_post_hearts)


def add_post():
    try:
        data = request.get_json()
        new_post = create_post(data)
        return jsonify(new_post), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def get_post_by_id(post_id):
    post = get_post(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({"message": "Post not found"}), 404


def get_posts():
    posts = get_all_posts()
    if not posts:
        return jsonify([]), 200
    return jsonify(posts), 200


def put_post_by_id(post_id):
    try:
        data = request.get_json()
        updated_post = update_post(post_id, data)
        return jsonify(updated_post), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def delete_post_by_id(post_id):
    try:
        result = delete_post(post_id)
        if result.get("message") == "Post not found":
            return jsonify(result), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def like_post(post_id):
    result = like_post_by_id(post_id)
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Post not found"}), 404


def get_likes(post_id):
    result = get_post_likes(post_id)
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Post not found"}), 404


def love_post(post_id):
    result = love_post_by_id(post_id)
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Post not found"}), 404


def get_hearts(post_id):
    result = get_post_hearts(post_id)
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Post not found"}), 404
