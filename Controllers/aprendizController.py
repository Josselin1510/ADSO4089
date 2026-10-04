from flask import request, jsonify
from Services.aprendizService import aprendizService
from Controllers.validation import missing_fields


class AprendizController:

    
    def show():
        data = aprendizService.show()
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