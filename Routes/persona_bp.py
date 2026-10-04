# blueprint  
from flask import Blueprint
from Controllers.personaController import personaController

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/', methods=['GET'])
def home():
    return personaController.show()

@persona_bp.route('/', methods=['POST'])
def add():
    return personaController.add()

@persona_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return personaController.searchByID(id)

@persona_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return personaController.update(id)

@persona_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return personaController.delete(id)