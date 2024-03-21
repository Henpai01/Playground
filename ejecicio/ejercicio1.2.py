

frase = input("Decime una frase maestro, y te calculo cuanto demora en decirlo: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabra = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabra} palabras y tardarias {cantidad_de_palabra/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabra *100 // 2*1.3 /10} segundos porque el es mas rapido que el promedio")

if cantidad_de_palabra > 120:
    print("para hijo que no te pedi el testamento")
