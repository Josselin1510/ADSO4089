from flask import Blueprint
from Controllers.matEvaController import matEvaController

matEva_bp = Blueprint('matEva_bp', __name__)

@matEva_bp.route('/', methods=['GET'])
def home():
    return matEvaController.show()

@matEva_bp.route('/', methods=['POST'])
def add():
    return matEvaController.add()

@matEva_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return matEvaController.searchByID(id)

@matEva_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return matEvaController.update(id)

@matEva_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return matEvaController.delete(id)
