from . import db
# from flask_login import UserMixin

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    poster = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime)  # Corrected data type to db.DateTime

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def __repr__(self):
        return '<Movie %r>' % self.poster
