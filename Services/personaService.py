import uuid
from flask import current_app
from Models.Persona import Persona


class personaService:

    def add(data):
        uuid_persona = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_PERSONA (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOC)
             VALUES (%s, %s, %s, %s, %s, %s) """
        c.execute(
            sql,
            (
                uuid_persona,
                data["primer_nombre"],
                data["segundo_nombre"],
                data["primer_apellido"],
                data["segundo_apellido"],
                data["documento"],
            ),
        )
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {
            "id": id,
            "PER_UUID": uuid_persona,
            "primer_nombre": data["primer_nombre"],
            "segundo_nombre": data["segundo_nombre"],
            "primer_apellido": data["primer_apellido"],
            "segundo_apellido": data["segundo_apellido"],
            "documento": data["documento"],
        }
        return respuesta

    def delete(id):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_PERSONA WHERE PER_ID = %s", (id,))
        c.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        if filas_afectadas == 0:
            return None
        return {"mensaje": f"Persona {id} eliminada correctamente"}

    def update(id, data):
        sql = """
            UPDATE T_PERSONA
            SET PER_PRI_NOMBRE   = COALESCE(%s, PER_PRI_NOMBRE),
                PER_SEG_NOMBRE   = COALESCE(%s, PER_SEG_NOMBRE),
                PER_PRI_APELLIDO = COALESCE(%s, PER_PRI_APELLIDO),
                PER_SEG_APELLIDO = COALESCE(%s, PER_SEG_APELLIDO),
                PER_DOC          = COALESCE(%s, PER_DOC)
            WHERE PER_ID = %s
        """
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get("primer_nombre"),
            data.get("segundo_nombre"),
            data.get("primer_apellido"),
            data.get("segundo_apellido"),
            data.get("documento"),
            id,
        ))
        c.connection.commit()
        c.close()
        return {"mensaje": f"Persona {id} actualizada correctamente"}

    def show():
        sql = "SELECT * FROM T_PERSONA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [Persona(x[0], x[1], x[2], x[3], x[4], x[5], x[6]).to_dict() for x in data]

    def searchByID(id):
        sql = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        if not data:
            return None
        return Persona(data[0], data[1], data[2], data[3], data[4], data[5], data[6]).to_dict()