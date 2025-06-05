'''
**Manejo de excepciones en concatenación de (str + int)**

   - Pide al usuario que ingrese un nombre (string) y una edad (que se intente convertir a entero).
   - Intenta concatenar `"La edad de " + nombre + " es " + edad`.
   - Si `edad` no se puede convertir, captura el `ValueError` y pide reingresar el dato.'''

while True:
    nombre = input("Ingrese su nombre: ")
    
    try:
        edad = input("Ingrese su edad: ")
        edad_int = int(edad)  # Intentar convertir a entero
        
        # Concatenar correctamente convirtiendo edad a string
        mensaje = "La edad de " + nombre + " es " + str(edad_int)
        print(mensaje)
        break
        
    except ValueError:
        print("Error: La edad debe ser un número entero. Intente nuevamente.")