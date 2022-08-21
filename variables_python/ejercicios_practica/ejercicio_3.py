# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
from inspect import ClassFoundException


print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre + " " + apellido
print (nombre_completo)

#Utilizo split -- genero una lista con los nombres y apellidos
nombre_completo1 = nombre_completo.split(" ")
#print (nombre_completo1)  #lo utilice para poder ver como funcionaba

#utilizo join para concatenar los nombres sin espacio y poder contar la cantidad de caracteres
nombre_completo2 = "".join(nombre_completo1)
#print (nombre_completo2)   #lo utilice para poder ver como funcionaba


# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
caracteres = len (nombre_completo2)
print ("la cantidad de letras que tiene su nombre completo es: ",caracteres)
