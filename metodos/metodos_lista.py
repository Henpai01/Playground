#creando una lista con (list)

lista = list([29 , 25 , 18, True])

#devuelve la cantidad de elementos de una lista 

resultado = len(lista)

#agregando un elementos a la lista 

lista.append(3)

#agregando un elemento a la lista con un indice especifico

lista.insert(2, 54)

#agregando varios elementos a la lista, este mismo se trabaja con [] porque estamos agg elementos a una lista

lista.extend([False, 2023, 24])

#eliminando elementos de la lista(Por su indice)
lista.pop(-1) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo y asi sucesivamente

#remueve un elemento de la lista por su valor

lista.remove(2023)

#remueve toda la lista 
#lista.clear()

#Ordenamos la lista de manera ascendiente, pero si colocamos remove= este no muestra la lista de manera decendiente

lista.sort()

#invirtiendo los elementos de una lista

lista.reverse()

#Verificando si un elemento se encuentra en la lista

elemento_de_lista = lista.index(25)

print(dir(set(["ladsada" , "dasdasd"])))