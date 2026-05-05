variable_de_control= 1
while variable_de_control < 5:
    print(variable_de_control)
    print(f "Esta es la vuelta: {variable_de_control}")
    variable_de_control +=1 # es lo mismo q variable_de_control = variable_de_control +1
else:
    print("No se ejecutó el ciclo")
print("El ciclo terminó")

clave= ""
while clave!="python123":
    clave= input("Ingrese la clave")
print("Acceso permitido")

# Ejercicio de codificar el menú
opciones= ""
while opciones != "c":
    print("a. Saludar")
    print("b. Mostrar mensaje")
    print("c. Salir")
    opciones = input("Ingrese la opción")
    if opciones== "a":
        print ("Bienvenido")
    elif opciones== "b":
        print("Clase de informática")
    elif opciones== "c":
        print("Saliendo del programa")
    else:
        print("Opción no válida")