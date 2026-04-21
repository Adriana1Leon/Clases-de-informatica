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
print(challenge)
#Count (Importante)
challenge= "thirty days of python"
print(challenge.count("y", 7, 14))