from flask import Flask, jsonify
from flask_mysqldb import MySQL
from Config import Config

# Importación de las rutas (Blueprints)
from Routes.persona_bp import persona_bp
from Routes.aprendiz_bp import apr_bp
from Routes.instructor_bp import instructor_bp
from Routes.curso_bp import curso_bp
from Routes.matricula_bp import matricula_bp
from Routes.imparte_bp import imparte_bp
from Routes.evaluacion_bp import evaluacion_bp
from Routes.matEva_bp import matEva_bp

app = Flask(__name__)

# Configuración de base de datos
app.config.from_object(Config) 
mysql = MySQL(app)
app.mysql = mysql

# Registro de rutas / Blueprints en la aplicación
app.register_blueprint(persona_bp, url_prefix='/personas')
app.register_blueprint(apr_bp, url_prefix='/aprendices')
app.register_blueprint(instructor_bp, url_prefix='/instructores')
app.register_blueprint(curso_bp, url_prefix='/cursos')
app.register_blueprint(matricula_bp, url_prefix='/matriculas')
app.register_blueprint(imparte_bp, url_prefix='/impartes')
app.register_blueprint(evaluacion_bp, url_prefix='/evaluaciones')
app.register_blueprint(matEva_bp, url_prefix='/matevas')


# Ruta principal de bienvenida / comprobación
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "API ADSO 4089 en ejecución",
        "rutas_disponibles": {
            "personas": "/personas",
            "aprendices": "/aprendices",
            "instructores": "/instructores",
            "cursos": "/cursos",
            "matriculas": "/matriculas",
            "impartes": "/impartes",
            "evaluaciones": "/evaluaciones",
            "matevas": "/matevas"
        }
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
