from flask import Flask, render_template, request, redirect, url_for, session
from modelo.package_model.Usuario import Usuario
from modelo.package_model.Registro_base import RegistroBase
from modelo.package_model.habitantesXvivienda import HabitantesXVivienda
from modelo.package_model.habitanteXmaterial import HabitanteXMaterial
from modelo.package_model.viviendaXsustento import ViviendaXSustento
from modelo.package_model.dashboard import Dashboard
from modelo.package_model.reporte import Reporte
from modelo.package_model.catalago import Catalogo  
from modelo.package_model.crud import CRUD  
from modelo.package_model.decorator import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

# No necesitas instanciar RegistroBase aquí

@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['username']
        contraseña = request.form['password']
        
        usuario = Usuario()
        usuarios = usuario.obtener_usuarios()
        
        for u in usuarios:
            if u['nombre'] == nombre and u['contraseña'] == contraseña:
                session['usuario'] = {'id': u['id'], 'nombre': u['nombre'], 'rol': u['rol']}
                if u['rol'] == 'admin':
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('cliente'))
        
        return 'Credenciales incorrectas, <a href="/">intenta de nuevo</a>.'
    return render_template('index.html')

@app.route('/admin')
@login_required(role='admin')
def admin():
    return render_template('admin.html', usuario=session['usuario'])


@app.route('/home')
@login_required(role='cliente')
def cliente():
    return render_template('home.html', usuario=session['usuario'])


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/datos', methods=['POST'])
def insertar_datos():
    if request.method == 'POST':
        municipio = request.form['municipio']
        localidad = request.form['localidad']
        material = request.form['material']
        pisos = request.form['pisos']
        ine = request.form['ine']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        sustento = request.form['sustento']
        
        # Crear un objeto RegistroBase con los datos del formulario
        registro_base = RegistroBase(municipio, localidad, material, pisos, ine, nombre, apellido, telefono, sustento)
        
        # Insertar datos utilizando los métodos de la clase RegistroBase
        registro_base.insertar_datos()
        
        # Redireccionar a la página de inicio
        return redirect(url_for('index'))

@app.route('/habitantesXvivienda')
def habitantes_por_vivienda():
    # Obtener los datos de los habitantes por vivienda
    habitantes_vivienda = HabitantesXVivienda().obtener_resumen_habitantes_por_vivienda()
    return render_template('habitantesXvivienda.html', viviendas=habitantes_vivienda)

@app.route('/tipos_de_casas')
def tipos_de_casas():
    # Obtener los datos de los habitantes por material de vivienda
    habitantes_material = HabitanteXMaterial().obtener_resumen_habitantes_por_material()
    return render_template('habitanteXmaterial.html', habitantesXmaterial=habitantes_material)

@app.route('/viviendaXsustento')
def vivienda_por_sustento():
    viviendas_sustento = ViviendaXSustento().obtener_resumen_vivienda_por_sustento()
    return render_template('viviendaXsustento.html', viviendas_sustento=viviendas_sustento)


@app.route('/dashboard')
def dashboard():
    # Crear una instancia de la clase Dashboard
    dashboard_data = Dashboard()
    
    # Obtener la población por municipio y por localidad
    poblacion_municipio = dashboard_data.obtener_poblacion_por_municipio()
    poblacion_localidad = dashboard_data.obtener_poblacion_por_localidad()
    
    # Verificar si los datos no son None
    if poblacion_municipio is not None and poblacion_localidad is not None:
        # Renderizar la plantilla dashboard.html con los datos obtenidos
        return render_template('dashboard.html', poblacion_municipio=poblacion_municipio, poblacion_localidad=poblacion_localidad)
    else:
        # Si los datos son None, renderizar la plantilla sin datos
        return render_template('dashboard.html', poblacion_municipio=[], poblacion_localidad=[])

@app.route('/reportes')
def mostrar_reporte():
    # Crear una instancia de la clase Reporte
    reporte = Reporte()

    # Generar los gráficos utilizando la clase Reporte
    grafico_municipio = reporte.generar_grafico_poblacion_municipio()
    grafico_localidad = reporte.generar_grafico_poblacion_localidad()

    # Obtener otros datos necesarios para el reporte
    poblacion_municipio = reporte.obtener_poblacion_por_municipio()
    poblacion_localidad = reporte.obtener_poblacion_por_localidad()

    # Renderizar la plantilla HTML con los datos y los gráficos generados
    return render_template('reporte.html', poblacion_municipio=poblacion_municipio,
                           poblacion_localidad=poblacion_localidad,
                           grafico_municipio=grafico_municipio,
                           grafico_localidad=grafico_localidad)

@app.route('/catalogo')
def mostrar_catalogo():
    catalogo_data = Catalogo()
    datos_catalogo = catalogo_data.obtener_datos_catalogo()
    return render_template('catalogo.html', datos_catalogo=datos_catalogo)



# Ruta para mostrar el formulario CRUD
@app.route('/crud', methods=['GET'])
def mostrar_formulario_crud():
    usuarios = Usuario().obtener_usuarios()
    return render_template('crud.html', usuarios=usuarios)

# Ruta para manejar todas las operaciones CRUD
@app.route('/crud', methods=['POST'])
def crud():
    if request.method == 'POST':
        if 'crear' in request.form:
            nombre = request.form['nombre']
            contraseña = request.form['contraseña']
            rol = request.form['rol']
            nuevo_usuario = Usuario(nombre=nombre, contraseña=contraseña, rol=rol)
            nuevo_usuario.insertar_usuario(nuevo_usuario)
        elif 'editar' in request.form:
            id_usuario = request.form['id']
            nombre = request.form['nombre']
            contraseña = request.form['contraseña']
            rol = request.form['rol']
            usuario_editado = Usuario(id=id_usuario, nombre=nombre, contraseña=contraseña, rol=rol)
            usuario_editado.update_usuario(usuario_editado)
        elif 'eliminar' in request.form:
            id_usuario = request.form['id']
            Usuario().eliminar_usuario(id_usuario)
    return redirect(url_for('mostrar_formulario_crud'))


if __name__ == "__main__":
    app.run(debug=True)
