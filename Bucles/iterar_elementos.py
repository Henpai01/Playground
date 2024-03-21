
animales = ["Gato","Perro","Loro","Avestru"]

numeros = (13,15,27,41)

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es un: {animal}')


#recorriendo la lista numeros y multiplicando cada valor por 3
for numero in numeros:
    Resultado = numero * 3
    print(f'El numero multiplicado por 3 da: {Resultado}')

#iterando 2 lista de mismo tamano a mismo tiempo 

for animal,numero in zip(animales,numeros):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')

#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)

for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice 

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es {valor}')

#usando else en el ultimo

for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino ')


#todo lo anterior funciona igual para tuplas y conjuntos