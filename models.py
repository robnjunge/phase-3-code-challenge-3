
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    given_name = db.Column(db.String(100))
    family_name = db.Column(db.String(100))
    reviews = db.relationship('Review', backref='customer', lazy='dynamic')

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    reviews = db.relationship('Review', backref='restaurant', lazy='dynamic')

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
