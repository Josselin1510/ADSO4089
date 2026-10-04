from flask import Blueprint
from Controllers.matriculaController import matriculaController

matricula_bp = Blueprint('matricula_bp', __name__)

@matricula_bp.route('/', methods=['GET'])
def home():
    return matriculaController.show()

@matricula_bp.route('/', methods=['POST'])
def add():
    return matriculaController.add()

@matricula_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return matriculaController.searchByID(id)

@matricula_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return matriculaController.update(id)

@matricula_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return matriculaController.delete(id)
