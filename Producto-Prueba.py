'''
**Leer y escribir JSON de productos**

   - Crea un diccionario en Python con al menos 3 productos, cada uno con campos: `{"id": int, "nombre": str, "precio": float}`.
   - Escribe ese diccionario en `productos.json` con `json.dump(..., indent=2)`.
   - Luego, abre `productos.json`, cárgalo con `json.load()`, añade un nuevo producto y guarda de nuevo.
   - Captura al menos `json.JSONDecodeError` si el JSON está mal formado.'''

import json

# Crear el archivo JSON inicial
productos = {
    "productos": [
        {"id": 1, "nombre": "Laptop", "precio": 1200.50},
        {"id": 2, "nombre": "Mouse", "precio": 25.99},
        {"id": 3, "nombre": "Teclado", "precio": 45.75}
    ]
}

with open('productos.json', 'w', encoding='utf-8') as archivo:
    json.dump(productos, archivo, indent=2, ensure_ascii=False)

# Leer, modificar y guardar nuevamente
try:
    with open('productos.json', 'r+', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        
        # Añadir nuevo producto
        nuevo_producto = {"id": 4, "nombre": "Monitor", "precio": 199.99}
        datos["productos"].append(nuevo_producto)
        
        # Volver al inicio del archivo para sobrescribir
        archivo.seek(0)
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
        archivo.truncate()
        
    print("Producto añadido correctamente.")

except json.JSONDecodeError:
    print("Error: El archivo JSON está mal formado.")
except FileNotFoundError:
    print("Error: El archivo productos.json no existe.")