from .Database import Database

class HabitanteXMaterial:
    def __init__(self):
        self.db = Database()

    def obtener_resumen_habitantes_por_material(self):
        query = """
            SELECT 
                m.MATERIAL,
                v.ID_VIVIENDA,
                COUNT(h.INE) AS num_habitantes
            FROM 
                vivienda v
            LEFT JOIN 
                material m ON v.ID_MATERIAL = m.ID_MATERIAL
            LEFT JOIN 
                habitantes h ON v.ID_VIVIENDA = h.ID_VIVIENDA
            GROUP BY 
                m.MATERIAL, v.ID_VIVIENDA
        """
        try:
            result = self.db.fetch_data(query)
            return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
