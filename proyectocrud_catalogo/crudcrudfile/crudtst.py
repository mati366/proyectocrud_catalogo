import os
from datetime import datetime
import pyfiglet

os.system('cls')

catalogo = [ ]

ventas = [ ]

# Nombre del productos
productos = 'CatalogoAviones.txt'
archivo_ventas = 'ventas_prod.txt'

def leer_datos_productos(productos):
    lista_datos = []
    with open(productos, 'r') as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')
            lista_datos.append(int(datos[0]))   # ID
            lista_datos.append(datos[1])        # Modelo
            lista_datos.append(datos[2])        # Marca
            lista_datos.append(int(datos[3]))   # Año
            lista_datos.append(datos[4])        # Consumo
            lista_datos.append(int(datos[5]))   # Unidades
            lista_datos.append(int(datos[6]))   # Horas de vuelo
            lista_datos.append(int(datos[7]))   # Precio
    return lista_datos

def leer_datos_ventas(archivo_ventas):
    lista_ventas = []
    with open(archivo_ventas, 'r') as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')
            lista_ventas.append([int(datos[0]), datos[1], int(datos[2]), int(datos[3])])
    return lista_ventas

def buscar(id):
    lista_datos = []
    with open(productos, 'r') as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')
            if int(datos[0]) == id:
                return {
                    'ID': int(datos[0]),
                    'Modelo': datos[1],
                    'Marca': datos[2],
                    'Año': int(datos[3]),
                    'Consumo': datos[4],
                    'Unidades': int(datos[5]),
                    'Horas de vuelo': int(datos[6]),
                    'Precio': int(datos[7])
                }
    return -1

def eliminar(id):
    lista_datos_actualizada = []
    existe = buscar(id)
    if existe != -1:
        with open(productos, 'r') as file:
            for linea in file:
                linea = linea.strip()
                datos = linea.split(',')
                if int(datos[0]) != id:
                    lista_datos_actualizada.append(linea)
        ultima_linea = len(lista_datos_actualizada)
        with open(productos, 'w') as file:
            c = 1
            for linea in lista_datos_actualizada:
                if c != ultima_linea:
                    file.write(linea + '\n')
                else:
                    file.write(linea)
                c += 1
        return 1
    else:
        return -1

def imprimir_datos(lista_datos):
    campos_por_avion = 8
    for i in range(0, len(lista_datos), campos_por_avion):
        print(f'ID: {lista_datos[i]}, Modelo: {lista_datos[i+1]}, Marca: {lista_datos[i+2]}, Año: {lista_datos[i+3]}, Consumo: {lista_datos[i+4]}, unidades: {lista_datos[i+5]}, Horas de vuelo: {lista_datos[i+6]}, Precio: {lista_datos[i+7]}')

def agregar_datos(id, modelo, marca, año, consumo, unidades, horas_totales, precio):
    producto = f"{id},{modelo},{marca},{año},{consumo},{unidades},{horas_totales},{precio}\n"
    with open(productos, 'a') as file:
        file.write(producto)

def modificar(id_a_modificar, nuevo_modelo, nueva_marca, nuevo_año, nuevo_consumo, nueva_unidad, nueva_horas_totales, nuevo_precio):
    lista_datos_actualizada = []
    id_encontrado = False
    with open(productos, 'r') as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')
            if int(datos[0]) == id_a_modificar:
                datos[1] = nuevo_modelo
                datos[2] = nueva_marca
                datos[3] = nuevo_año
                datos[4] = nuevo_consumo
                datos[5] = nueva_unidad
                datos[6] = nueva_horas_totales
                datos[7] = nuevo_precio
                id_encontrado = True
            lista_datos_actualizada.append(','.join(map(str, datos)))
    if not id_encontrado:
        return -1
    with open(productos, 'w') as file:
        file.write('\n'.join(lista_datos_actualizada) + '\n')
    return 1

def cargar_datos():
    catalogo = leer_datos_productos(productos)
    ventas = leer_datos_ventas(archivo_ventas)
    print('Datos cargados correctamente!')
    return catalogo, ventas

def respaldar_datos():
    with open(productos, 'w') as file:
        for i in range(0, len(catalogo), 8):
            file.write(f'{catalogo[i]},{catalogo[i+1]},{catalogo[i+2]},{catalogo[i+3]},{catalogo[i+4]},{catalogo[i+5]},{catalogo[i+6]},{catalogo[i+7]}\n')
    with open(archivo_ventas, 'w') as file:
        for venta in ventas:
            file.write(f'{venta[0]},{venta[1]},{venta[2]},{venta[3]}\n')
    print('Datos respaldados correctamente!')

