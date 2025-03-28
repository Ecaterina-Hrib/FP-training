from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .comment import Comment
from .post import Post