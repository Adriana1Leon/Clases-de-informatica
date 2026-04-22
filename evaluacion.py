# ===== PARTE A =====
"""Respuesta 1: 
a) str, int, float,
b) Mostraría los tipos de todas las variables y la longitud de la variable "nombre".
c) La función "len(nombre)" se encarga de mostrar el número de caracteres que tiene la variable.

Respuesta 2: 
a) La función "print()" se encarga de mostrar el mensaje establecido al usuario, mientras que
"input()" es utilizado para que el usuario ingrese los datos solicitados.
b)Porque no se ha establecido que tipo de datos van a ser manejados en la variable, si es float, str,
int.
c) El operador / se usa para dividir números, // se usa para dar el resultado de una división pero
solo usando números enteros y por último, % te indica si la divisón va a ser entera o va a tener
decimales, dando el residuo de la davisión.
d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
#python --version
#Python 3.14.3
e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
N/A"""

# ===== PARTE B =====
# Código corregido
"""
a) No declara que tipos de datos son las variables si son str, float, etc. 
b) Porque de ahí el programa ya va a saber con qué tipo de datos va a trabajar. 
"""
#Construcción breve (15 puntos)
"""Escribe un fragmento de código que haga lo siguiente:
1. Cree la variable frase con el texto "Tecnología para todos".
frase= "Tecnología para todos"
2. Muestre la frase en mayúsculas.
print(frase.upper)
3. Muestre la cantidad de caracteres de la frase.
print(len(frase))
4. Verifique si la palabra "Python" está dentro de la frase.
N/A
5. Reemplace "Tecnología" por "Programación".
print(frase.replace("Tecnología", "Programación"))
6. Divida la frase en palabras usando split().
palabras = frase.split()
"""
# ===== PARTE C =====
# Programa integrador
name= input("ingrese su nombre: ")
apellido= input("ingrese su apellido: ")
pais= input("ingrese su país: ")
ancho= input("ingrese el ancho de la pared: ")
alto= input("ingrese el alto de la pared: ")
precio_m= input("ingrese el precio por metro cuadrado: ")
area= ancho * alto
costo_total_e= area * precio_m
#2
nombre_completo= name + " " + apellido
#3

print(f"Nombre: {nombre_completo} \n País: {pais} \n Área: {area} \n Costo {costo_total_e})
print("País: ", pais)
print("El área es: ", area)
print("el costo total es: ", costo_total_e)

print(f"Nombre completo en mayúsculas es: {nombre_completo.upper()}")
print(f"Longitud del nombre completo es: {len(nombre_completo)}")
print(f"¿Está presente la letra 'a' en el nombre completo? { 'a' in nombre_completo }")
print(f"¿El costo total es mayor que 100 dólares? {costo_total > 100}")