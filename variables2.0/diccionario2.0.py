#creando un diccionario con dict()

diccionario = dict(nombre= "Daniel", apellido= "Rodriguez")

#las listas no puedes ser claves y usamos frozenset para matar conjuntos

diccionario = {frozenset(["Daniels","Venezolano" ]): "jajaja"}

#creando diccionario con fromkeys() con 2 parametros = NONE
diccionario = dict.fromkeys(["Nombre","Apellido"])

#creando diccionario con fromkeys() con 2 parametros = Cambiando el valor por defecto a "No hay informacion"
diccionario = dict.fromkeys("ABCDEF","No hay informacion")

print(diccionario)