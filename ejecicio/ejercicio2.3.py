#creando una funcion que muestre la serie fibonacci entre el 0 y el numero dado

def fibonacci(num):
    fibonacci_lista = [0]
    a,b = 0,1
    for i in range(num):
      
      if a+b > num: return fibonacci_lista
      else:
         fibonacci_lista.append(b)
         a,b = b,a+b


resultado = fibonacci(20)
print(resultado)




