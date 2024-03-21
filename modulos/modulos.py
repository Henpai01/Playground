#formas de importar un modulo
#formas de modificar un modulo, sencillamente agg el nombre del modulos, despues la palabra"as" osea que si se llama simon y le pones simos as pedro, ahora es pedro

#desde este modulo importamos 4 funciones
from modulo_saludar import saludar_venezolano,saludar_raro,saludar,saludar_formal
import modulo_saludar as m_saludar

#creamos variables con resultados
saludo = saludar("Daniels")
saludo_formal = saludar_formal("Marco")
saludo_raro = saludar_raro("Pedro")
saludo_venezolano = saludar_venezolano("YULIBISADIDA")

#mostramos los resultados
print(saludo_venezolano)
print(saludo_raro)
print(saludo_formal)
print(saludo)

print(saludar.__name__)