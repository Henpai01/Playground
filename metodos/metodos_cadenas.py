
cadena1 = "Hola,Daniel"
cadena2 = "bienvenido bro"

#Convierte todo a Mayusculas (Upper)
Mayusc1 = cadena1.upper()
#Convierte todo Minusculas (Lower)
Mayusc2 = cadena1.lower()

#Primera en Mayuc
Primera_mayusc = cadena1.capitalize()

#Buscamosen otra cadena, si no hay resultados nos da -1 

busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay resultado, no lanza error

busqueda_index = cadena1.index("D")

#Nos indentifica si tiene un valor numerico osea nos da true, sino da false

es_numerico = cadena1.isnumeric()

#si es alpha numerico devolvemos true, sinop devolvemos false

es_alfanumerico = cadena1.isalpha()

#Contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencia exactas que hay

contar_coincidencia = cadena1.count("Hola")

# "len" contamos cuantos caracteres tiene una cadena 

contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con una cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("l")

#si el valor x se encuentra en la cadena original, remplaza el valor x por otro valor (osea Y)
#basicamente modifica el producto/palabra de la frase

cadena_nueva = cadena1.replace(","," ")

cadena_nueva_2 = cadena1.capitalize()

#nos va a separar cadena con la cadena que le pasemos

cadena_separada = cadena1.split(",")

print(cadena_separada[1])