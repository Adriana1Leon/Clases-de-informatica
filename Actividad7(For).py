#EJERCICIO LISTAS
"""Escribe un programa que recorra la lista con un ciclo for y determine:
1. La suma total de las notas.
2. El promedio del curso.
3. Cuántos estudiantes aprobaron.
4. Cuántos estudiantes reprobaron. 
Considera que aprueba quien tiene nota mayor o igual a 7."""

notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma= 0
for nota in notas:
    suma = suma + nota
    promedio= suma/len(notas)
print(f"el promedio de la clase es: {promedio}")
    if nota>=7:
    print("Estudiante Aprobado")
else: 
print("Estudiante no aprobado")
