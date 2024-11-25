#Nesecito una variable que se va a usar
#para terminar el ciclo
numero=1

while numero >0:
    emocion=input("¿Como te sientes? ")
    print("Interesante que te sientas ", emocion)
    numero=int (input("Permaneceren el programa, 0 salir "))


    opcion=1
#En un ciclo while realiza operaciones hasta que el usuario escriba 0
while opcion!=0:
    num1=int(input("Ingresa el primer número "))
    num2=int(input("Ingresa el segundo número "))
    print("Ingresa 1. Sumar")
    print("Ingresa 2. Restar")
    print("Ingresa 3. Multiplicar")
    print("Ingresa 4. Dividir")
    op=int(input("¿Qué operación quieres hacer con esos números? "))
    if (op==1):
        sum=num1+num2
        print("La suma de los números es: ", sum)
    elif (op==2):
        res=num1-num2
        print("la resta...", res)
    elif (op==3):
        mult=num2*num1
        print("La multiplicación es... ", mult)
    elif (op==4):
        div=num1/num2
        print("La division es... ", div)
    else:
        print("No valido")
    opcion=int(input("Deseas Continuar, sino presiona 0. para salir"))