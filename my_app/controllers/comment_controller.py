from app.models.comment import Comment
from app import db

def get_comments_by_post(post_id):
    return Comment.query.filter_by(post_id=post_id).all()

def create_comment(post_id, content):
    new_comment = Comment(post_id=post_id, content=content)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment
