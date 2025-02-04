## L izcano Jaimes Naya 
## 10097097811

##ejercicio interes simple
def interes_simple (p , r ,t ):
    simp = (p*r*t)/100
    return simp

def interes_c (ci, t , n , u ):
    com= ci*(1+(u/(100* n)))**(nt)- ci
    return com

p= float(input("Ingrese el capital principal: "))
r= float(input("Ingrese el tasa de interes anual % : "))
t= float(input("Ingrese el tiempo en años: "))
n= float(input("Ingrese el numero de veces  que se capitaliza por año: "))

sim = interes_simple (p, r, t)
ci = interes_c (p, t, n, r)

print("Interes simple = " , sim)
print("Interes compuestos = " , ci)