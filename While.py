#Ejercicio pro
palabra = input("ingrese una palabra: ").lower()
vocales = 0 
cons= 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra=="u":
        vocales += 1

        total= (len(palabra))
        cons= total-vocales
print (f"hay {cons} consonantes")
print(f"hay {vocales} vocales")
print (f"hay {total} letras")
    