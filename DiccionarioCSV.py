'''
**Crear un CSV de usuarios y leerlo**

- Define una lista de diccionarios con los campos: `{"id": int, "nombre": str, "ciudad": str}` para al menos 5 usuarios ficticios.
- Genera un archivo `usuarios.csv` con encabezado `id,nombre,ciudad` usando `csv.DictWriter`.
- Escribe un script que lea con `csv.DictReader` y filtre solo los usuarios que vivan en “Bogotá”.
- Maneja la excepción `FileNotFoundError` si el CSV no existe.'''

import csv

def escribirArchivoCSV(path: str, lineas: list, encabezados: list, mode = 'w'):
    try:
        with open(path, mode=mode, newline= '') as file:
            escritor = csv.DictWriter(file, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(lineas)
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

def leerArchivoCSV(path: str) -> list:
    try:
        with open(path, mode= 'r', newline='') as file:
            reader = csv.DictReader(file)
            for filas in reader:
                if filas["ciudad"] == "Bogota":
                    print(filas)
            return list(filas)
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

menu = """

██████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀

    1. Escribir datos
    2. Leer datos
    3. Salir
"""

while True:
    print(menu)
    opcion = input("Seleccionem una opcion del Menu:\n -> ")
    if opcion == "1":
        fields = ["id", "nombre", "ciudad"]
        datos = [
        {"id": "1", "nombre": "Jorge", "ciudad": "Bogota"},
        {"id": "2", "nombre": "Ana", "ciudad": "Bogota"},
        {"id": "3", "nombre": "Luis", "ciudad": "Medellin"},
        {"id": "4", "nombre": "Marta", "ciudad": "Medellin"},
        {"id": "5", "nombre": "Carlos", "ciudad": "Bucaramanga"}
        ]
        escribirArchivoCSV('usuarios.csv', datos, fields)
        print("FIN DE ESCRITURA")
    elif opcion == "2":
        leerArchivoCSV('usuarios.csv')
        #for row in leerArchivoCSV('usuarios.csv'):
        #    print(f'{row["id"]} {row["nombre"]} {row["ciudad"]}')           
            #print(f'{row[0]} {row[1]} {row[2]}')
        print('FIN DEL ARCHIVO')

    elif opcion == "3":
        print("Saliendo del programa....")
        print("Has salido del programa.")
        break
    else:
        print("Tomese en serio la vaina \nIngrese una opcion valida \nPresione ENTER para continuar")

