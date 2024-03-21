
diccionario = {
    "nombre" : "Daniel",
    "apellido" : "Rodriguez",
    "edad" : 18
}

# key nos devuelve un objeto key_item (se puede interar)

claves = diccionario.keys()

#usando la palabra get(), si no encuentra el valor sigue le programa, pero si usamos tipo lista[] nos lanza una exception

valo_de_dadada = diccionario.get("dadada")
print('hola papa, el programa continua')

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario

diccionario.pop("edad")

#obteniendo un elemento dict_item iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)