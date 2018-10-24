
path = './registro_vuelos.txt'


def registro_vuelos(opcion):
    def ingresar_vuelo(hora, destino):
        return agregar_a_archivo(path, hora, destino)

    def actualizar_vuelo():
        return

    def eliminar_vuelo():
        return

    def consultar_vuelo(path):
        return leer_archivo(path)

    def leer_archivo(path):
        try:
            archivo_abierto = open(path)  # por defecto es la r -> read
            arreglo_lineas = archivo_abierto.readlines()
            for linea in arreglo_lineas:
                print(linea)
            archivo_abierto.close()
        except Exception:
            print("No se pudo leer")

    def agregar_a_archivo(path, *lineas_a_escribir):
        try:
            archivo_abierto = open(path, "a")  # por defecto es la r -> read
            for linea in lineas_a_escribir:
                archivo_abierto.write("\n" + linea)

            archivo_abierto.close()
        except Exception:
            print("No se pudo leer")

    def elegir_opcion():
        return {
            'ingresar': ingresar_vuelo(),
            'actualizar': actualizar_vuelo(),
            'eliminar': eliminar_vuelo(),
            'consultar': consultar_vuelo()
        }[opcion]
    return elegir_opcion()


opcion = input("Ingrese una opcion \n 1. Ingresar: \n"
               "")
registro_vuelos(opcion)

hora = input("hora")
destino