def buscar_venta(fecha):
    lista_ventas = leer_datos_ventas(archivo_ventas)
    for v in lista_ventas:
        if v[1] == fecha:
            return f"Los datos de la venta son: Folio: {v[0]}, Fecha: {v[1]} , ID Producto: {v[2]}, Total: ${v[3]}"
    return "Venta no encontrada, ingrese una fecha valida"

def imprimir_ventas(lista_ventas):
    for v in lista_ventas:
        print(f"Folio: {v[0]}, Fecha: {v[1]}, ID Producto: {v[2]}, Total: ${v[3]}")

def agregar_venta(fecha, id_producto, total):
    global folio
    # Generar nuevo folio basado en el último folio existente
    if len(ventas) == 0:
        folio = 1
    else:
        folio = ventas[-1][0] + 1
    with open(archivo_ventas, 'a') as file:
        file.write(f"\n{folio},{fecha},{id_producto},{total}")
    # Actualizar la lista de ventas global
    ventas.append([folio, fecha, id_producto, total])

def eliminar_venta(venta):
    lista_ventas_actualizada = []
    existe = buscar_venta(ventas)
    if existe != -1:
        lista_ventas = leer_datos_ventas(archivo_ventas)
        for v in lista_ventas:
            if v[0] != venta:
                lista_ventas_actualizada.append(v)
        with open(archivo_ventas, 'w') as file:
            for v in lista_ventas_actualizada:
                file.write(f"{v[0]},{v[1]},{v[2]},{v[3]}\n")
        return 1
    else:
        return -1
#funcion fechas 
def validar_fecha(fechas):
    partes = fechas.split('-')
    if len(partes) != 3:
        return False
    
    dia, mes, año = partes
    
    if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
        return False
    
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    
    if dia < 1 or dia > 31:
        return False
    if mes < 1 or mes > 12:
        return False
    if año <= 2000:
        return False
    
    return True

def validar_datos(catalogo):
    while True:
        try:
            id = int(input('Ingrese el id del avion (4 caracteres): '))
        except ValueError:
            print("Error, el ID deben ser caracteres numéricos")
            continue
        if len(str(id)) != 4:
            print('Error, el ID debe tener 4 caracteres numéricos.')
            continue
        if any(productos[0] == id for producto in catalogo):
            print('Error, el ID ingresado ya existe en el catálogo.')
            continue
        modelo = input('Ingrese el modelo del avion: ')
        if not modelo:
            print('Error, el modelo no puede estar vacío.')
            continue
        marca = input('Ingrese la marca del avion: ')
        if not marca:
            print('Error, la marca no puede estar vacía.')
            continue
        try:
            año = int(input('Ingrese el año del avion: '))
        except ValueError:
            print('Error, el año debe ser numérico.')
            continue
        consumo = input('Ingrese el consumo del avion (xx lt/hr): ')
        if not consumo:
            print('Error, el consumo no puede estar vacío.')
            continue
        try:
            unidades = int(input('Ingrese las unidades que existen del avion (>= 0): '))
            if unidades < 0:
                print('Error, las unidades deben ser mayor o igual a 0.')
                continue
        except ValueError:
            print('Error, las unidades deben ser un número entero.')
            continue
        try:
            horas_totales = int(input('Ingrese las horas totales del avion: '))
        except ValueError:
            print('Error, las horas totales deben ser un número entero.')
            continue
        try:
            precio = int(input('Ingrese el precio del avion: '))
            if precio < 0:
                print('Error, el precio debe ser mayor o igual a 0.')
                continue
        except ValueError:
            print('Error, el precio debe ser un número entero.')
            continue
        return id, modelo, marca, año, consumo, unidades, horas_totales, precio

