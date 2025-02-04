## Lizcano Jaimes Naya
## 1097097811

##Algunas veces debemos definir las variables para evitar errores de indefiniciones
mayorNum = 0
menorNum = 0
##Creamos un ciclo para que se repita 10 veces
for i in range(1,11):
    print("Ingrese el termino #", i)
    n = int(input())
    print(n)
    if (mayorNum == 0) or (menorNum == 0):
        mayorNum = n
        menorNum = n
    else:
        if (n>mayorNum):
            mayorNum = n
        else:
            if (n<menorNum):
                menorNum = n
print("El numero mayor es: ", mayorNum)
print("El numero menor es: ", menorNum)

## Lizcano Jaimes Naya
## 1097097811