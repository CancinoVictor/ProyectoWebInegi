from .Database import Database

class RegistroBase:
    def __init__(self, municipio, localidad, material, pisos, ine, nombre, apellido, telefono, sustento):
        self.municipio = municipio
        self.localidad = localidad
        self.material = material
        self.pisos = pisos
        self.ine = ine
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.sustento = sustento
        self.db = Database()

    def insertar_datos(self):
        conn = self.db.conn
        cursor = self.db.cursor

        try:
            cursor.execute("INSERT INTO municipio (MUNICIPIO) VALUES (%s)", (self.municipio,))
            municipio_id = cursor.lastrowid

            cursor.execute("INSERT INTO localidad (ID_MUNICIPIO, LOCALIDAD) VALUES (%s, %s)", (municipio_id, self.localidad))
            localidad_id = cursor.lastrowid

            cursor.execute("INSERT INTO material (MATERIAL) VALUES (%s)", (self.material,))
            material_id = cursor.lastrowid

            cursor.execute("INSERT INTO vivienda (ID_MATERIAL, ID_LOCALIDAD, ATTRIBUTE_PISOS) VALUES (%s, %s, %s)", (material_id, localidad_id, self.pisos))
            vivienda_id = cursor.lastrowid

            cursor.execute("INSERT INTO habitantes (INE, ID_VIVIENDA, NOMBRE, APELLIDO, TELEFONO) VALUES (%s, %s, %s, %s, %s)",
                           (self.ine, vivienda_id, self.nombre, self.apellido, self.telefono))

            cursor.execute("INSERT INTO sustento (ID_VIVIENDA, SUSTENTO) VALUES (%s, %s)", (vivienda_id, self.sustento))

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            pass

       