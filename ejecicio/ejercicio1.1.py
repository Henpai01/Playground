#duraciones de cursos 

otros_cursos_min = 2.5
otros_cursos_med = 4
otros_cursos_max = 7
dalto_curso = 1.5

#Duracion de crudos 
crudo_promedio = 5
crudo_dalto = 3.5


#diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100 
diferencia_con_max= 100 - dalto_curso *1000 // otros_cursos_max /10
diferencia_con_med = 100 - dalto_curso / otros_cursos_med * 100 

#calculando el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = 100 - otros_cursos_med * 1000 // crudo_promedio / 10 
tiempo_vacio_dalto= 100 - dalto_curso * 1000 // crudo_promedio / 10 

#mostrando la diferencia de duracion
print("---------------------")
print("El curso de dalto dura:")
print(f"- un : {diferencia_con_min}% menos que el mas rapido")
print(f"- un : {diferencia_con_max}% menos que el mas lento")
print(f"- un : {diferencia_con_med}% menos que el promedio")
print("---------------------")

#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiemo vacio")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")

print("---------------------")

#Mostrando diferencias si el curso durara 10 horas 
print(f"Ver 10 horas de este curso equivale a {otros_cursos_med * 100 // dalto_curso / 10} horas de este curso")
print(f"Ver 10 horas de otros cursos equivale  {dalto_curso * 100 // otros_cursos_med / 10} de este curso")
print(f"Ver 10 horas de otros cursos equivale  {dalto_curso * 100 // otros_cursos_max / 10} horas de este curso")
print("---------------------")