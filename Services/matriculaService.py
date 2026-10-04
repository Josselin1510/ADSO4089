import uuid
from flask import current_app
from Models.Matricula import Matricula


class matriculaService:

    def add(data):
        uuid_mat = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_MATRICULA (MAT_UUID, MAT_ESTADO,
             MAT_FECHA_INCRIPCION, MAT_APR_ID, MAT_CUR_ID)
             VALUES (%s, %s, %s, %s, %s) """
        c.execute(
            sql,
            (
                uuid_mat,
                data["estado"],
                data["fecha_inscripcion"],
                data["apr_id"],
                data["cur_id"],
            ),
        )
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {
            "id": id,
            "MAT_UUID": uuid_mat,
            "estado": data["estado"],
            "fecha_inscripcion": data["fecha_inscripcion"],
            "apr_id": data["apr_id"],
            "cur_id": data["cur_id"],
        }
        return respuesta

    def delete(id):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_MATRICULA WHERE MAT_ID = %s", (id,))
        c.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        if filas_afectadas == 0:
            return None
        return {"mensaje": f"Matrícula {id} eliminada correctamente"}

    def update(id, data):
        sql = """
            UPDATE T_MATRICULA
            SET MAT_ESTADO            = COALESCE(%s, MAT_ESTADO),
                MAT_FECHA_INSCRIPCION = COALESCE(%s, MAT_FECHA_INSCRIPCION),
                MAT_APR_ID            = COALESCE(%s, MAT_APR_ID),
                MAT_CUR_ID            = COALESCE(%s, MAT_CUR_ID)
            WHERE MAT_ID = %s
        """
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get("estado"),
            data.get("fecha_inscripcion"),
            data.get("apr_id"),
            data.get("cur_id"),
            id,
        ))
        c.connection.commit()
        c.close()
        return {"mensaje": f"Matrícula {id} actualizada correctamente"}

    def show():
        sql = "SELECT * FROM T_MATRICULA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [Matricula(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]

    def searchByID(id):
        sql = "SELECT * FROM T_MATRICULA WHERE MAT_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        if not data:
            return None
        return Matricula(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()