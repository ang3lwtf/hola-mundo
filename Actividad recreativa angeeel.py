Usuario=input("Como te llamas? ")
print("Holaaa", Usuario, "Bienvenidooo KJDAKJDKLSJLK")

opcion=1
while opcion!=0:
    print("Ingresa 1. Area triangulo")
    print("Ingresa 2. Area Rectangulo")
    print("Ingresa 3. Area Circulo")
    print("Ingresa 4. Convertir Temperatura °F a °C")
    print("Ingresa 5. Convertir Temperatura °C a °F")
    print("Ingresa 0. Salir del programa")
    op=int(input("¿Qué operación quieres hacer con esos números? "))

    if (op==1):
        base=int(input("Ingresa la base: "))
        altura=int(input("Ingresa la altura: "))
        area=(base*altura)/2
        print("El area del triangulo es: ", area)
        
    elif (op==2):
        base1=int(input("Ingresa la base: "))
        altura1=int(input("Ingresa la altura: "))
        area2=base1*altura1
        print("El area del rectangulo es... ", area2)

    elif (op==3):
        radio=int(input("Ingresa el radio: "))
        area3=3.14*radio*radio
        print("El area del circulo es... ", area3)
    elif (op==4):
        fare=int(input("Ingresa los grados °F: "))
        C=((fare-32)*5)/9
        print("Los grados en °C son... ", C, "°")
    elif (op==5):
        CC=int(input("Ingresa los grados °C: "))
        F=(CC*9/5)+32
        print("Los grados en °C son... ", F, "°" )    
    else:
        print("No valido")
    opcion=int(input("Si deseas Continuar presiona cualquier numero, sino presiona 0. para salir "))