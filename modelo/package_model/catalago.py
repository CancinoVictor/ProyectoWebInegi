from .Database import Database

class Catalogo:
    def __init__(self):
        # Crear una instancia de la clase Database
        self.db = Database()

    def obtener_datos_catalogo(self):
        query = """
            SELECT 
                *
            FROM 
                catalogo;
        """
        try:
            result = self.db.fetch_data(query)
            return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
