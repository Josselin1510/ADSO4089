import uuid
from flask import current_app
from Models.Evaluacion import Evaluacion


class evaluacionService:

    def add(data):
        uuid_eva = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_EVALUACION (EVA_UUID, EVA_NOMBRE,
             EVA_CODIGO, EVA_PORCENTAJE, EVA_DATE)
             VALUES (%s, %s, %s, %s, %s) """
        c.execute(
            sql,
            (
                uuid_eva,
                data["nombre"],
                data["codigo"],
                data["porcentaje"],
                data["fecha"],
            ),
        )
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {
            "id": id,
            "EVA_UUID": uuid_eva,
            "nombre": data["nombre"],
            "codigo": data["codigo"],
            "porcentaje": data["porcentaje"],
            "fecha": data["fecha"],
        }
        return respuesta

    def delete(id):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_EVALUACION WHERE EVA_ID = %s", (id,))
        c.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        if filas_afectadas == 0:
            return None
        return {"mensaje": f"Evaluación {id} eliminada correctamente"}

    def update(id, data):
        sql = """
            UPDATE T_EVALUACION
            SET EVA_NOMBRE    = COALESCE(%s, EVA_NOMBRE),
                EVA_CODIGO    = COALESCE(%s, EVA_CODIGO),
                EVA_PORCENTAJE = COALESCE(%s, EVA_PORCENTAJE),
                EVA_DATE      = COALESCE(%s, EVA_DATE)
            WHERE EVA_ID = %s
        """
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get("nombre"),
            data.get("codigo"),
            data.get("porcentaje"),
            data.get("fecha"),
            id,
        ))
        c.connection.commit()
        c.close()
        return {"mensaje": f"Evaluación {id} actualizada correctamente"}

    def show():
        sql = "SELECT * FROM T_EVALUACION"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [Evaluacion(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]

    def searchByID(id):
        sql = "SELECT * FROM T_EVALUACION WHERE EVA_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        if not data:
            return None
        return Evaluacion(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()