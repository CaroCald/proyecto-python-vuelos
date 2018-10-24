def registro_vuelos(opcion):
    pathArchivo = './registro_vuelos.txt'

    def ingresar_vuelo(hora, destino):
        return agregar_a_archivo(pathArchivo, f"Hora: {hora}", f"Destino: {destino} \n")

    def actualizar_vuelo():
        return print('actualizar')

    def eliminar_vuelo():
        return print('eliminar vuelo')

    def agregar_a_archivo(path, *lineas_a_escribir):
        try:
            archivo_abierto = open(path, "a")  # por defecto es la r -> read
            for linea in lineas_a_escribir:
                archivo_abierto.write("\n" + linea)

            archivo_abierto.close()
            return print('Ingresado con exito!')
        except Exception:
            return print("No se pudo leer")

    def leer_archivo(path=pathArchivo):
        try:
            archivo_abierto = open(path)  # por defecto es la r -> read
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
    return seleccion()


eleccion = input("Ingrese una opcion \n "
               "1. Ingresar: \n"
               "2. Actualizar \n"
               "3. Consultar \n"
               "4. Eliminar")

registro_vuelos(eleccion)
