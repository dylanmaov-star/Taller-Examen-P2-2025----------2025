baseUsuarios = []

#Usuario CRUD

def crearUsuario():

    id = input("Ingrese su ID de usuario: ")
    if obtenerId(id) != -1:
        print("Ya hay un usuario con este ID")
        return
    nombre = input("Digite su nombre: ")
    contacto = input("Digite su contacto: ")
    rol = input("Ingrese rol: ")
    tareas = [] 
    usuario = (id, nombre, contacto, rol, tareas)
    baseUsuarios.append(usuario)
    print("Usuario creado correctamente.")

def listarUsuarios():

    if baseUsuarios == []:
        print("No hay usuarios registrados")
        return
    print("\nLista de usuarios:")
    for usu in baseUsuarios:
        print(f"ID: {usu[0]}, Nombre: {usu[1]}, Contacto: {usu[2]}, Rol: {usu[3]}")

def obtenerId(id):
    i = 0
    while i < len(baseUsuarios):
        if baseUsuarios[i][0] == id:
            return i
        i+=1
    return -1 

def verUsuario():

    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    usu = baseUsuarios[idx]
    print("Usuario encontrado")
    print(f"ID: {usu[0]}, \nNombre: {usu[1]}, \nContacto: {usu[2]}, \nRol: {usu[3]}")
    if usu[4] == []:
        print("No tiene tareas asiganadas")
    else:
        print(f"Tiene {len(usu[4])} tareas asignadas")


def actualizarUsuario():

    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    usu = baseUsuarios[idx]
    print("Deja en blanco si no quieres cambiar el campo")

    nuevoNombre = input(f"Nombre actual ({usu[1]}): ")
    nuevoContacto = input(f"Contacto actual ({usu[2]}): ")
    nuevoRol = input(f"Rol actual ({usu[3]}): ")

    if nuevoNombre == "":
        nuevoNombre = usu[1]
    if nuevoContacto == "":
        nuevoContacto = usu[2]
    if nuevoRol == "":
        nuevoRol = usu[3]

    tareas = usu[4][:]
    usuarioNuevo = (usu[0], nuevoNombre, nuevoContacto, nuevoRol, tareas)
    baseUsuarios[idx] = usuarioNuevo
    print("Usuario actualizado correctamente")

def eliminarUsuario():
    
    id = input("Ingrese ID del usuario a eliminar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado.")
        return
    baseUsuarios.pop(idx)
    print("Usuario eliminado")


#Tareas CRUD

def agregarTarea():

    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado, no es posible agregar una tarea")
        return 
    codigo = input("Codigo de la tarea: ")
    titulo = input("Titulo de la tarea: ")
    detalle = input("Descripcion: ")
    estado = input("Estado (pendiente/completada): ")
    if estado != "pendiente" and estado != "completada":
        print("Estado no valido; se guardar como 'pendiente'")
        estado = "pendiente"
    tarea = {"codigo": codigo, "titulo": titulo, "estado": estado, "detalle": detalle}

    usuario = baseUsuarios[idx]
    tareasCopiadas = usuario[4][:]
    tareasCopiadas.append(tarea)
    usuarioNuevo = (usuario[0], usuario[1], usuario[2], usuario[3], tareasCopiadas)
    baseUsuarios[idx] = usuarioNuevo
    print("Tarea agregada al usuario")

def listarTareas():
    
    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    usuario = baseUsuarios[idx]
    tareas = usuario[4]
    if tareas == []:
        print("El usuario no tiene tareas")
        return
    print(f"Tareas de {usuario[1]}:")
    i = 0
    while i < len(tareas):
        tare = tareas[i]
        print(f"- Codigo: {tare['codigo']}, Titulo: {tare['titulo']}, Estado: {tare['estado']}")
        i += 1

def listarTareas_estado():
    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    buscarEstado = input("Ingrese el estado para buscar la tarea(pendiente/completada): ")
    if buscarEstado != "pendiente" and buscarEstado != "completada":
        print("Estado no valido")
        return
    usuario = baseUsuarios[idx]
    tareas = usuario[4]
    contador = 0
    i = 0
    while i < len(tareas):
        t = tareas[i]
        if t["estado"] == buscarEstado:
            print(f"- {t['codigo']}: {t['titulo']} ({t['estado']})")
            contador += 1
        i += 1
    if contador == 0:
        print("No se encontraron tareas con ese estado para el usuario")

