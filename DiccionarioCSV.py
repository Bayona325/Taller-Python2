'''
**Crear un CSV de usuarios y leerlo**

- Define una lista de diccionarios con los campos: `{"id": int, "nombre": str, "ciudad": str}` para al menos 5 usuarios ficticios.
- Genera un archivo `usuarios.csv` con encabezado `id,nombre,ciudad` usando `csv.DictWriter`.
- Escribe un script que lea con `csv.DictReader` y filtre solo los usuarios que vivan en “Bogotá”.
- Maneja la excepción `FileNotFoundError` si el CSV no existe.'''

'''
**Actualizar un CSV (lectura-escritura)**

   - Lee `usuarios.csv` y modifica la ciudad de un usuario dado (ej. cambiar al usuario con `id=3` a ciudad “Cali”).
   - Sobrescribe el mismo archivo con los cambios.
   - Asegúrate de usar un bloque `try-except` para capturar errores de lectura/escritura.'''

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
            datos = list(reader)
            print("\n=== TODOS LOS USUARIOS ===")
            for usuario in datos:
                print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Ciudad: {usuario['ciudad']}")
            return datos
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

def leerArchivoBogotaCSV(path: str) -> list:
    try:
        with open(path, mode= 'r', newline='') as file:
            reader = csv.DictReader(file)
            print("\n=== Usuarios de Bogota ===")
            for filas in reader:
                if filas["ciudad"] == "Bogota":
                    print(filas)
            return list(filas)
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")


def editarArchivo(path: str, id_usuario: str, nueva_ciudad: str):
    try:
        # Leer el archivo existente
        with open(path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            datos = list(reader)
            encabezados = reader.fieldnames
        
        # Modificar el usuario con el ID especificado
        modificado = False
        for usuario in datos:
            if usuario['id'] == id_usuario:
                usuario['ciudad'] = nueva_ciudad
                modificado = True
                break
        
        if not modificado:
            print(f"No se encontró un usuario con ID {id_usuario}")
            return False
        
        # Escribir los datos actualizados
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=encabezados)
            writer.writeheader()
            writer.writerows(datos)
        
        print(f"Usuario con ID {id_usuario} actualizado a ciudad {nueva_ciudad}")
        return True
        
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")
        return False

menu = """

██████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀

    1. Escribir datos
    2. Leer datos
    3. Editar datos
    4. Salir
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
        leerArchivoBogotaCSV('usuarios.csv')
        print('FIN DEL ARCHIVO')
    elif opcion == "3":
        id_editar = input("Ingrese el ID del usuario a editar: ")
        nueva_ciudad = input("Ingrese la nueva ciudad: ")
        editarArchivo('usuarios.csv', id_editar, nueva_ciudad)

    elif opcion == "4":
        print("Saliendo del programa....")
        print("Has salido del programa.")
        break
    else:
        print("Tomese en serio la vaina \nIngrese una opcion valida \nPresione ENTER para continuar")
        
