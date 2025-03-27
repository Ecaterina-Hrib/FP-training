from models import db
from models.post import Post

def create_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_all_posts():
    return Post.query.all()

def like_post(id):
    post = Post.query.get_or_404(id)
    post.likes += 1
    db.session.commit()
    return post

def dislike_post(id):
    post = Post.query.get_or_404(id)
    post.dislikes += 1
    db.session.commit()
    return post
