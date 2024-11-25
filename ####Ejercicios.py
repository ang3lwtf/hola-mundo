####Ejercicios
'1) Crear una funcion llamada multiplicar que resiba tres numeros, regrese el resultado'
print("multiplicar")
def multiplicar(n1,n2,n3):
    res_mult=n1*n2*n3
    return res_mult

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
num3=int(input("Ingresa el tercer numero: "))

print(multiplicar(num1,num2,num3))

'2)Crea una funcion llamada largo_cadena que reciba un texto y devuelve la cantidad de caracteres en la misma'
print("caracteres de texto")
def largo_cadena(texto):
    elementos=len(texto)
    return elementos

text=(input("Ingresa el texto: "))
print(largo_cadena(text))

"3) crear una funcion llamada promedio que reciba 2 calificaciones "
print("promedioooooo")
def promedio(n1,n2):
    prom=(n1+n2)/2
    return prom
num1=float(input("Ingresa la primera calificación: "))
num2=float(input("Ingresa la segunda calificación: "))
print(promedio(num1,num2,))

#funcion recibir nombre, edad y mes. Devolver: dos primeras letras de nombre-edad-mes; letra del mes: MA170
def disk_curp(nombre, edad, mes):
    letras=nombre[0:2] 
    letr=edad[0:2]
    let=mes[0]
    return letras, letr, let

nom=(input("Ingresa tu nombre: "))
ed=int(input("Ingresa tu edad: "))
m=input("ingrea tu mes de naciomiento: ")
print(disk_curp(nom,ed,m)) 