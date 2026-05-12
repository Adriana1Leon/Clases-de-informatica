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

#CICLO for

numbers= [0,1,2,3,4,5]
for number in numbers:
    print(number)

#Ejemplo

notas=[8,7,9,10,6]
suma = 0
for nota in notas:
    suma = suma + nota
promedio= suma/len(notas)
print(promedio)

#Otra forma de hacer el ejemplo
notas=[8,7,9,10,6]
suma = 0
cont=0
for nota in notas:
    cont += 1
    suma = suma + nota
promedio= suma/cont
print(f"El promedio es: {promedio}")

#Ejercicio2
language= "Phyton"
for in letter in language:
    print(letter)

#Ejercicio pro
palabra = input("ingrese una palabra: ")
vocales = 0 
cons= 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra=="u"
    vocales = vocales + 1
    print(f"hay {vocales} vocales")
    cons= len(palabra - vocales)
    print (f"hay {cons} consonantes")
    