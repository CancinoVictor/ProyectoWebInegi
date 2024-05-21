from .Database import Database
import plotly.graph_objs as go

class Reporte:
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

    def generar_grafico_poblacion_municipio(self):
        datos = self.obtener_poblacion_por_municipio()
        if datos:
            municipios = [registro[0] for registro in datos]
            poblaciones = [registro[1] for registro in datos]

            # Crear el gráfico de barras
            grafico = go.Bar(x=municipios, y=poblaciones)

            # Configurar el diseño del gráfico
            layout = go.Layout(title='Población por Municipio',
                               xaxis=dict(title='Municipio'),
                               yaxis=dict(title='Población'))

            # Crear la figura
            figura = go.Figure(data=[grafico], layout=layout)

            return figura.to_html(full_html=False, include_plotlyjs='cdn')
        else:
            return None

    def generar_grafico_poblacion_localidad(self):
        datos = self.obtener_poblacion_por_localidad()
        if datos:
            localidades = [registro[0] for registro in datos]
            poblaciones = [registro[1] for registro in datos]

            # Crear el gráfico de barras
            grafico = go.Bar(x=localidades, y=poblaciones)

            # Configurar el diseño del gráfico
            layout = go.Layout(title='Población por Localidad',
                               xaxis=dict(title='Localidad'),
                               yaxis=dict(title='Población'))

            # Crear la figura
            figura = go.Figure(data=[grafico], layout=layout)

            return figura.to_html(full_html=False, include_plotlyjs='cdn')
        else:
            return None
