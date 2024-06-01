# from flask import Blueprint, request, jsonify
# from datastructures import User

# users_bp = Blueprint('user_bp', __name__)


# @users_bp.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.name for user in users])

# @users_bp.route('/user', methods=['POST'])
# def create_user():
#     name = request.json['name']
#     new_user = User(name=name)
#     users_bp.session.add(new_user)
#     users_bp.session.commit()
#     return jsonify({'message': 'Usuario creado con éxito'}), 201


