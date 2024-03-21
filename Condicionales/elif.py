
ingreso_mesual = 1000
gasto_mesual = 150

#if anidados y else if (elif)

if ingreso_mesual > 10000:
    if ingreso_mesual - gasto_mesual < 0:
         print("Estas como venezolano de 2018")
    elif ingreso_mesual - gasto_mesual > 3000:
         print("Ya no tienes que escapar de latam")
    else:
         print("Estas bajo rey")

elif ingreso_mesual > 1000:
        print("Estas bien")
   
elif ingreso_mesual > 500:
    print("Estas bien en Ecuador")

elif ingreso_mesual > 100:
    print("Estas bien en Venezuela")

else:
    print("Estas pobre como cat")
