import os

registro_de_vuelos = {}
def registro_vuelos(opcion):
    pathArchivo = './registro_vuelos.txt'

    def ingresar_vuelo(hora, destino):
        registro_de_vuelos.update({
            'vuelo': hora +"-"+destino,
        })
        return agregar_a_archivo(pathArchivo, hora + " - " + destino)

    def actualizar_vuelo(nuevo_dato, dato):
        modificar_dato(pathArchivo, nuevo_dato=nuevo_dato, dato=dato)

        return leer_archivo(pathArchivo)

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
        try:
            archivo_abierto = open(ruta)
            arreglo_lineas = archivo_abierto.readlines()
            for linea in arreglo_lineas:
                if linea == str(dato):
                    print(linea)
            archivo_abierto.close()
            agregar_a_archivo(pathArchivo, nuevo_dato)
            eliminar_de_archivo(pathArchivo, dato)
            sobre_escribir_archivo("./registro_vuelos_nuevo.txt")
        except Exception:
            print("No se pudo leer")

    def eliminar_de_archivo(ruta, dato):
        with open(ruta, "r") as input:
            with open("./registro_vuelos_nuevo.txt", "w+") as output:
                for line in input:
                    if line != dato + "\n":
                        output.write(line)
        input.close()
        output.close()

    def leer_archivo(path=pathArchivo):
        try:
            archivo_abierto = open(path, "r")  # por defecto es la r -> read
            arreglo_lineas = archivo_abierto.readlines()
            for linea in arreglo_lineas:
                registro_de_vuelos.update({
                    'vuelo': linea.split("\n")[0]
                })
                print(linea)
            archivo_abierto.close()
        except Exception:
            return print("No se pudo leer")

    def sobre_escribir_archivo(ruta):
        with open(ruta, "r") as input:
            with open(pathArchivo, "w+") as output:
                for line in input:
                        output.write(line)
        input.close()
        output.close()

    def consultar_vuelo(path=pathArchivo):
        return leer_archivo(path)

    def seleccion():
        if opcion == "1":
            hora = input("ingrese hora ")
            destino = input("destino")
            ingresar_vuelo(hora=hora, destino=destino)
        elif opcion == "2":
            consultar_vuelo(pathArchivo)
        elif opcion == "3":
            dato_anterior = input("Ingrese el dato que desea actualizar ")
            nuevo_dato = input("Ingrese el valor del dato que desea actualizar")
            actualizar_vuelo(nuevo_dato=nuevo_dato, dato=dato_anterior)
        elif opcion == "4":
            dato_a_eliminar = input("dato a eliminar")
            eliminar_de_archivo(pathArchivo, dato_a_eliminar)
            sobre_escribir_archivo("./registro_vuelos_nuevo.txt")


    return seleccion()


while True:
    print("Ingrese una opcion: ")
    eleccion = input("\n 1. Ingresar: \n 2. Consultar \n 3. Actualizar  \n 4. Eliminar \n 5. Salir")
    registro_vuelos(eleccion)
    if eleccion == "5":
        break


