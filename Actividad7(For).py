# EJERCICIO LISTAS

notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma= 0
aprobados= 0
reprobados = 0
cant= 0
for nota in notas:
    suma = suma + nota
    cant= cant+ 1
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados= reprobados + 1
promedio = suma / cantidad
print(f"La suma total de las notas es: {suma}")
print(f"El promedio del curso es: {promedio}")
print(f"La cantidad de estudiantes aprobados es: {aprobados}")
print(f"La cantidad de estudiantes reprobados es: {reprobados}")

# EJERCICIOS STRING

contra = "Python2026"
letras = 0
num = 0
cant_o = 0
for caracter in contra:
    if caracter >= "a" and caracter <= "z":
        letras = letras + 1
    elif caracter >= "A" and caracter <= "Z":
        letras = letras + 1
    elif caracter >= "0" and caracter <= "9":
        numeros = num + 1
    if caracter == "o":
        cant_o = cant_o + 1
print(f"La contraseña tiene {letras} letras.")
print(f"La contraseña tiene {num} numeros.")
print(f"La letra O aparece {cant_o} veces.")

# EJERCICIOS CON SET

productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
cant_productos = 0
letras = 0
for producto in productos:
    cant_productos = cant_productos + 1
    contador = 0
    for letra in producto:
        contador = contador + 1
    if contador > 6:
        letras = letras + 1
print(f"Hay {cant_productos} productos unicos.")
print(f"Hay {letras} productos con mas de 6 letras.")

# EJERCICIO CON BREAK

correo = input("Ingrese su correo: ")
usuario = " "
for letra in correo:
    if letra == "@":
        break
    usuario= usuario + letra
print(f"Su usuario es: {usuario}")

# EJERCICIO CON CONTINUE

tel= input("Ingrese su número de teléfono: ")
telefono_n = ""
for caracter in tel:
    if caracter == " " or caracter == "-":
        continue
    telefono_n= telefono_n + caracter
print(f"Su número teléfonico limpio es: {telefono_n}")
