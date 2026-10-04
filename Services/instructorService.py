import uuid
from flask import current_app
from Models.Instructor import Instructor


class instructorService:

    def add(data):
        uuid_instructor = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_INSTRUCTOR (INS_UUID, INS_ESPECIALIDAD,
             INS_PER_ID) VALUES (%s, %s, %s) """
        c.execute(sql, (uuid_instructor, data["especialidad"], data["per_id"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {
            "id": id,
            "INS_UUID": uuid_instructor,
            "especialidad": data["especialidad"],
            "per_id": data["per_id"],
        }
        return respuesta

    def delete(id):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_INSTRUCTOR WHERE INS_ID = %s", (id,))
        c.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        if filas_afectadas == 0:
            return None
        return {"mensaje": f"Instructor {id} eliminado correctamente"}

    def update(id, data):
        sql = """
            UPDATE T_INSTRUCTOR
            SET INS_ESPECIALIDAD = COALESCE(%s, INS_ESPECIALIDAD),
                INS_PER_ID       = COALESCE(%s, INS_PER_ID)
            WHERE INS_ID = %s
        """
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (data.get("especialidad"), data.get("per_id"), id))
        c.connection.commit()
        c.close()
        return {"mensaje": f"Instructor {id} actualizado correctamente"}

    def show():
        sql = "SELECT * FROM T_INSTRUCTOR"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [Instructor(x[0], x[1], x[2], x[3]).to_dict() for x in data]

    def searchByID(id):
        sql = "SELECT * FROM T_INSTRUCTOR WHERE INS_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        if not data:
            return None
        return Instructor(data[0], data[1], data[2], data[3]).to_dict()