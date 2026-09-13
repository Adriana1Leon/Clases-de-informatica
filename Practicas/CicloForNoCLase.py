#Mi forma (Larga)

"""promedio= 0
promedio_final= 1
asistencia= float(input("Ingrese su porcentaje de asistencia: "))

if asistencia < 0 or asistencia >100:
    print ("Datos no válidos")

elif asistencia < 75:
    print("Reprobado por inasistencia.")

else:
    for nota in range (1,4):
        notas= float(input("Ingrese su nota: "))
        if notas > 10 or notas < 0:
            print("Dato no válido")
            break
        else:
            promedio += notas
    else:
        promedio_final= promedio/3
        if promedio_final >= 9:
            print("Excelente.")
        elif promedio_final >= 7:
            print("Aprobado")
        elif promedio_final >= 5:
                print("Debe rendir recuperación")
        else:
                print("Reprobado")
        print(f"Su promedio es: {promedio_final:.2f}")"""


#FORMA CHAT (Más corta)
promedio = 0
asistencia = float(input("Ingrese su porcentaje de asistencia: "))

if asistencia < 0 or asistencia > 100:
    print("Datos no válidos")

elif asistencia < 75:
    print("Reprobado por inasistencia")

else:
    for numero_nota in range(1, 4):
        nota = float(input(f"Ingrese la nota {numero_nota}: "))

        if nota < 0 or nota > 10:
            print("Nota no válida. Vuelva a intentarlo")
            break
        else:
            promedio += nota

    else:
        promedio_final = promedio / 3

        if promedio_final >= 9:
            print("Excelente")
        elif promedio_final >= 7:
            print("Aprobado")
        elif promedio_final >= 5:
            print("Debe rendir recuperación")
        else:
            print("Reprobado")

        print(f"Su promedio es: {promedio_final:.2f}")