def menu_vender():
    while True:
        if len(catalogo) == 0:
            print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
            os.system('pause')
            break
        else:
            print(pyfiglet.figlet_format("vender aeronaves \n"))
            print('catalogo de aeronaves:')
            lista_datos = leer_datos_productos(productos)
            imprimir_datos(lista_datos)
            try:
                id = int(input('Ingrese el ID del avion a comprar: '))
            except ValueError:
                os.system("cls")
                print('Error, ingrese un ID valido (solo numeros)')
                os.system('pause')
                os.system("cls")
                continue
            lista = buscar(id)
            if lista == -1:
                os.system("cls")
                print('Error, ID no valido, por favor, seleccione un ID existente')
                os.system('pause')
                os.system("cls")
                continue
            else:
                print('\nCaracteristicas del avion a comprar:\n')
                print(f'''Modelo: {lista['Modelo']} ; Marca: {lista['Marca']} ; Año: {lista['Año']} ; Consumo: {lista['Consumo']} ; Unidades: {lista['Unidades']} ; Horas Totales: {lista['Horas de vuelo']} ; Precio: ${lista['Precio']}''')
                try:
                    cantidad_comprar = int(input('¿Cuantas unidades desea comprar?: '))
                except ValueError:
                    print('Error, ingrese una cantidad valida')
                    continue
                if cantidad_comprar > lista['Unidades']:
                    os.system('cls')
                    decision = input('Stock no valido, desea volver a intentarlo? (si/no): ')
                    if decision.lower() == 'si':
                        continue
                    elif decision.lower() == 'no':
                        os.system('cls')
                        break
                elif cantidad_comprar <= lista['Unidades']:
                    total_compra = cantidad_comprar * lista['Precio']
                    decision = input(f"\n¿Desea confirmar la compra de {cantidad_comprar} unidades de un {lista['Marca']} {lista['Modelo']} por un total de ${total_compra}? (si/no): ")
                    if decision.lower() == 'si':
                        lista['Unidades'] -= cantidad_comprar
                        fecha = datetime.now().strftime('%d-%m-%Y')
                        agregar_venta(fecha, id, total_compra)
                        modificar(id, lista['Modelo'], lista['Marca'], lista['Año'], lista['Consumo'], lista['Unidades'], lista['Horas de vuelo'], lista['Precio'])
                        os.system('cls')
                        print(f'La compra de {cantidad_comprar} {lista["Marca"]} {lista["Modelo"]} por ${total_compra} se ha completado y ha sido registrada.')
                        if lista['Unidades'] <= 0:
                            eliminar(id)
                        decision = input('¿Desea comprar otro producto? (si/no): ')
                        if decision.lower() == 'si':
                            continue
                        elif decision.lower() == 'no':
                            os.system('cls')
                            break
                    elif decision.lower() == 'no':
                        os.system('cls')
                        decision = input('compra cancelada, desea volver a intentarlo? (si/no): ')
                        if decision.lower() == 'si':
                            continue
                        elif decision.lower() == 'no':
                            os.system('cls')
                            break


fecha = datetime.now().strftime('%d-%m-%Y')



