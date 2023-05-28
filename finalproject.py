from operator import itemgetter

def es_caracter(cadena):
    try:
        int(cadena)
        return False
    except ValueError:
        return True

def promediototaltotal(c1,c2,c3):
    promediante=(c1+c2+c3)/3
    return promediante

d={}

for i in[1,2,3,4,5,6]:

    
    #promedio de 3 calificaciones parciales:
    print("\n\nponderación de la materia:\n\n55% promedio de 3 calificaciones parciales(3 semanas)\n30% un examen final\n15% tareas en 2 periodos\n\n")
   
    
    
    while True:
        nombre=input("cuál es el nombre del alumno? ")
        if es_caracter(nombre):
            print("\n\nnombre guardado exitosamente :)")
            break
        else:
            print("\n\nun nombre no puede contener un número:c intentalo de nuevo :c")

    while True:
        cal1=float(input("\ncual fue su calificación del primer parcial(semana 1) sobre 100? "))
        if cal1>100:
            print(f"\ntu calificación no puede ser mayor a 100")
        else:
            print(f"\ncalificación parcial 1: ", cal1)
            break

    while True:
        cal2=float(input("\ncual fue su calificacion del segundo parcial(semana 2) sobre 100? "))
        if cal2>100:
            print(f"\ntu calificacion no puede ser mayor a 100")
        else:
            print(f"\ncalificacion parcial 2: ", cal2)
            break

    while True:
        cal3=float(input("\ncual fue su calificacion del tercer parcial(semana 3) sobre 100? "))
        if cal3>100:
            print(f"\ntu calificacion no puede ser mayor a 100")
        else:
            print(f"\ncalificacion parcial 3: ", cal3)
            break

    promedy=promediototaltotal(cal1,cal2,cal3)
    print(f"\npromedio de las 3= ",promedy)
    if promedy<70:
        print("\ntienes un mal promedio de tus 3 calificaciones, debes mejorar aun mas")
    else:
        print("\ntu promedio es bueno, felicidades :D")
    total_primera_parte=promedy*0.55
    print(f"\npromedio sobre la calificacion total de la materia: ",total_primera_parte)

    #obtener porcentaje de examen final

    calexam=float(input("\ncual fue su calificacion del examen final sobre 100? "))
    promedyexam=calexam*.30
    print(f"\ntu promedio del examen sobre la calificacion total de la materia: ",promedyexam)
    if calexam<70:
        print("(\npor cierto, tienes mala calificacion en el examen >:D")
    else:
        print("\npor cierto, buena calificacion en el examen, felicidades :3")

    #obtener porcentaje de tareas(2 periodos)

    tareas1=int(input("\ncual fue tu calificacion del primer periodo de tareas? "))
    tareas2=int(input("\ncual fue tu calificacion del segundo periodo de tareas? "))
    promedytareas=(tareas1+tareas2)/2
    print("\ntu promedio total de las 2 materas es de: ",promedytareas)
    if promedytareas<70:
        print("\ntu promedio de tareas es malo, debes cumplir mas...")
    else:
        print("\ntienes un buen promedio de materias, felicidades :D")


    caltotaltareas=promedytareas*.15
    print(f"\ntu calificacion respecto al total de la materia es: ",caltotaltareas)

    #sacar resultados finales de la materia

    totalpromedy=total_primera_parte+promedyexam+caltotaltareas
    print(f"\n\npromedio total de la materia, del alumno: ",totalpromedy)
    if totalpromedy<70:
        print(f"\ntu promedio fue menor a 50 puntos... nos vemos en extraordinarios ;)\npromedio total:",totalpromedy)
    else:
        print(f"\n\nmuy buen promedio, ¡¡felicidades, arobaste la materia!! tu promedio fue:",totalpromedy)
        print("\n\n")
    d[nombre]=totalpromedy

d_desc = dict(sorted(d.items(), key=itemgetter(1), reverse=True))

print(f"\nla lista sin ordenar es la siguiente: \n",d)
print(f"\n\nla lista con promedios en orden descendente es:\n",d_desc)
print("designed by jonfer :D")