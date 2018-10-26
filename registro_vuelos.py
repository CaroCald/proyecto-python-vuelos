import re

def registro_vuelos(opcion):
    pathArchivo = './registro_vuelos.txt'

    def ingresar_vuelo(hora, destino):
        return agregar_a_archivo(pathArchivo, f"Hora: {hora}", f"Destino: {destino} \n")

    def actualizar_vuelo(pathArchivo, nuevo_dato, dato):
        contenido = modificar_dato(pathArchivo, nuevo_dato, dato)
        agregar_a_archivo(pathArchivo, contenido)
        return print(contenido)

    def eliminar_vuelo(dato):
        return eliminar_de_archivo(pathArchivo, dato)

    def agregar_a_archivo(path, *lineas_a_escribir):
        try:
            archivo_abierto = open(path, "a")  # por defecto es la r -> read
            for linea in lineas_a_escribir:
                archivo_abierto.write("\n" + linea)

            archivo_abierto.close()
            return print('Ingresado con exito!')
        except Exception:
            return print("No se pudo leer")

    def modificar_dato(ruta, nuevo_dato, dato):
        with open(ruta, 'r') as archivo:
            arreglo_lineas = archivo.readlines()
            
            for linea in arreglo_lineas:
                if dato in linea:
                    linea = linea.replace(dato, nuevo_dato)
                    arreglo_lineas = linea

        return arreglo_lineas


    def eliminar_de_archivo(ruta, dato):
        with open(ruta, "r") as input:
            with open("./registro_vuelos_nuevo.txt", "wb") as output:
                for line in input:
                    if line != dato + "\n":
                        output.write(line.encode())
        input.close()
        output.close()

    def leer_archivo(path=pathArchivo):
        try:
            archivo_abierto = open(path, "a")  # por defecto es la r -> read
            arreglo_lineas = archivo_abierto.readlines()
            for linea in arreglo_lineas:
                print(linea)
            archivo_abierto.close()
        except Exception:
            return print("No se pudo leer")

    def consultar_vuelo(path=pathArchivo):
        return leer_archivo(path)

    def seleccion():
        if opcion == "1":
            hora = input("ingrese hora ")
            destino=input("destino")
            ingresar_vuelo(hora=hora, destino=destino)
        elif opcion == "2":
            consultar_vuelo(pathArchivo)
        elif opcion == "3":
            nuevo = input("Nuevo Dato")
            hora = input("Ingrese hora ")
            actualizar_vuelo(pathArchivo,  nuevo,hora)
        elif opcion == "4":
            dato = input("dato a eliminar")
            eliminar_vuelo(dato)

    return seleccion()

print("Ingrese una opcion: ")
eleccion = input("\n 1. Ingresar: \n 2. Consultar \n 3.Actualizar  \n 4. Eliminar")

registro_vuelos(eleccion)
