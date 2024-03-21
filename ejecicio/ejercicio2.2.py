#creando una funcion que nos devuelvan los numeros primos 
#entre el 0 y el argumento que pasamos


#crear una funcion que verifique si el numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno de los numero que termine el bucle
        if num%i==0: return False
    #si termina el bucle significa que el numero no fue divisible entonces, es primo 
    return True

#creando una funcion que retorne una lista con todos los primos 
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso que lo sea creamos una lista
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos

#desempaquetando los retornos de una funcion
resultado = primos_hasta(98)
#el magnifico print, pa saber que devergue hice :D
print(resultado)
