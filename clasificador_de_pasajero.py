
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño, pasa gratis")
elif edad >= 12 and edad <= 17:
    print("Adolecente: media tarifa")
elif edad >= 18 and edad <= 64: 
    print(" Adulto: tarifa completa")
else:
   print("Adulto mayor: media tarifa")
