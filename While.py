#Continue en for 
cedula= input("Ingrese su cédula: ")
cedula_limpia= " "
for caracter in cedula:
    if caracter == "-" or caracter == " ":
        continue
    cedula_limpia += caracter
print(cedula_limpia)