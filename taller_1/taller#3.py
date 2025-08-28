import os
os.system("clear")
print("Bienvenido a su programa que determinara que numero es mas grande entre 3 vaolres")
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
print("El numero mayor es: ", mayor)