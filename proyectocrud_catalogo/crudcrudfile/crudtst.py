import os
from datetime import datetime
import pyfiglet

os.system('cls')

# es un numero correlativo (folio=folio+1)
# Folio comienza desde folio=10000
catalogo = [ ]

#       folio,  fecha id,cantidad, total
# 20 Ventas
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
        print(f'ID: {lista_datos[i]}, Modelo: {lista_datos[i+1]}, Marca: {lista_datos[i+2]}, Año: {lista_datos[i+3]}, Consumo: {lista_datos[i+4]}, Cantidad de motores: {lista_datos[i+5]}, Horas de vuelo: {lista_datos[i+6]}, Precio: {lista_datos[i+7]}')

def agregar_datos(id, modelo, marca, año, consumo, unidades, horas_totales, precio):
    with open(productos, 'a') as file:
        file.write(f'\n{id},{modelo},{marca},{año},{consumo},{unidades},{horas_totales},{precio}')

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
    global catalogo, ventas
    catalogo = leer_datos_productos(productos)
    ventas = leer_datos_ventas(archivo_ventas)
    print('Datos cargados correctamente!')

def respaldar_datos():
    with open(productos, 'w') as file:
        for i in range(0, len(catalogo), 8):
            file.write(f'{catalogo[i]},{catalogo[i+1]},{catalogo[i+2]},{catalogo[i+3]},{catalogo[i+4]},{catalogo[i+5]},{catalogo[i+6]},{catalogo[i+7]}\n')
    with open(archivo_ventas, 'w') as file:
        for venta in ventas:
            file.write(f'{venta[0]},{venta[1]},{venta[2]},{venta[3]}\n')
    print('Datos respaldados correctamente!')

def buscar_venta(venta):
    lista_ventas = leer_datos_ventas(archivo_ventas)
    for v in lista_ventas:
        if v[0] == venta:
            return v
    return -1

