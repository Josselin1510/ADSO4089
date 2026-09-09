from flask import jsonify, request
from Services.personaService import personaService
from Controllers.validation import missing_fields


class personaController:

    def show():
        data = personaService.show()
        return jsonify(data), 200

    def searchByID(id):
        data = personaService.searchByID(id)
        if not data:
            return jsonify({"mensaje": "Registro no encontrado"}), 404
        return jsonify(data), 200

    def add():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = [
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "documento",
        ]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = personaService.add(data)
        return jsonify(x), 201

    def update(id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({"error": "JSON inválido"}), 400

        campos_req = [
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "documento",
        ]
        faltantes = missing_fields(data, campos_req)
        if faltantes:
            return jsonify({"mensaje": f"Faltan parámetros: {faltantes}"}), 400

        x = personaService.update(id, data)
        return jsonify(x), 200

    def delete(id):
        x = personaService.delete(id)
        return jsonify(x), 200