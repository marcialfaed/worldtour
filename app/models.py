from .database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String)

class Establishment(db.Model):
    __tablename__ = 'establishments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    contact_info = db.Column(db.String)
    location = db.relationship("Location", back_populates="establishments")

Location.establishments = db.relationship("Establishment", order_by=Establishment.id, back_populates="location")
