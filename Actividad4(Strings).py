#Como hacer una variable de texto con varias lineas.
StringsVariasLineas= """Adriana Leon
ruta 3
Diploma 1B"""
print(StringsVariasLineas)
#Forma 1.
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