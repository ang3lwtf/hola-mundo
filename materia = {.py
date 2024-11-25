materia = {
    "nombre": "Programación",
    "codigo": "INF02",
    "profesor": "Mari García",
    "horarios": ["Lunes 9:00-11:00", "Miércoles 9:00-11:00"],
    "creditos": 10,
    "nivel": "Intermedio",
    "prerequisitos": ["Computación 1"],
    "descripcion": "Desarrollo de algoritmos"
}

print (materia ["nombre"])

alumno = {
    "nombre": "Jose angeeeel",
    "matricula": "2200270214",
    "semestre": "quinto",
    "calificaciones": {
        "Matemáticas": 10,
        "Física": 10,
        "Programación": 10,
        "Química": 10
    },        
    "direccion": {
        "calle": "Isabela la catolica",
        "ciudad": "Calera de victor rosales (calerayork)",
        "codigo postal": "98500"
    },
    "telefono": "478-108-1197",
    "email": "angsincontrol@gmail.com"
}
print (alumno ["nombre" ])
print (alumno["calificaciones"])

print("La calificación del alumno en programación es:")
print (alumno[ "calificaciones"] ["Programación" ])