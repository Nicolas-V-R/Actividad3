#Ejercicio 17 ya se realizo

#Ejercicio 18
def ej18():
    n = int(input("Ingresa un numero entero: "))
    suma = sum(range(n + 1, n + 101))
    print("La suma de los 100 numeros siguientes es ", suma)

ej18()

#Ejercicio 19

def ej19():
    euros = float(input("Cantidad en euros: "))
    tasa = 1.13
    dolares = euros * tasa
    print(f"{euros} euros son {dolares:.2f} dolares")

ej19()

#Ejercicio 20

def ej20():
    altura = float(input("Altura del rectangulo: "))
    ancho = float(input("Ancho del rectangulo: "))
    area = altura * ancho
    print("El área del rectangulo es ", area)

ej20()

#Ejercicio 21

def ej21():
    x = float(input("Primer numero: "))
    y = float(input("Segundo numero: "))
    if x > y:
        print("El mayor es ", x, "y el menor es ", y)
    elif y > x:
        print("El mayor es ", y, "y el menor es ", x)
    else:
        print("Ambos numeros son iguales")

ej21()


#Ejercicio 22

def ej22():
    n = int(input("Ingresa un numero entero: "))
    print("Numeros impares menores que ", n)
    for i in range(1, n, 2):
        print(i, end=' ')

ej22()


#Ejercicio 23

def ej23():
    t = int(input("Primer numero: "))
    u = int(input("Segundo numero: "))
    while u != 0:
        t, u = u, t % u
    print("El maximo comun divisor e :", t)

ej23()


#Ejercicio 24

import math

def ej24():
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))

    cuadratica_1 = b**2 - 4*a*c

    if a == 0:
        print("No es una ecuación cuadrotica")
    elif cuadratica_1 < 0:
        print("No tiene solucion real")
    elif cuadratica_1 == 0:
        x = -b / (2*a)
        print("Tiene una solucion ", x)
    else:
        x1 = (-b + math.sqrt(cuadratica_1)) / (2*a)
        x2 = (-b - math.sqrt(cuadratica_1)) / (2*a)
        print("Las soluciones son ", x1, "y", x2)

ej24()
