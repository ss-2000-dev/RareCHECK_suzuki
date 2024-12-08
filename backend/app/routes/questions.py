from flask import Blueprint, jsonify, request
from app.models import Question

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()
    # Logic to create a question
    return jsonify({'message': 'Question created successfully'})
