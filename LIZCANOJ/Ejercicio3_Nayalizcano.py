## Lizcano Jaimes Naya
## 1097097811

print("Los numeros que satisfacen la expresion son: ")
##Crear un for anidado en el rango que queramos
for p in range(200):
    for q in range(200):
        expresionMatematica = p**3 + q**4 - 2*p**2
        ##Escribir la expresion matematica y condicionarla para mostar numeros 
        if (expresionMatematica<680):
            print("p: ", p)
            print("q: ", q)
            print("Sumatoria: ", expresionMatematica)

## Lizcano Jaimes Naya
## 1097097811