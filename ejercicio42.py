

#Pide calificaciones de tareas, proyectos y exámenes y calcula la nota final.



tareas = float(input("Nota tareas: "))
proyecto = float(input("Nota proyecto: "))
examen = float(input("Nota examen: "))

final = (tareas*0.3) + (proyecto*0.3) + (examen*0.4)
print("Nota final:", final)