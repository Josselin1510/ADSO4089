from flask import Blueprint
from Controllers.instructorController import instructorController

instructor_bp = Blueprint('instructor_bp', __name__)

@instructor_bp.route('/', methods=['GET'])
def home():
    return instructorController.show()

@instructor_bp.route('/', methods=['POST'])
def add():
    return instructorController.add()

@instructor_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return instructorController.searchByID(id)

@instructor_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return instructorController.update(id)

@instructor_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return instructorController.delete(id)