def imprimir_ventas(lista_ventas):
    for v in lista_ventas:
        print(f"Venta: {v[0]}, Fecha: {v[1]}, ID Producto: {v[2]}, Total: {v[3]}")

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
    existe = buscar_venta(venta)
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
                while True:
                    if len(productos) == 0:
                        
                        print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                        os.system('pause')
                        break
                    else:
                        print(pyfiglet.figlet_format("vender aeronaves \n"))
                       
                        print('catalogo de aeronaves:')
                        while sw == 0:
                            imprimir_datos(catalogo)
                            try:
                                id = int(input('Ingrese el ID del avion a comprar: '))
                            except ValueError:
                                print('Error, ingrese un ID valido (solo numeros)')
                                os.system('pause')
                                continue
                            lista = buscar(id)
                            if lista == -1:
                                print('Error, ID no valido')
                            else:
                                print('\nCaracteristicas del avion a comprar:\n')
                                print(f'''Modelo: {lista['Modelo']} Marca: {lista['Marca']} Año: {lista['Año']} Consumo: {lista['Consumo']} Unidades: {lista['Unidades']} Horas Totales: {lista['Horas de vuelo']} Precio: ${lista['Precio']}''')
                                try:
                                    cantidad_comprar = int(input('¿Cuantas unidades desea comprar?: '))
                                except ValueError:
                                    print('Error, ingrese una cantidad valida')
                                    continue
                                if cantidad_comprar <= lista['Unidades']:
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
                                            sw = 0
                                        elif decision.lower() == 'no':
                                            os.system('cls')
                                            sw = 1
                                            break
                                    elif decision.lower() == 'no':
                                        os.system('cls')
                                        decision = input('compra cancelada, desea volver a intentarlo? (si/no): ')
                                        if decision.lower() == 'si':
                                            sw = 0
                                        elif decision.lower() == 'no':
                                            os.system('cls')
                                            sw = 1
                                            break
                                else:
                                    os.system('cls')
                                    decision = input('Stock no valido, desea volver a intentarlo? (si/no): ')
                                    if decision.lower() == 'si':
                                        continue
                                    elif decision.lower() == 'no':
                                        os.system('cls')
                                        break
                        if sw != 0:
                            break   

            case 2: # REPORTES
                while True:
                    os.system("cls")
                    print(pyfiglet.figlet_format("vender aeronaves \n"))
                    print('''
                    1. general de ventas
                    2. ventas por fecha especifica
                    3. ventas por rango de fechas
                    4. salir al menu principal
                    ''')
                    op = int(input('Ingrese una opción entre 1-4: '))
                    if op == 1:
                        if len(ventas) == 0:
                            print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                        else:
                            imprimir_ventas(ventas)
                        os.system('pause')

                    elif op == 2:
                        if len(ventas) == 0:
                            print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                        else:
                            while True:
                                fecha = input('Ingrese la fecha (dd-mm-yyyy): ')
                                # Validar formatos incorrectos
                                if "/" in fecha or len(fecha) == 4:
                                    print("Error, debe ingresar la fecha con este formato (dd-mm-yyyy)")
                                    continue
                                # Validar el formato correcto de la fecha
                                else:
                                    ventas_fecha = [venta for venta in ventas if venta[1] == fecha]
                                    if ventas_fecha:
                                        imprimir_ventas(ventas_fecha)
                                    else:
                                        print("No se encontraron ventas para la fecha especificada.")
                                    break



                    elif op == 3:
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
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print('\n agregar productos\n')
                                    id = int(input('Ingrese el id del avion: '))
                                    modelo = input('Ingrese el modelo del avion: ')
                                    marca = input('Ingrese la marca del avion: ')
                                    año = input('Ingrese el año del avion: ')
                                    consumo = input('Ingrese el consumo del avion (xx lt/hr): ')
                                    unidades = int(input('Ingrese las unidades que existen del avion (xx): '))
                                    horas_totales = int(input('Ingrese las horas totales del avion : '))
                                    precio = int(input('Ingrese el precio del avion: '))
                                    agregar_datos(id, modelo, marca, año, consumo, unidades, horas_totales, precio)
                            case 2: # BUSCAR PRODUCTO
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print('\n buscar producto\n')
                                    id = int(input('Ingrese el id del avion que desea buscar: '))
                                    lista = buscar(id)
                                    if lista != -1:
                                        print(lista)
                                    else:
                                        print('No se encontró el producto')
                            case 3: # ELIMINAR PRODUCTO
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print('\n eliminar producto\n')
                                    id = int(input('Ingrese un ID a eliminar: '))
                                    lista = eliminar(id)
                                    if lista != -1:
                                        print('Avion eliminado!')
                                    else:
                                        print('No se encontró el producto')
                            case 4: #MODIFICAR SEGUN ID INGRESADA
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print('modificar por ID')
                                    id_a_modificar = int(input('Ingrese un id para buscar: '))
                                    lista = buscar(id_a_modificar)
                                    if lista != -1:
                                        print('ID encontrado!')
                                        print(lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7])
                                        print('\n')
                                        nuevo_modelo = input('Ingrese el nuevo modelo: ')
                                        nueva_marca = input('Ingrese la nueva marca: ')
                                        nuevo_año = input('Ingrese el nuevo año: ')
                                        nuevo_consumo = input('Ingrese el nuevo consumo: ')
                                        nueva_unidad = int(input('Ingrese las unidades del avion: '))
                                        nueva_horas_totales = int(input('Ingrese las nuevas horas totales: '))
                                        nuevo_precio = int(input('Ingrese el nuevo precio: '))
                                        modificar(id_a_modificar, nuevo_modelo, nueva_marca, nuevo_año, nuevo_consumo, nueva_unidad, nueva_horas_totales, nuevo_precio)
                                        print('\n Nuevos datos actualizados con exito!')
                                    else:
                                        print('Error, ID no existe')
                            case 5: #LISTAR LOS PRODUCTOS EXISTENTES
                                if len(catalogo) == 0:
                                    print('Error, datos no encontrados, cargue los datos en caso de ser necesario.')
                                else:
                                    print('\n listar productos\n')
                                    lista_aviones = leer_datos_productos(productos)
                                    imprimir_datos(lista_aviones)
                    if opc == 6:
                        break
                    os.system('pause')

            case 4: # ADMINISTRACIÓN
                os.system('cls')
                op = 0
                while op != 3:
                    print(pyfiglet.figlet_format("administracion"))
                    print('''
                       
                        ----------------
                        1. Cargar datos
                        2. Respaldar datos
                        444. Test
                        3. Salir
                        ''')
                    op = int(input('Ingrese una opción: '))
                    if op == 1:
                        cargar_datos()
                        os.system('pause')
                        os.system('cls')
                        break
                    elif op == 2:
                        respaldar_datos()
                        os.system('pause')
                        os.system('cls')
                        break
                    elif op == 3:
                        break
                    elif op == 444:
                        print('El largo de los productos es:', len(catalogo), 'y el largo de las ventas es: ' ,len(ventas))
                    else:
                        print('Opción incorrecta.')
                        os.system('pause')
            case 5: #SALIDA DEL SISTEMA
                print('Saliendo del sistema...')
                break
    except ValueError:
        print('Error, Ingrese solo numeros')
        os.system('pause')
        
