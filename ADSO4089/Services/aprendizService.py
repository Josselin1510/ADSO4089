import uuid
from flask import current_app
from Models.Aprendiz import Aprendiz


class aprendizService:

    def show():
        sql = "SELECT * FROM T_APRENDIZ"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [
            Aprendiz(x[0], x[1], x[2], x[3]).to_dict() for x in data
        ] if data else []

    def searchByID(id):
        sql = "SELECT * FROM T_APRENDIZ WHERE APR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()

        if not data:
            return None

        return Aprendiz(data[0], data[1], data[2], data[3]).to_dict()

    def add(data):
        uuid_apr = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()

        sql = """
            INSERT INTO T_APRENDIZ (APR_UUID, APR_FECHA_NAC, APR_PER_ID)
            VALUES (%s, %s, %s)
        """

        c.execute(sql, (uuid_apr, data["fecha_nac"], data["per_id"]))
        c.connection.commit()

        inserted_id = c.lastrowid
        c.close()

        return {
            "id": inserted_id,
            "uuid": uuid_apr,
            "fecha_nac": data["fecha_nac"],
            "per_id": data["per_id"],
        }

    def update(id, data):
        c = current_app.mysql.connection.cursor()

        sql = """
            UPDATE T_APRENDIZ
            SET APR_FECHA_NAC = %s, APR_PER_ID = %s
            WHERE APR_ID = %s
        """

        c.execute(sql, (data["fecha_nac"], data["per_id"], id))
        c.connection.commit()
        c.close()

        return {"mensaje": f"Aprendiz con ID {id} actualizado correctamente"}

    def delete(id):
        try:
            c = current_app.mysql.connection.cursor()
            sql = "DELETE FROM T_APRENDIZ WHERE APR_ID = %s"
            c.execute(sql, (id,))
            c.connection.commit()
            filas_afectadas = c.rowcount
            c.close()
            if filas_afectadas == 0:
                return None
            return {"mensaje": f"Aprendiz con ID {id} eliminado correctamente"}
        except Exception as e:
            if "1451" in str(e) or "foreign key" in str(e).lower():
                return {"error": "No se puede eliminar el aprendiz porque tiene registros asociados"}
            return {"error": str(e)}