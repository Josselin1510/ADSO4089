from flask import Blueprint
from Controllers.evaluacionController import evaluacionController

evaluacion_bp = Blueprint('evaluacion_bp', __name__)

@evaluacion_bp.route('/', methods=['GET'])
def home():
    return evaluacionController.show()

@evaluacion_bp.route('/', methods=['POST'])
def add():
    return evaluacionController.add()

@evaluacion_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return evaluacionController.searchByID(id)

@evaluacion_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return evaluacionController.update(id)

@evaluacion_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return evaluacionController.delete(id)
