from flask import jsonify, request
from Services.instructorService import instructorService
from Controllers.validation import missing_fields


class InstructorController:

    
    def show():
        data = instructorService.show()
        return jsonify(data), 200

    def searchByID(id):
        data = instructorService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Instructor no encontrado"}), 404
        return jsonify(data), 200

   
    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["especialidad", "per_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = instructorService.add(data)
        return jsonify(x), 201

    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        x = instructorService.update(id, data)
        return jsonify(x), 200

    def delete(id):
        x = instructorService.delete(id)
        return jsonify(x), 200