import os 
os.system("clear")
print("Bienvenido que numero desea consultar un numero")
num=int(input("Ingrese un numero del 1 al 10: "))

if 1<=num<=10:
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
else:
    print("El numero ingresado no esta en el rango solicitado")