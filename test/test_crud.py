import modelo.package_model.Users as Users

# Crear una instancia de la clase Usuario
obj_usuario = Users.Usuario()

# Obtener todos los usuarios
lista_usuarios = obj_usuario.obtener_usuarios()

# Verificar si se encontraron usuarios
if lista_usuarios != None:
    for usuario in lista_usuarios:
        print(usuario)
else:
    print("No se encontraron datos de usuarios")

# Obtener un usuario por su ID (en este caso, ID 1)
usuario_id_4 = obj_usuario.obtener_usuario_por_id(1)

# Verificar si se encontró el usuario
if usuario_id_4 != None:
    print(usuario_id_4[0], usuario_id_4[1], usuario_id_4[2], usuario_id_4[3])
else:
    print("No se encontró ningún usuario con el ID especificado")


#insertar
# obj_curso=Curso.Curso("","PLASTILINA 1","djdjd")
# result_ins=obj_curso.insertar_cursos(obj_curso)
# if result_ins=="1":
#      print("El curso fue registrado con éxito")
# else:
#      print("No se pudo registrar el curso")

 
#update
# obj_curso_upd=Curso.Curso(1,"python 5","2024-03-11")
# result_upd=obj_curso.update_cursos(obj_curso_upd)
# if result_upd=="1":
#      print("El curso fue actualizado con éxito")
# else:
#      print("No se pudo actualzar el curso")

 
#eliminar    
#borra_cursos_id = obj_curso.eliminar_curso(69)
#if borra_cursos_id==1:
#    print("El curso fue eliminado con éxito")
#else:
#    print("No se pudo eliminar el curso")