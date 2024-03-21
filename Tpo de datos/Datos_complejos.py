# se cuenta del 0 al 9 
# Cuando es lista (se puede modificar)
lista = ["Daniel Rodriguez", "Aprendiz de Python", 1.85]
# Cuando es tupla (no se puede modificar)
tupla = ("Daniel Rodriguez", "Aprendiz de Python", 1.85)

# se puede m odificar
lista[2] = 1.84
# no se puede modificar
#tupla(3) = 1.82

# creando un conjunto (set)

#se puede redefinir todo el texto + no se puede moficicar por indice, tampoco se puede repertir el indice en el conjunto

Conjunto = {"Daniel Rodriguez", "Aprendiz de Python", 1.85}

#Creando un diccionario (dict) (la estructura es key + value y separamos con comas) 

diccionario = {'nombre' : "Daniel Rodriguez",'Es un' : "Aprendiz de Python", 'mide' : "1.85", 'dato duplicado' : "Daniel Rodriguez",}

print(diccionario['nombre'])
print(diccionario['mide'])
print(diccionario['Es un'])
