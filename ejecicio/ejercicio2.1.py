#falto el profe a la clase y los pibes van a hacerla solos

#pedir el nombre de los amigos de clases 

def obtener_Amigos_de_clases(cantidad):
    #crear una lista de amigos de clase
    amigos_de_clase = []
    #ejecutando for para pedir informacion de los estudiantes 
    for i in range(7):
     nombre = input("Ingresar Nombre del estudiante: ")
     edad = int(input("Ingresar la edad del estudiante: "))
     amigo_de_clase = (nombre,edad)
     #agregando a la lista los amigos de clases 
     amigos_de_clase.append(amigo_de_clase)
     #ordenandolos de mayor a menor segun su edad
    amigos_de_clase.sort(key=lambda x:x[1])

    #amigos de clase[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = amigos_de_clase[0][0]
    profesor = amigos_de_clase[-1][0]
    #retorno de la tupla 
    return asistente,profesor
#desempaquetamos una funcion 
asistente,profesor =  obtener_Amigos_de_clases(5)
#bueno el print XD
print(f"El profesor es: {profesor} y su asistente es {asistente}")

