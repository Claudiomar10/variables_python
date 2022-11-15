# CODE:6
# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
- El objetivo será realizar un calculadora,
- Se ingresará por consola dos números decimales (float)
- Se deberá calcular todas las operaciones entre ellos:
A) Suma  --> primero número más el segundo    
B) Resta --> primero número menos el segundo
C) Multiplicación --> primero número por el segundo
D) División --> primero número dividido el segundo
E) Exponente/Potencia --> primero número exponente el segundo

- Para todos los casos se debe imprimir en pantalla
  el resultado de la operación realizada

Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Almacenar el valor de cada operación realizada en las
  variables que usted creará con los siguientes nombres:
  suma, resta, multiplicacion, division, potencia

- Al final imprimir todos los resultados almacenados
  en esas variables
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input("Ingrese el primer numero = "))
numero_2 = float(input("Ingrese el segundo numero = "))
#A) SUMA
suma = numero_1 + numero_2
#B)RESTA
resta = numero_1 - numero_2
#C) MULTIPLICACION
multiplicacion = numero_1 * numero_2
#D) DIVISION
division = numero_1 / numero_2
#E) POTENCIA
potencia = numero_1**numero_2

#Salidas Pantalla
print ("El resultado de sumar los dos números es igual a = ",suma)
print ("El resultado de restar los dos números es igual a = ",resta)
print ("El resultado de multiplicar los dos números es igual a = ",multiplicacion)
print ("El resultado de dividir los dos números es igual a = ",division)
print ("El resultado de la potencia del primer número elevado al segundo es igual a = ",potencia)