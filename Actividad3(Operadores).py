#%%
#Declara tu edad como una variable de tipo entero.  
edad= 16
#%%
#Declara tu estatura como una variable de tipo decimal (float).  
estatura= 1.65
#%%
#Escribe un programa que solicite al usuario la base y la altura de un triángulo y calcule su área 
base= float(input ("Ingrese la base del triángulo: "))
altura= float(input ("Ingrese la altura del triángulo: "))
area= (0.5 * base * altura)
print("El valor del área es:", area)
#%%
#Escribe un programa que solicite al usuario los lados a, b y c de un triángulo y calcule su perímetro
lado_a= float (input("Ingrese el lado a: "))
lado_b= float (input("Ingrese el lado b: "))
lado_c= float (input("Ingrese el lado c: "))
perimetro= (lado_a + lado_b + lado_c)
print("El perimetro de su triángulo es: ", perimetro)
#%%
#Obtén la longitud y el ancho de un rectángulo usando un prompt. Calcula su área y su perímetro 
longitud= float (input("Ingrese el largo del rectángulo: "))
ancho= float (input("Ingrese el ancho del rectángulo: "))
area_rec= longitud * ancho
perimetro_rec= 2 * longitud + 2 * ancho
print ("El área del rectángulo es: ", area_rec)
print ("El perimetro del rectángulo es: ", perimetro_rec)
#%%
#Obtén el radio de un círculo usando un prompt. Calcula el área y la circunferencia
radio= float(input("Ingrese el radio del circulo: "))
area_cir= 3.14 * radio ** 2
circun= 2 * 3.14 * radio
print("El área del círculo es: ", area_cir)
print("La circunferencia del círculo es :", circun)
#%%
#Encuentra la pendiente y la distancia euclidiana entre los puntos (2, 2)  (6, 10). 
x1,y1=2,2
x2,y2= 6,10
pen=  (y2 - y1) / (x2 - x1)
dist= ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La pendiente es :",  pen)
print("La distancia es: ", dist)
#%%
#Calcula el valor de y en la función:y = x² + 6x + 9
x= -3 
y= x**2 + 6*x + 9 
print("y:", y)
#%%
#Encuentra la longitud de las palabras “python” y “dragón” y realiza una comparación booleana (verdadero/falso).  
print(len("python")) == len("dragón"))
#%%
#Usa el operador in para verificar si la palabra “jerga” está en la siguiente oración
oracion= "Espero que este curso no esté lleno de jerga" 
print("jerga" in oracion) 
#%%
#Usa el operador and para verificar si "on" se encuentra tanto en "python" como en "dragon". 
print("on" in "python" and "on" in "dragon") 
#%%
#Encuentra la longitud del texto “python” y convierte ese valor a tipo float y luego a tipo string.  
valor= len("python") 
print(str(float(valor))) 
#%%
#Verifica si la división entera de 7 entre 3 es igual al valor entero de 2.7.  
print(7//3 == int(2.7))
#%%
#Verifica si el tipo de dato de “10” es igual al tipo de dato de 10.  
print(type("10") == type(10))
#%%
#Verifica si int('9.8') es igual a 10.  
print(int(float('9.8')) == 10)
#%%
#Escribe un programa que solicite al usuario ingresar las horas trabajadas y la tarifa por hora. Calcula el pago total.  
horas= float (input("Ingrese las horas trabajadas: "))
tarifa= float (input("Ingrese la tarifa por hora: "))
pago= horas * tarifa

print("Su pago es de: $",pago)
#%%
#Escribe un programa que solicite al usuario ingresar el número de años que ha vivido. Calcula la cantidad de segundos que ha vivido. 
years= int(input("Ingrese el número de años vividos: "))
seg= years * 31536000
print("Segundos vividos: ",seg)
#%%
#Escribe un programa en Python que muestre la siguiente tabla:  
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64") 
print("5 1 5 25 125")
          
