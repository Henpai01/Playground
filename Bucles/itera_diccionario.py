
diccionario = {
    "nombre" : "Daniels",
    "apellido" : "Rodriguez",
    "Subs" : 10000
}

print(diccionario)

#recorriendo la diccionario para obtener las claves
for key in diccionario:
    key
    print(f'La clave es : {key}')

#recorriendo la diccionario con items() para obtener las claves y el valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]

    print(f'La clave es : {key} y el valor es: {value}')