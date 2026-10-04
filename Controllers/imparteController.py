from flask import jsonify, request
from Services.imparteService import imparteService
from Controllers.validation import missing_fields


class ImparteController:

    def show():
        data = imparteService.show()
        return jsonify(data), 200

    
    def searchByID(id):
        data = imparteService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Registro no encontrado"}), 404
        return jsonify(data), 200

    
    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["rol", "fecha_asignacion", "cur_id", "ins_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = imparteService.add(data)
        return jsonify(x), 201

    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        x = imparteService.update(id, data)
        return jsonify(x), 200

    
    def delete(id):
        x = imparteService.delete(id)
        return jsonify(x), 200