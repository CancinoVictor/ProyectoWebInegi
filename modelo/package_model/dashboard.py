from .Database import Database

class Dashboard:
    def __init__(self):
        # Crear una instancia de la clase Database
        self.db = Database()

    def obtener_poblacion_por_municipio(self):
        query = """
            SELECT 
                m.MUNICIPIO AS municipio, 
                COUNT(h.INE) AS poblacion_municipio
            FROM 
                municipio m
            LEFT JOIN 
                localidad l ON m.ID_MUNICIPIO = l.ID_MUNICIPIO
            LEFT JOIN 
                vivienda v ON l.ID_LOCALIDAD = v.ID_LOCALIDAD
            LEFT JOIN 
                habitantes h ON v.ID_VIVIENDA = h.ID_VIVIENDA
            GROUP BY 
                m.MUNICIPIO;
        """
        try:
            result = self.db.fetch_data(query)
            return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def obtener_poblacion_por_localidad(self):
        query = """
            SELECT 
                l.LOCALIDAD AS localidad, 
                COUNT(h.INE) AS poblacion_localidad
            FROM 
                localidad l
            LEFT JOIN 
                vivienda v ON l.ID_LOCALIDAD = v.ID_LOCALIDAD
            LEFT JOIN 
                habitantes h ON v.ID_VIVIENDA = h.ID_VIVIENDA
            GROUP BY 
                l.LOCALIDAD;
        """
        try:
            result = self.db.fetch_data(query)
            return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
