x=3.14159
print(f" El número redondeado sería: {round(x,4)}")


user= input("Ingrese su nombre de usuario: ")

if len(user) > 12:
    print("No puede contener más de 12 caracteres")
elif user.isalpha():
    print("Nombre de usuario válido")
else:
    print("No puede contener espacios ni digitos") 