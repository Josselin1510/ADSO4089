from flask import request, jsonify
from Services.aprendizService import aprendizService
from Controllers.validation import missing_fields


class aprendizController:

    def show():
        data = aprendizService.show()
        return jsonify(data), 200

    def searchByID(id):
        data = aprendizService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Aprendiz no encontrado"}), 404
        return jsonify(data), 200

    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["fecha_nac", "per_id"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = aprendizService.add(data)
        return jsonify(x), 201

    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        x = aprendizService.update(id, data)
        return jsonify(x), 200

    def delete(id):
        x = aprendizService.delete(id)
        if not x:
            return jsonify({"mensaje": "Aprendiz no encontrado"}), 404
        if "error" in x:
            return jsonify(x), 400
        return jsonify(x), 200