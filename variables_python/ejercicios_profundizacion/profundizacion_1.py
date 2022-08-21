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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
#trabajaremos con tres decimales, utilizamos round para truncar los decimales
numero_1 = float(input ("ingrese un numero: "))
numero_2 = float(input("Ingrese un numero: "))

#SUMA
suma = numero_1 + numero_2
print ("La suma de los dos numeros ingresados es: ",round(suma,3))

#RESTA
resta = numero_1 - numero_2
print ("La resta de los dos numeros ingresados es: ",round(resta,3))

#MULTIPLICACION
multiplicacion = numero_1 * numero_2
print ("La multiplicacion de los dos numeros ingresados es: ",round(multiplicacion,3))

#DIVISION
division = numero_1 / numero_2
print ("La division de los dos numeros ingresados es: ",round(division,3))
#NOTA: aca no contemplamos la posibilidad que el segundo numero ingresado sea igual a cero-- ver ese caso

#EXPONENTE/POTENCIA
potencia = numero_1 ** numero_2
print ("La potencia de el primer numero ingresado, elevado al segundo numero ingresado, es: ",round(potencia,3))

