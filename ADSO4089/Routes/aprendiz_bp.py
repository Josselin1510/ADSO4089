from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def home():
    return aprendizController.show()

@apr_bp.route('/', methods=['POST'])
def add():
    return aprendizController.add()

@apr_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return aprendizController.searchByID(id)

@apr_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return aprendizController.update(id)

@apr_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return aprendizController.delete(id)