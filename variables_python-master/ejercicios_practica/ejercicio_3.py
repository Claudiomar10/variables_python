# CODE:3
# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese su primer nombre y luego su primer apellido

nombre = str(input('Ingrese por consola su primer nombre:'))

apellido = str(input('Ingrese por consola su primer apellido:'))

# Alumno:
# Imprima en pantalla su nombre y apellido
# utilizando las variables nombre y apellido

print ("Mi Nombre es:", nombre + " " + apellido)

# Crear una variable llamada nombre_apellido donde se 
# almacene el contenido de las variables nombre y apellido
# separando con un espacio su nombre de su apellido

# nombre_apellido = .....
nombre_apellido = nombre + " " + apellido

# Crear una variable llamada cantidad donde se
# almacene la cantidad de caracteres que posee la variable
# nombre_apellido utilizando la función len

# cantidad = len(....)

# Imprimir en pantalla la variable cantidad
cantidad = len(nombre_apellido)
print ("La cantidad de caracteres (incluyendo el espacio) es: ",cantidad)

#para eliminar el espacio podemos utilizar split y join

nombre_apellido = nombre_apellido.split()
print ("Prueba de split: ",nombre_apellido)  #impresion para probar como funciona split

#ahora concatenamos con join y luego aplicamos len para obtener la cantidad de caracteres sin espacio
nombre_apellido = "".join(nombre_apellido)
print ("Prueba join: ",nombre_apellido)    #para probar como funciona join 

#ahora si calculamos la cantidad de caracteres sin espacio
cantidad = len (nombre_apellido)
print ("La cantidad de caracteres (sin considerar el espacio) es: ",cantidad)