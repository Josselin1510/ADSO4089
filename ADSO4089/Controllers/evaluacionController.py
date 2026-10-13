from flask import jsonify, request
from Services.evaluacionService import evaluacionService
from Controllers.validation import missing_fields


class evaluacionController:

    def show():
        data = evaluacionService.show()
        return jsonify(data), 200

    def searchByID(id):
        data = evaluacionService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Evaluación no encontrada"}), 404
        return jsonify(data), 200

    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["nombre", "codigo", "porcentaje", "fecha"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = evaluacionService.add(data)
        return jsonify(x), 201

    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        x = evaluacionService.update(id, data)
        return jsonify(x), 200

    def delete(id):
        x = evaluacionService.delete(id)
        if not x:
            return jsonify({"mensaje": "Evaluación no encontrada"}), 404
        if "error" in x:
            return jsonify(x), 400
        return jsonify(x), 200