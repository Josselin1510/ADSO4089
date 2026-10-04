import uuid
from flask import current_app
from Models.MatEva import MatEva


class matEvaService:

    def add(data):
        uuid_mat_eva = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_MAT_EVA (MATE_UUID, MATE_NOTA,
             MATE_EVA_ID, MATE_MAT_ID) VALUES (%s, %s, %s, %s) """
        c.execute(
            sql,
            (uuid_mat_eva, data["nota"], data["eva_id"], data["mat_id"]),
        )
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {
            "id": id,
            "MATE_UUID": uuid_mat_eva,
            "nota": data["nota"],
            "eva_id": data["eva_id"],
            "mat_id": data["mat_id"],
        }
        return respuesta

    def delete(id):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_MAT_EVA WHERE MATE_ID = %s", (id,))
        c.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        if filas_afectadas == 0:
            return None
        return {"mensaje": f"Registro matrícula-evaluación {id} eliminado correctamente"}

    def update(id, data):
        sql = """
            UPDATE T_MAT_EVA
            SET MATE_NOTA   = COALESCE(%s, MATE_NOTA),
                MATE_EVA_ID = COALESCE(%s, MATE_EVA_ID),
                MATE_MAT_ID = COALESCE(%s, MATE_MAT_ID)
            WHERE MATE_ID = %s
        """
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (data.get("nota"), data.get("eva_id"), data.get("mat_id"), id))
        c.connection.commit()
        c.close()
        return {"mensaje": f"Registro matrícula-evaluación {id} actualizado correctamente"}

    def show():
        sql = "SELECT * FROM T_MAT_EVA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [MatEva(x[0], x[1], x[2], x[3], x[4]).to_dict() for x in data]

    def searchByID(id):
        sql = "SELECT * FROM T_MAT_EVA WHERE MATE_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        if not data:
            return None
        return MatEva(data[0], data[1], data[2], data[3], data[4]).to_dict()