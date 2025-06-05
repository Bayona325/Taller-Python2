'''
**Convertir CSV a JSON**

   - Toma el `usuarios.csv` del ejercicio anterior, léelo con `csv.DictReader` y conviértelo a una lista de diccionarios.
   - Guarda esa lista en `usuarios.json` usando `json.dump()`.
   - Si ocurre un error de lectura en CSV o JSON, debe manejarse con `try-except`.'''

import csv
import json

try:
    # Leer el CSV y convertirlo a lista de diccionarios
    with open('usuarios.csv', 'r', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        datos = [fila for fila in lector]
    
    # Escribir el JSON
    with open('usuarios.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(datos, jsonfile, indent=2, ensure_ascii=False)
    
    print("Conversión de CSV a JSON completada.")

except FileNotFoundError:
    print("Error: El archivo usuarios.csv no existe.")
except Exception as e:
    print(f"Error durante la conversión: {e}")