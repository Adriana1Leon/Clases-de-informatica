# Escribe un comentario de múltiples líneas con: nombre, fecha y título.  
Adriana Leon
15-04-2026
Ejercicios Nivel 1

#Declara una variable llamada nombre y asígnale un valor.  
nombre= "Adriana"
#Declara una variable llamada apellido y asígnale un valor.  
apellido= "Leon" 
#Declara una variable llamada nombreCompleto y asígnale un valor.  
nombre_completo= nombre, apellido
#Declara una variable llamada pais y asígnale un valor.  
pais= "Ecuador"
#Declara una variable llamada ciudad y asígnale un valor.  
ciudad= "Quito"
#Declara una variable llamada edad y asígnale un valor.  
edad= "16 años"
#Declara una variable llamada anio y asígnale un valor.  
year= "2026"
#Declara una variable llamada estaCasado y asígnale un valor.  
estado_civil="Soltero"

#Declara una variable llamada esVerdadero y asígnale un valor.  
es_verdadero= "True"

#Declara una variable llamada luzEncendida y asígnale un valor.  
luz_encendida= "On"

#Declara varias variables en una sola línea.  
bebida_fav, colegio , materia= "Té negro helado", "ISM North", "Informática"

#Ejercicios: Nivel 2 
#Comprueba el tipo de dato de todas tus variables utilizando la función integrada type().  
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(year))
print(type(estado_civil))
print(type(es_verdadero))
print(type(luz_encendida))

#Usando la función integrada len(), encuentra la longitud de tu variable nombre.  
print(len(nombre))

#Compara la longitud de tu variable nombre y tu variable apellido.  
# Compara la longitud de tu nombre con la longitud de tu apellido.
print(len(nombre) > len(apellido))
print(len(nombre) < len(apellido))
print(len(nombre) == len(apellido))
# %%

#Declara 5 como numeroUno y 4 como numeroDos.  
numero_uno, numero_dos= 5, 4

#Suma numeroUno y numeroDos y asigna el resultado a una variable llamada total.  
print(numero_uno + numero_dos)

#Resta numeroDos de numeroUno y asigna el resultado a una variable llamada diferencia.  
diferencia= numero_uno - numero_dos
print(diferencia)

#Multiplica numeroUno por numeroDos y asigna el resultado a una variable llamada producto.  
producto= numero_uno * numero_dos
print(diferencia)

#Divide numeroUno por numeroDos y asigna el resultado a una variable llamada division.  
division= numero_uno / numero_dos
print(division)

#Usa el operador módulo para encontrar el residuo de dividir numeroDos para numeroUno y asigna el resultado a una variable llamada residuo.  
resultado= numero_dos % numero_uno
print(resultado)

#Calcula numeroUno elevado a la potencia de numeroDos y asigna el resultado a una variable llamada potencia.  
potencia= numero_uno ** numero_dos
print(potencia)

#Encuentra la división entera de numeroUno para numeroDos y asigna el resultado a una variable llamada divisionEntera.  
division_entera= numero_uno // numero_dos
print(division_entera)

#El radio de un círculo es de 30 metros.  
radio_m= 30 

#Calcula el área de un círculo y asigna el valor a una variable llamada areaCirculo.  
area_cir= 3.14 * radio_m ** 2
print(area_cir)

#Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circunferenciaCirculo.  
circunferencia_circulo= 3.14 * (radio_m * 2)
print(circunferencia_circulo)

#Toma el valor del radio como entrada del usuario y calcula el área. 
rad= input ("Ingrese el valor del rado")
valor=( float(rad) ** 2)* 3.14
print("El valor del área es:", valor)

#Utiliza la función input() para obtener el nombre, apellido, pais y edad de un usuario y almacena cada valor en su variable correspondiente.
nombre= str(input("Ingrese su nombre: ")
apellido= str(input("Ingrese su apellido: "))
pais= str(input("Ingrese su país: "))
edad= int(input("Ingrese su edad: "))

#Ejecuta help('keywords') en la consola de Python o en tu archivo para comprobar las palabras reservadas de Python. 
help('keywords')