import uuid
from flask import current_app
from Models.Imparte import Imparte


class imparteService:

    def add(data):
        uuid_imp = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_IMPARTE (IMP_UUID, IMP_ROL,
             IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID)
             VALUES (%s, %s, %s, %s, %s) """
        c.execute(
            sql,
            (
                uuid_imp,
                data["rol"],
                data["fecha_asignacion"],
                data["cur_id"],
                data["ins_id"],
            ),
        )
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {
            "id": id,
            "IMP_UUID": uuid_imp,
            "rol": data["rol"],
            "fecha_asignacion": data["fecha_asignacion"],
            "cur_id": data["cur_id"],
            "ins_id": data["ins_id"],
        }
        return respuesta

    def delete(id):
        c = current_app.mysql.connection.cursor()
        c.execute("DELETE FROM T_IMPARTE WHERE IMP_ID = %s", (id,))
        c.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        if filas_afectadas == 0:
            return None
        return {"mensaje": f"Registro de impartición {id} eliminado correctamente"}

    def update(id, data):
        sql = """
            UPDATE T_IMPARTE
            SET IMP_ROL               = COALESCE(%s, IMP_ROL),
                IMP_FECHA_ASIGNACION  = COALESCE(%s, IMP_FECHA_ASIGNACION),
                IMP_CUR_ID            = COALESCE(%s, IMP_CUR_ID),
                IMP_INS_ID            = COALESCE(%s, IMP_INS_ID)
            WHERE IMP_ID = %s
        """
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get("rol"),
            data.get("fecha_asignacion"),
            data.get("cur_id"),
            data.get("ins_id"),
            id,
        ))
        c.connection.commit()
        c.close()
        return {"mensaje": f"Registro de impartición {id} actualizado correctamente"}

    def show():
        sql = "SELECT * FROM T_IMPARTE"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return [Imparte(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]

    def searchByID(id):
        sql = "SELECT * FROM T_IMPARTE WHERE IMP_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        if not data:
            return None
        return Imparte(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()