#While Normal (Con condición)

answer= ""

while answer != "yes":
    answer= (input("Do you agree? (Yes or No): ")).lower() 
print("end")


#While True (Bucle infinito que debe de usar if y break)

while True:
    answer= input("Do you agree? (Yes or No): ").lower()
    if answer in ("yes"):
        print ("end")
        break