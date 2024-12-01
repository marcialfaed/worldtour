from flask import request, jsonify
from . import app
from .models import db, User, Location

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([{
        'name': loc.name,
        'description': loc.description,
        'latitude': loc.latitude,
        'longitude': loc.longitude,
        'image_url': loc.image_url
    } for loc in locations])

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users])

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(username=data['username'], password=data['password'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})
