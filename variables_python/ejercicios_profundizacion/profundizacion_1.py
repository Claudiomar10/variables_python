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
numero_11 = round(numero_1,3)
numero_22 = round(numero_2,3)
#print (numero_11)  lo utilice para probar round, funciona el print pero al operar
#print (numero_22)  con numero_11, y numero_22., no logro truncar los decimales


#SUMA
suma = numero_1 + numero_2
print ("La suma entre",round(numero_1,3),"y",round(numero_2,3),"es:",round(suma,3))

#RESTA
resta = numero_1 - numero_2
print ("La resta entre",round(numero_1,3),"y",round(numero_2,3),"es:",round(resta,3))

#MULTIPLICACION
multiplicacion = numero_1 * numero_2
print ("La multiplicacion entre",round(numero_1,3),"y",round(numero_2,3),"es:",round(multiplicacion,3))

#DIVISION
division = numero_1 / numero_2
print ("La division entre",round(numero_1,3),"y",round(numero_2,3),"es:",round(division,3))
#NOTA: aca no contemplamos la posibilidad que el segundo numero ingresado sea igual a cero-- ver ese caso

#EXPONENTE/POTENCIA
potencia = numero_1 ** numero_2
print ("La potencia entre",round(numero_1,3),"elevado a",round(numero_2,3),"es: ",round(potencia,3))

