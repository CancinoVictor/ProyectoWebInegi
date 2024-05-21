from .Database import Database
class HabitantesXVivienda:
    def __init__(self):
        # Crear una instancia de la clase Database
        self.db = Database()

    def obtener_resumen_habitantes_por_vivienda(self):
        query = """
            SELECT 
                v.ID_VIVIENDA,
                m.MATERIAL, 
                l.LOCALIDAD, 
                COUNT(h.INE) AS num_habitantes, 
                GROUP_CONCAT(h.NOMBRE, ' ', h.APELLIDO SEPARATOR ', ') AS habitantes
            FROM 
                vivienda v
            LEFT JOIN 
                material m ON v.ID_MATERIAL = m.ID_MATERIAL
            LEFT JOIN 
                localidad l ON v.ID_LOCALIDAD = l.ID_LOCALIDAD
            LEFT JOIN 
                habitantes h ON v.ID_VIVIENDA = h.ID_VIVIENDA
            GROUP BY 
                v.ID_VIVIENDA
        """
        result = self.db.fetch_data(query)
        return result
