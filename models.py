from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Class"""

    __tablename__ = 'pets'

    id          = db.Column(db.Integer,
                            primary_key = True)
    name        = db.Column(db.String(),
                            nullable = False)
    species     = db.Column(db.String(),
                            nullable = False)
    photo_url   = db.Column(db.String(),
                            default = 'https://complianz.io/wp-content/uploads/2019/03/placeholder-300x202.jpg.webp')
    age         = db.Column(db.Integer)
    notes       = db.Column(db.Text)
    available   = db.Column(db.Boolean,
                            nullable = False,
                            default = True)