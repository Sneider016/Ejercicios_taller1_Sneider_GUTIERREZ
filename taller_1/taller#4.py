import os
os.system("clear")

print("Calcule si un estudiante aprueba la materia o no")
notas = []
for i in range(1, 5):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
if promedio >= 3.5:
    print("El estudiante aprueba la materia con un promedio de:", promedio)
else:
    print("El estudiante no aprueba la materia con un promedio de:", promedio)


