print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

#Lista
deportes=["Futbol","Voleibol","Natación","Basquetbol","Dormir"]
print(deportes)
#Que deporte se encuentra en la posicion 2
print(deportes[2])

#En que posicion se encuentra Natación
print(deportes.index("Natación"))


#Agrega otro deporte al final
deportes.append("Handball")
print(deportes)

#Agregar otro deporte en posicion 2
deportes.insert(2,"rebote")
print(deportes)



num_deportes=int(input("cuantos deportes quieres agregar? "))
for i in (range(num_deportes)):
    dep=input("ingresa el deporte madafaker ")
    deportes.append(dep)

print(deportes)


cantidad_saludos=int(input("Cuantos saludos quieres? "))
for i in range(cantidad_saludos):
    print("wazaaaa")



