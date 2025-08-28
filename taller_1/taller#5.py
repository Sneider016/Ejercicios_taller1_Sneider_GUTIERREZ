import os
os.system("clear")
print("Bienvenido a tu programa que dibuje un triangulo")
n=int(input("ingrese el tamaño de la base del triangulo: "))
for i in range(1, n+1):
    print("*" * i)