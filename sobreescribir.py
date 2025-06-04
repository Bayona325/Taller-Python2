'''**Sobrescribir un archivo de texto y luego añadir contenido**

- Crea (o sobrescribe) el archivo `diario.txt` y escribe en la primera línea:

  ```yaml
  Fecha: 2025-06-02
  ```

- Luego, abre el mismo archivo en modo append (`'a'`) para agregar dos líneas más con tus actividades del día.

- Al final, vuelve a abrir en `'r'` y muestra todo el contenido por pantalla.'''

def escribirArchivo(path: str, lineas: list, mode = 'w'):
    try:
        with open(path, mode) as file:
            file.writelines(lineas)
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

def continuarArchivo(path: str, mode = 'a'):
    try:
        with open(path, mode) as file:
            texto = input("")
            file.write(texto + "\n")
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

def leer(lec: str) -> list:
    try:
        with open(lec, mode= 'r') as file:
            for linea in file:
                print(linea.strip())
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
        Escribir = escribirArchivo('diario.txt', ["Fecha: 2025-06-02\n"], )
        print(Escribir)

        for i in range(2):
            Continuar = continuarArchivo('diario.txt')
            input(Continuar)

    elif opcion == "2":
        Lectura = leer('diario.txt')
        print(Lectura)
        print("FIN DEL ARCHIVO")
    elif opcion == "3":
        print("Saliendo del programa....")
        print("Has salido del programa.")
        break
    else:
        print("Tomese en serio la vaina \nIngrese una opcion valida \nPresione ENTER para continuar")
