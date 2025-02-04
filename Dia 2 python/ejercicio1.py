##Lizcano Jaimes Naya
##1097097811
def convertir_temperatura1(grado):
    convertir= (grado*9/5)+32
    return convertir

grado= int (input ("ingresa el valor en grados fharenheit"))
print (convertir_temperatura1(grado))

def convertir_temperatura(grado):
    convertir= (grado-32)*5/9 
    return convertir


grado= int (input ("ingresa el valor en grados celcius"))
print (convertir_temperatura (grado))

                
