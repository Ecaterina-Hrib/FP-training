from datetime import datetime
from . import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    hearts = db.Column(db.Integer, default=0)
    sentiment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Post {self.id}: {self.content}>'

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'likes': self.likes,
            'hearts': self.hearts,
            'sentiment': self.sentiment
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
