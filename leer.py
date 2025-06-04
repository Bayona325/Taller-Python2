'''**Leer y mostrar un archivo de texto línea a línea**

- Crea un archivo `notas.txt` con varias líneas de texto (por ejemplo, títulos de películas).
- Escribe un script que abra `notas.txt` en modo lectura y muestre cada línea numerada.
- Si el archivo no existe, captura la excepción `FileNotFoundError` y muestra un mensaje amigable.'''

def leer(lec: str) -> list:
    try:
        with open(lec, mode= 'r') as file:
            for i, linea in enumerate(file, start=1):
                print(f'{i}. {linea}')
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

Lectura = leer('notas.txt')

print(Lectura)
print("FIN DEL ARCHIVO")

#def leer(lec: str) -> list:
#    with open(lec, mode= 'r') as file:
#        for linea in file:
#            print(linea.strip())

#Lectura = leer('notas.txt')
#print(Lectura)
