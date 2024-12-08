from flask import Blueprint, jsonify
from app.models import Question

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    result = [{'id': q.id, 'question': q.question} for q in questions]
    return jsonify(result)
