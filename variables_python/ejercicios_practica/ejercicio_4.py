# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

print('Ingrese palabra 3:')
palabra_3 = str(input())

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
print ("Salida 1")
palabra_11 = palabra_1.upper() #transforma la palabra_1 en mayuscula
palabra_22 = palabra_2.upper() #transforma la palabra_2 en mayuscula
palabra_33 = palabra_3.upper() #transforma la palabra_3 en mayuscula
print (palabra_11[0] + palabra_22[0] + palabra_33[0])

#otra salida posible
print ("Salida 2")
print (palabra_11,palabra_22,palabra_33,"--->",palabra_11[0] + palabra_22[0] + palabra_33[0])


