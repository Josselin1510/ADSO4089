from flask import jsonify, request
from Services.cursoService import cursoService
from Controllers.validation import missing_fields


class cursoController:

    def show():
        data = cursoService.show()
        return jsonify(data), 200

    def searchByID(id):
        data = cursoService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Curso no encontrado"}), 404
        return jsonify(data), 200

    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["nombre", "codigo", "duracion", "costo", "descripcion"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = cursoService.add(data)
        return jsonify(x), 201

    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = ["nombre", "codigo", "duracion", "costo", "descripcion"]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = cursoService.update(id, data)
        return jsonify(x), 200

    def delete(id):
        x = cursoService.delete(id)
        if not x:
            return jsonify({"mensaje": "Curso no encontrado"}), 404
        if "error" in x:
            return jsonify(x), 400
        return jsonify(x), 200