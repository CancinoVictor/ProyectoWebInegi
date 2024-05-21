import pymysql
from modelo.package_model.Database import Database

class Usuario:

    def __init__(self, id=0, nombre='', contraseña='', rol=''):
        self.__id_usuario = id
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__rol = rol

    def update_usuario(self, obj_usuario):
        conexion = Database()
        try:
            with conexion.conn.cursor() as cursor:
                query = "UPDATE usuarios SET nombre=%s, contraseña=%s, rol=%s WHERE id=%s"
                vals = (obj_usuario.__nombre, obj_usuario.__contraseña, obj_usuario.__rol, obj_usuario.__id_usuario)
                affected = cursor.execute(query, vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
        except Exception as e:
            return str(e)
        finally:
            conexion.close()

    def eliminar_usuario(self, id):
        conexion = Database()
        try:
            with conexion.conn.cursor() as cursor:
                affected = cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
                conexion.conn.commit()
            return affected
        except Exception as e:
            return str(e)
        finally:
            conexion.close()

    def insertar_usuario(self, obj_usuario):
        conexion = Database()
        try:
            with conexion.conn.cursor() as cursor:
                query = "INSERT INTO usuarios(nombre, contraseña, rol) VALUES (%s, %s, %s)"
                vals = (obj_usuario.__nombre, obj_usuario.__contraseña, obj_usuario.__rol)
                affected = cursor.execute(query, vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
        except Exception as e:
            return str(e)
        finally:
            conexion.close()

    def obtener_usuarios(self):
        conexion = Database()
        usuarios = []
        try:
            with conexion.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT id, nombre, contraseña, rol FROM usuarios")
                usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            return str(e)
        finally:
            conexion.close()