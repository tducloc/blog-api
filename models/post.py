from ..db import db
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author = db.Column(db.String, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="posts")
    tags = relationship("Tag", secondary="post-tag", back_populates="posts")
    comments = relationship("Comment", back_populates="comments")
    liked_users = relationship("User", secondary="like", back_populates="likes")
    read_users = relationship("User", secondary="read", back_populates="reads")
    favorite_users = relationship(
        "User", secondary="favorite", back_populates="favorites"
    )


post_tag = Table(
    "post_tag",
    db.Model.metadata,
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)
