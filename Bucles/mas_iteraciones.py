
frutas = ["cambur", "pera", "manzana", "fresa"]
cadena = "Hola Daniels"
numeros = [5,8,16,35]

#evitando que se coma una manzana con la sentencia continue 
for fruta in frutas:
    if fruta == "manzana":
      continue
    print(f'La fruta que me voy a comer es: {fruta}')

#evitando que el bucle siga ejecutandose(el else no se ejecuta tampoco)

for fruta in frutas:
    if fruta == "manzana":
      break
    print(f'La fruta que me voy a comer es: {fruta}')

print("Bucle terminado")
#recorriendo una cadena de texto 
for letra in cadena:
   print(letra)

#forma compleja de usar for
numero_duplicados = list()
for numero in numeros:
   numero_duplicados.append(numero*2)
print(numero_duplicados)

#forma de usar for en una linea de codigo
numero_duplicados = [x*2 for x in numeros]
print(numero_duplicados)