opcion = 0
while opcion != 5:
    try:
        os.system('cls')
        sw = 0
        print(pyfiglet.figlet_format("catalogo de aviones"))
        print(f'''
            fecha: {fecha}
            version: v002
            sistema de ventas
            -------------------
            1. Vender productos
            2. Reportes
            3. Mantenedores
            4. Administración
            5. Salir
            ''')
        opcion = int(input('Ingrese una opcion entre 1-5: '))
        match opcion:
            case 1: #VENTA DE PRODUCTOS
                menu_vender()

            case 2: # REPORTES
                while True:
                    os.system("cls")
                    print(pyfiglet.figlet_format("reportes"))
                    print('''
                    1. general de ventas
                    2. ventas por fecha especifica
                    3. ventas por rango de fechas
                    4. salir al menu principal
                    ''')
                    op = int(input('Ingrese una opción entre 1-4: '))
                    if op == 1:
                        os.system("cls")
                        if len(ventas) == 0:
                            print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                        else:
                            imprimir_ventas(ventas)
                        os.system('pause')

                    elif op == 2:
                        os.system("cls")
                        if len(ventas) == 0:
                            print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                        else:
                            while True:
                                fecha = input('Ingrese la fecha (dd-mm-yyyy): ')
                                # Validar formatos incorrectos
                                if "/" in fecha or len(fecha) != 10:
                                    os.system("cls")
                                    print("Error, debe ingresar la fecha con este formato (dd-mm-yyyy)")
                                    continue
                                # Validar el formato correcto de la fecha
                                else:
                                    os.system("cls")
                                    leer_datos_ventas(archivo_ventas)
                                    venta_busqueda = buscar_venta(fecha)
                                    print(venta_busqueda)
                                    os.system("pause")
                                    break
                    elif op == 3:
                        os.system("cls")
                        if len(catalogo) == 0:
                            print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                        else:
                            fecha_inicio = input('Ingrese la fecha de inicio (dd-mm-yyyy): ')
                            fecha_fin = input('Ingrese la fecha de fin (dd-mm-yyyy): ')
                            ventas_rango = [venta for venta in ventas if fecha_inicio <= venta[1] <= fecha_fin]
                            if ventas_rango:
                                imprimir_ventas(ventas_rango)
                            else:
                                print('No se encontraron ventas en el rango de fechas especificado.')
                            os.system('pause')

                    elif op == 4:
                        break
                    else:
                        print('Opción incorrecta.')
                        os.system('pause')

            case 3: #MANTENEDORES
                opc = 0
                while opc < 6:
                    os.system('cls')
                    print(pyfiglet.figlet_format("mantenedores"))
                    print('''
                            ------------
                            1. agregar
                            2. buscar por id
                            3. eliminar por id
                            4. modificar
                            5. listar 
                            6. salir
                        ''')
                    opc = int(input('Ingrese una opcion entre 1-6: '))
                    if opc >= 1 and opc <= 6:
                        match opc:
                            case 1: #AGREGAR PRODUCTOS
                                os.system("cls")
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print(pyfiglet.figlet_format("Agregar Producto"))
                                    id, modelo, marca, año, consumo, unidades, horas_totales, precio = validar_datos(catalogo)
                                    agregar_datos(id, modelo, marca, año, consumo, unidades, horas_totales, precio)
                                    print('\nDatos agregados con éxito!')
                            case 2: # BUSCAR PRODUCTO
                                os.system("cls")
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print(pyfiglet.figlet_format("Buscar Producto"))
                                    id = int(input('Ingrese el id del avion que desea buscar: '))
                                    lista = buscar(id)
                                    if lista != -1:
                                        print(f'''Modelo: {lista['Modelo']} ; Marca: {lista['Marca']} ; Año: {lista['Año']} ; Consumo: {lista['Consumo']} ; Unidades: {lista['Unidades']} ; Horas Totales: {lista['Horas de vuelo']} ; Precio: ${lista['Precio']}''')
                                    else:
                                        print('No se encontró el producto')
                            case 3: # ELIMINAR PRODUCTO
                                os.system("cls")
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print(pyfiglet.figlet_format("Eliminar Producto"))
                                    id = int(input('Ingrese un ID a eliminar: '))
                                    lista = eliminar(id)
                                    if lista != -1:
                                        print('Avion eliminado!')
                                    else:
                                        print('No se encontró el producto')
                            case 4: #MODIFICAR SEGUN ID INGRESADA
                                os.system("cls")
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print(pyfiglet.figlet_format("Modificar Producto"))
                                    id_a_modificar = int(input('Ingrese un id para buscar: '))
                                    lista = buscar(id_a_modificar)
                                    if lista != -1:
                                        print('ID encontrado!')
                                        print(f'''Modelo: {lista['Modelo']} ; Marca: {lista['Marca']} ; Año: {lista['Año']} ; Consumo: {lista['Consumo']} ; Unidades: {lista['Unidades']} ; Horas Totales: {lista['Horas de vuelo']} ; Precio: ${lista['Precio']}''')
                                        print('\n')
                                        
                                        id_validado, nuevo_modelo, nueva_marca, nuevo_año, nuevo_consumo, nueva_unidad, nueva_horas_totales, nuevo_precio = validar_datos(catalogo)
                                        modificar(id_a_modificar, nuevo_modelo, nueva_marca, nuevo_año, nuevo_consumo, nueva_unidad, nueva_horas_totales, nuevo_precio)
                                        
                                        print('\nNuevos datos actualizados con éxito!')
                                    else:
                                        print('Error, ID no existe')
                            case 5: #LISTAR LOS PRODUCTOS EXISTENTES
                                os.system("cls")
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print(pyfiglet.figlet_format("Lista de Productos"))
                                    lista_aviones = leer_datos_productos(productos)
                                    imprimir_datos(lista_aviones)
                    if opc == 6:
                        break
                    os.system('pause')

            case 4: # ADMINISTRACIÓN
                os.system('cls')
                op = 0
                while op != 4:
                    print(pyfiglet.figlet_format("administracion"))
                    print('''
                       
                        ----------------
                        1. Cargar datos
                        2. Respaldar datos
                        3. Revisar datos actuales
                        4. Salir
                        ''')
                    op = int(input('Ingrese una opción: '))
                    if op == 1:
                        catalogo, ventas = cargar_datos()
                        os.system('pause')
                        os.system('cls')
                        break
                    elif op == 2:
                        respaldar_datos()
                        os.system('pause')
                        os.system('cls')
                        break
                    elif op == 3:
                        if len(catalogo) > 0 and len(ventas) > 0:
                            os.system('cls')
                            print("Datos actualmente cargados con exito")
                            os.system("pause")
                            os.system('cls')
                            break
                        else:
                            os.system('cls')
                            print("Datos no cargados correctamente, por favor, cargue los datos para trabajar con estos.")
                            os.system("pause")
                            os.system('cls')
                            continue
                    elif op == 4:
                        break
                    else:
                        print('Opción incorrecta.')
                        os.system('pause')
            case 5: #SALIDA DEL SISTEMA
                print('Saliendo del sistema...')
                break
    except ValueError:
        print('Error, Ingrese solo numeros')
        os.system('pause')