def buscarTarea():
    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    codigoTarea = input("Ingrese el codigo de la tarea que desea buscar: ")
    usuario = baseUsuarios[idx]
    tareas = usuario[4]
    i = 0
    while i < len(tareas):
        if tareas[i]["codigo"] == codigoTarea:
            t = tareas[i]
            print("Tarea encontrada: ")
            print(f"Codigo: {t['codigo']}\nTitulo: {t['titulo']}\nEstado: {t['estado']}\nDetalle: {t['detalle']}")
            return
        i += 1
    print("Tarea no encontrada para ese usuario.")

def actualizarTarea():
    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    codigoTarea = input("Ingrese el codigo de la tarea que desea actualizar")
    usuario = baseUsuarios[idx]
    tareas = usuario[4][:]
    i = 0
    while i < len(tareas):
        if tareas[i]["codigo"] == codigoTarea:
            print("Dejar en blanco para no cambiar el campo.")
            nuevoTitulo = input(f"Titulo actual ({tareas[i]['titulo']}): ")
            nuevoDetalle = input(f"Detalle actual ({tareas[i]['detalle']}): ")
            nuevoEstado = input(f"Estado actual ({tareas[i]['estado']}): ")

            if nuevoTitulo != "":
                tareas[i]["titulo"] = nuevoTitulo
            if nuevoDetalle != "":
                tareas[i]["detalle"] = nuevoDetalle
            if nuevoEstado == "pendiente" or nuevoEstado == "completada":
                tareas[i]["estado"] = nuevoEstado

           
            usuarioNuevo = (usuario[0], usuario[1], usuario[2], usuario[3], tareas)
            baseUsuarios[idx] = usuarioNuevo
            print("Tarea actualizada")
            return
        i += 1
    print("No se encontro la tarea")

def eliminarTarea():
    id = input("Ingrese el ID  a buscar: ")
    idx = obtenerId(id)
    if idx == -1:
        print("Usuario no encontrado")
        return 
    codigoTarea = input("Ingrese el codigo de la tarea que desea borrar")
    usuario = baseUsuarios[idx]
    tareas = usuario[4][:]
    i = 0
    while i < len(tareas):
        if tareas[i]["codigo"] == codigoTarea:
            tareas.pop(i)
            usuarioNuevo = (usuario[0], usuario[1], usuario[2], usuario[3], tareas)
            baseUsuarios[idx] = usuarioNuevo
            print("Tarea eliminada")
            return
        i += 1
    print("No se encontró la tarea indicada")

def reporteTareas_porUsuario():
        if baseUsuarios == []:
           print("No hay usuarios")
           return

        for u in baseUsuarios:
            print("\n--------------------------------")
            print(f"Usuario {u[1]} (ID: {u[0]}) - Rol: {u[3]}")
            tareas = u[4]
            if tareas == []:
                print("  No tiene tareas")
                continue

            pendientes = 0
            completadas = 0
            i = 0
            while i < len(tareas):
                t = tareas[i]
                print(f"  - {t['codigo']}: {t['titulo']} ({t['estado']})")
                if t['estado'] == "pendiente":
                    pendientes += 1
                elif t['estado'] == "completada":
                    completadas += 1
            i += 1
            print(f"  Totales -> Pendientes: {pendientes}, Completadas: {completadas}")


#Menus

def menu_usuarios():
    while True:
        print("\n--- MENÚ USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Ver usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crearUsuario()
        elif opcion == "2":
            listarUsuarios()
        elif opcion == "3":
            verUsuario()
        elif opcion == "4":
            actualizarUsuario()
        elif opcion == "5":
            eliminarUsuario()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def menu_tareas():
    while True:
        print("\n--- MENÚ TAREAS ---")
        print("1. Agregar tarea a usuario")
        print("2. Listar tareas de un usuario")
        print("3. Listar tareas por estado")
        print("4. Buscar tarea de un usuario")
        print("5. Actualizar tarea")
        print("6. Eliminar tarea")
        print("7. Reporte: tareas por usuario")
        print("8. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            agregarTarea()
        elif opcion == "2":
            listarTareas()
        elif opcion == "3":
            listarTareas_estado()
        elif opcion == "4":
            buscarTarea()
        elif opcion == "5":
            actualizarTarea()
        elif opcion == "6":
            eliminarTarea()
        elif opcion == "7":
            reporteTareas_porUsuario()
        elif opcion == "8":
            break
        else:
            print("Opcion invalida.")

def menu_principal():
    while True:
        print("\n-- SISTEMA CONTROL DE TAREAS --")
        print("1. Menu Usuarios")
        print("2. Menu Tareas")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_tareas()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion inválida.")

menu_principal()
