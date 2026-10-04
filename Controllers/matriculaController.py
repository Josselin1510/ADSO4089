from flask import jsonify, request
from Services.matEvaService import matEvaService
from Controllers.validation import missing_fields


class MatEvaController:

    
    def show():
        data = matEvaService.show()
        return jsonify(data), 200

    
    def searchByID(id):
        data = matEvaService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Registro no encontrado"}), 404
        return jsonify(data), 200

    
    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["nota", "eva_id", "mat_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = matEvaService.add(data)
        return jsonify(x), 201

    
    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["nota", "eva_id", "mat_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = matEvaService.update(id, data)
        return jsonify(x), 200

  
    def delete(id):
        x = matEvaService.delete(id)
        return jsonify(x), 200