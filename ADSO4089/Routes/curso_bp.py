from flask import Blueprint
from Controllers.cursoController import cursoController

curso_bp = Blueprint('curso_bp', __name__)

@curso_bp.route('/', methods=['GET'])
def home():
    return cursoController.show()

@curso_bp.route('/', methods=['POST'])
def add():
    return cursoController.add()

@curso_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return cursoController.searchByID(id)

@curso_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return cursoController.update(id)

@curso_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return cursoController.delete(id)
