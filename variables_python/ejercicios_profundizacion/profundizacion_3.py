# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

Cualquier duda con estos métodos pueden consultarla por el campus
'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio
nombre = input ("Ingrese su nombre completo: ")

#nombre con todas las letras en minusculas
nombre_minuscula = nombre.lower()
print ("El nombre completo en minuscula es:",nombre_minuscula)

#nombre con todas las letras en mayusculas
nombre_mayuscula = nombre.upper()
print ("El nombre completo en mayuscula es:",nombre_mayuscula)

#nombre con la primer letra del nombre en mayuscula (Solo el primer nombre de la cadena)
nombre_capitalize = nombre.capitalize()
print ("El nombre con la primera letra en mayuscula es:",nombre_capitalize)

#nombre con la primera letra en mayuscula en cada nombre que compone el nombre completo
nombre_t = nombre.title()
print ("El nombre con la primera letra mayuscula en cada nombre es:",nombre_t)
