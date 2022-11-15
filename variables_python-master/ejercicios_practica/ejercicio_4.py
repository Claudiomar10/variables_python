# CODE:4
# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
palabra_1 = str(input('Ingrese palabra 1:'))

palabra_2 = str(input('Ingrese palabra 2:'))

palabra_3 = str(input('Ingrese palabra 3:'))

# Objetivo:
# De cada palabra ingresada se utilizará
# la primera letra para armar un acrónimo, por ejemplo:
# Si las palabras ingresadas fueran:
# --> Alumbrado, barrido y limpieza
# El acrónimo resultado es --> abl

# Alumno:
# Crear una variable llamada acronimo donde se 
# almacene la primera letra de cada palabra
# en el orden corespondiente

acronimo = palabra_1[0]+palabra_2[0]+palabra_3[0]

# Imprimir la variable acronimo en pantalla

print ("El acronimo resultante es: ",acronimo)

#otra salida seria transformar las palabras a mayusculas, para que el acronimo quede prolijo

palabra_1 = palabra_1.upper() #transforma la palabra_1 a mayuscula
palabra_2 = palabra_2.upper() #transforma la palabra_2 a mayuscula 
palabra_3 = palabra_3.upper() #transforma la palabra_3 a mayuscula
acronimo = palabra_1[0]+palabra_2[0]+palabra_3[0]
print ("El acronimo formado con letras mayusculas es: ",acronimo)