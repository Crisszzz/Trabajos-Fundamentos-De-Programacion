
# Analisis del primer parcial de FP
#Analisis del primer parcial fe FP
v_canEst = 0
c_valExamteo = 0.40
c_valExamPra = 0.60
v_defPrinPar = 0.0
v_conCic = 1
v_promNotPriPar = 0.0
v_sumNotPriPar = 0.0
v_promNotPriPar = 0.0
v_promNotParteo = 0.0
v_sumNotParteo = 0.0
v_sumNotParPra = 0.0
v_promNotParPra =0.0
# Leer cantidad de estudiantes
v_canEst=int(input("Digite la cantidad de Estudiantes: "))
for v_conCic in range(v_canEst):
     #opciones
    def opcion_calcular_la_nota_del_primer_parcial_por_estudiante():
      print("Ha seleccionado la opcion de Nota del primer parcial por estudiante")
      v_nomEst = input("Nombre del estudiante: ") 
      v_genEst = input("Genero del estudiante: ")
      v_notExteo = float(input("Digite nota de examen teorico: "))
      v_notExpra = float(input("Digite nota del examen practico: "))
      # Calculo de la nota del primer parcial por estudiante
      v_notDePriPar = v_notExteo * c_valExamteo + v_notExpra * c_valExamPra
      print("Su nota del primer parcial: ",v_notDePriPar)



      # Funcion de opciones
    while True:
        print("Menu principal:")
        print("1. Opcion calcular la nota del primer parcial por estudiante")
        print("2. Cerrar programa")
        opciones = input("Seleccione una opcion: ")
        if opciones =="1":
            opcion_calcular_la_nota_del_primer_parcial_por_estudiante()
        elif opciones =="2":
            break   
        

