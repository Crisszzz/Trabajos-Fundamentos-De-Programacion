
#Analisis del primer parcial fe FP
v_canEst = 0
c_valExamteo = 0.40
c_valExamPra = 0.60
v_defPrinPar = 0.0
v_conCic = 1
v_promNotPriPar = 0.0
v_sumNotPriPar = 0.0
v_promNotParteo = 0.0
v_sumNotParteo = 0.0
v_sumNotParPra = 0.0
v_promNotParPra =0.0
v_sumnotMuj = 0.0
a_canMuj=0
v_notMaxMuj=0.0
v_notMinMuj=5.0
v_sumnotHom=0.0
a_canHom=0
v_notMaxHom=0.0
v_notMinHom=5.0
V_promNotPriParM=0.0
V_promNotPriParH=0.0
v_notMaxGru=0.0
v_notMinGru=5.0


# Leer cantidad de estudiantes
v_canEst=int(input("Digite la cantidad de Estudiantes: "))
for v_conCic in range(v_canEst):
    # Captura de datos
    v_nomEst = input("Nombre del estudiante: ") 
    v_genEst = input("Genero del estudiante: ")
    v_notExteo = float(input("Digite nota de examen teorico: "))
    v_notExpra = float(input("Digite nota del examen practico: "))
    print(v_conCic)
    # Calculo de la nota del primer parcial por estudiante
    v_notDePriPar = v_notExteo * c_valExamteo + v_notExpra * c_valExamPra
    print("Su nota del primer parcial: ",v_notDePriPar)
    # Calcular la suma de las notas de los estudiantes para calcular el promedio
    v_sumNotPriPar = v_sumNotPriPar + v_notDePriPar
    v_sumNotParteo = v_sumNotParteo + v_notExteo
    v_sumNotParPra = v_sumNotParPra + v_notExpra
    # Calcular nota maxima
    if v_notDePriPar>v_notMaxGru:
        v_notMaxGru=v_notDePriPar
    if v_notDePriPar>v_notMinGru:
        v_notMinGru=v_notDePriPar

    
    # Calcular el promedio, nota maxima y minima del examen teorico por genero
if v_genEst=="F":
    v_sumnotMuj = v_sumnotMuj + v_notDePriPar
    a_canMuj= a_canMuj + 1
    if v_notDePriPar>v_notMaxMuj:
        v_notMaxMuj=v_notDePriPar
    if v_notDePriPar<v_notMinMuj:
        v_notMinMuj=v_notDePriPar
if v_genEst=="H":
    v_sumnotHom = v_sumnotHom + v_notDePriPar
    a_canHom= a_canHom + 1
    if v_notDePriPar>v_notMaxHom:
        v_notMaxHom=v_notDePriPar
    if v_notDePriPar<v_notMinHom:
        v_notMinHom=v_notDePriPar

        

 
# Calcular promedio del grupo de la nota del primer parcial
v_promNotPriPar = v_sumNotPriPar / v_canEst
print("El promedio de grupo del primer parcias es: ", v_promNotPriPar)

# Calcular el Promedio del examen teorico

v_promNotParteo = v_sumNotParteo / v_canEst
print("El promedio de notas del parcial teorico es: ", v_promNotParteo)

# Calcular el Promedio del examen practico

v_promNotParPra = v_sumNotParPra / v_canEst
print("El promedio de la nota del parcial practico es: ",v_promNotParPra)

# Calcular el promedio del examen teorico por genero

# Por Mujeres
V_promNotPriParM = v_sumnotMuj/a_canMuj
print("El promedio de la nota del primer parcial en las mujeres es: ",V_promNotPriParM)
# Por Hombres
V_promNotPriParH = v_sumnotHom/a_canHom
print("El promedio de la nota del primer parcial en hombres es: ",V_promNotPriParH)


# Nota Maxima y Minima General
print("La nota maxima general fue: ",v_notMaxGru)
print("La nota minima general fue: ",v_notMinGru)


# Nota Maxima y Minima por Mujeres
print("La nota maxima de las mujeres es: ",v_notMaxMuj)
print("La nota minima de las mujeres es: ",v_notMinMuj)

# Nota Maxima y Minima por Hombres
print("La nota maxima de los hombres es: ",v_notMaxHom)
print("La nota minimo de los hombres es: ",v_notMinHom)







