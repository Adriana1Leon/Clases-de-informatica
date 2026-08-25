#Como hacer una variable de texto con varias lineas
StringsVariasLineas= """Adriana Leon
ruta 3
Diploma 1B"""
print(StringsVariasLineas)

#Forma 1
colegio= "Ism"
longitud= len(colegio)
print(longitud)

#otra forma.
print(len("San Fransisco de Quito"))

#Unir 2 variables de texto
nombre="Adriana"
apellido= "León"
nombre_completo= nombre +" "+ apellido
print ("Mi nombre completo es: ", nombre_completo)

#Para repetir un string un determinado número de veces:
print(nombre_completo * 3)

#Funcion \n como "enter"
print("Python\nChallenge\njaja")

#\t como tecla de tabulación
print("Adriana\tSemana 1\tSemana 2\tSemana 3")

# \\ para poner caracteres literales (Inútil)
print("símbolo(\\)")

#Nuevo método de escribir mensajes
print(f"Mi nombre es: {nombre} y mi apellido es {apellido}")

#Desempaquetado visual (Inútil)
language= "Python"
a,b,c,d,e,f = language
print(b)
last_three= language[0:3]
print(last_three)

#Navegando caracteres
last_three= language[-3:] 
"""le dice al programa que agarre las 3 últimas letras de
la palabra, y esto se da por los : al final."""
print (last_three)

#Invertir caracteres
greeting= "Hello, World!"
print(greeting[::-1]) #Se usa [::-1] siempre, lo único que cambia es el texto.

#Imprimir solo los caracteres que unop quiera de la palabra
language= "Python"
pto= language[0:6:2] #el 0 representa donde inicia, el 6 es el final, el 2 es el salto que da.
print(pto)

#Capitalize
challenge= "thirty days of python"
print(challenge.capitalize())

#Count (Importante)
challenge= "thirty days of python"
print(challenge.count("y", 7, 14))


#Nivel 1
#Crea una variable texto con el valor: 
texto = "Programación Para Todos"
#Muestra el contenido de la variable en pantalla.  
print(texto)
#Muestra la cantidad de caracteres que tiene la cadena.  
print("Cantidad de caracteres:", len(texto))

#Nivel 2
#Convierte la cadena a mayúsculas.  
print(texto.upper())
#Convierte la cadena a minúsculas.  
print(texto.lower())
#Aplica title() y muestra el resultado.  
print(texto.title())
#Aplica capitalize() y muestra el resultado.  
print(texto.capitalize())

#Nivel 3
#¿La cadena empieza con "Programación"?  
print(texto.startswith("Programación"))
#¿La cadena termina con "Todos"?  
print(texto.endswith("Todos"))
#Encuentra la posición de la palabra "Para".  
print(texto.find("Para"))
#Verifica si la cadena contiene la palabra "Python".
print("Python" in texto)

#Nivel 4
#Reemplaza "Programación" por "Python".  
print(texto.replace("Programación", "Python"))
#Divide la cadena en palabras usando split().  
palabras = texto.split()
print(palabras)
#Une las palabras usando " - " como separador.  
print(" - ".join(palabras))

# Nivel 5
#Muestra el primer carácter de la cadena.  
print(texto[0])
#Muestra el último carácter de la cadena.  
print(texto[-1])
#Muestra el carácter en la posición 5.  
print(texto[5])

#Nivel 6
#Crea una variable con tu nombre completo.  
nombre = "Adriana"
apellido = "León"
#Muestra un mensaje usando format() o f-string: 
"Hola, mi nombre es ___"  
print(f"Hola, mi nombre es {nombre} {apellido}")

#Crea un acrónimo con tus iniciales.
print(nombre[0] + apellido[0])