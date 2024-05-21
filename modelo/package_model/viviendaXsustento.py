from .Database import Database

class ViviendaXSustento:
    def __init__(self):
        self.db = Database()

    def obtener_resumen_vivienda_por_sustento(self):
        query = """
         SELECT 
        v.ID_VIVIENDA,
        MAX(s.SUSTENTO) AS SUSTENTO, 
        GROUP_CONCAT(h.NOMBRE, ' ', h.APELLIDO SEPARATOR ', ') AS habitantes
        FROM 
        vivienda v
        LEFT JOIN 
        sustento s ON v.ID_VIVIENDA = s.ID_VIVIENDA
        LEFT JOIN 
        habitantes h ON v.ID_VIVIENDA = h.ID_VIVIENDA
        GROUP BY 
        v.ID_VIVIENDA;
        """
        try:
            result = self.db.fetch_data(query)
            return result if result else []  # Retorna una lista vacía si el resultado es None
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []
