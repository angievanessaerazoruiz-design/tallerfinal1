

#Crea un programa que pida la edad de una persona y determine su fase de vida:
#"Infancia" (0-12), "Adolescencia" (13-17), "Adultez" (18-59) y "Vejez" (60 o más).


e = int(input("Edad: "))
if e<=12: print("Infancia")
elif e<=17: print("Adolescencia")
elif e<=59: print("Adultez")
else: print("Vejez")
