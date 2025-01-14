# Add any model classes for Flask-SQLAlchemy here
from . import db

class Movies(db.Model):
    
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text())
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime())

    def get_id(self):
            try:
                return unicode(self.id)  # python 2 support
            except NameError:
                return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.title)
    
    def  __init__  (self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at