import uuid
from flask import current_app
from Models.Curso import Curso


class cursoService:

    def show():
        sql = "SELECT * FROM T_CURSO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        return [
            Curso(x[0], x[1], x[2], x[3], x[4], x[5], x[6]).to_dict()
            for x in data
        ] if data else []

    def searchByID(id):
        sql = "SELECT * FROM T_CURSO WHERE CUR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()

        if not data:
            return None

        return Curso(
            data[0], data[1], data[2], data[3], data[4], data[5], data[6]
        ).to_dict()

    def add(data):
        uuid_cur = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()

        sql = """
            INSERT INTO T_CURSO (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        c.execute(
            sql,
            (
                uuid_cur,
                data["nombre"],
                data["codigo"],
                data["duracion"],
                data["costo"],
                data["descripcion"],
            ),
        )
        c.connection.commit()

        inserted_id = c.lastrowid
        c.close()

        return {
            "id": inserted_id,
            "uuid": uuid_cur,
            "nombre": data["nombre"],
            "codigo": data["codigo"],
            "duracion": data["duracion"],
            "costo": data["costo"],
            "descripcion": data["descripcion"],
        }

    def update(id, data):
        c = current_app.mysql.connection.cursor()

        sql = """
            UPDATE T_CURSO
            SET CUR_NOMBRE = %s, CUR_CODIGO = %s, CUR_DURACION = %s, CUR_COSTO = %s, CUR_DESCRIPCION = %s
            WHERE CUR_ID = %s
        """

        c.execute(
            sql,
            (
                data["nombre"],
                data["codigo"],
                data["duracion"],
                data["costo"],
                data["descripcion"],
                id,
            ),
        )
        c.connection.commit()
        c.close()

        return {"mensaje": f"Curso con ID {id} actualizado correctamente"}

    def delete(id):
        c = current_app.mysql.connection.cursor()

        sql = "DELETE FROM T_CURSO WHERE CUR_ID = %s"

        c.execute(sql, (id,))
        c.connection.commit()
        c.close()

        return {"mensaje": f"Curso con ID {id} eliminado correctamente"}