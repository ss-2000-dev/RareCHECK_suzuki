from flask import Blueprint, jsonify, request, session
from app.models import User
import bcrypt
import uuid
import traceback

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400
        
        user = User.query.filter_by(email=email).first()
        if user is None or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({'message': 'Invalid email or password'}), 400

        session['session_id'] = str(uuid.uuid4())
        session['user_id'] = user.id

        return jsonify({
            'userId': user.id,
            'username': user.username,
            'isAdmin': user.is_admin,
        }), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200
