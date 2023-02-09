from datetime import datetime
from flask import Blueprint, jsonify

expense = Blueprint('expenses', __name__, url_prefix='/expenses')


@expense.route("/")
def get_all_expenses():
    data = {
        "success": [
            {
                "id": 1,
                "description": "Conta de luz",
                "value": 320.0,
                "due_date": datetime.now().strftime('%d/%m/%Y')
            },
            {
                "id": 2,
                "description": "Conta de Agua",
                "value": 50.0,
                "due_date": datetime.now().strftime('%d/%m/%Y')
            },
            {
                "id": 1,
                "description": "Conta de internet",
                "value": 129.0,
                "due_date": datetime.now().strftime('%d/%m/%Y')
            },
        ]
    }
    return jsonify(data), 200