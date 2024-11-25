#CREAR FUNCIONES

#Funcion llamada saludar, va a recibir el nombre de alguien
def saludar(nombre):
    print("Holaaaaaaa ", nombre)
    
nom=input("Ingresa tu nombre: ")
saludar(nom)

#Funcion llamada sumita, va a recibir 5 numeros
#Va a regresar rl valor de la suma
def sumita(n1, n2, n3, n4, n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
num3=int(input("Ingresa el tercer numero: "))
num4=int(input("Ingresa el cuarto numero: "))
num5=int(input("Ingresa el quinto numero: "))


#Mandar llamar a la funcion / USARLA
print(sumita(num1,num2,num3,num4,num5))

#Crear una funcion llamada area_tiangulo
#Que reciba el resultado del area
#prin
#print(area_triangulo(4,5))