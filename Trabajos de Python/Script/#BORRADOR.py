import random
import matplotlib.pyplot as plt

# Crear lista con los equipos de la liga colombiana
equipos = ["América de Cali", "Atlético Bucaramanga", "Atlético Huila", "Atlético Nacional", "Boyacá Chicó", "Deportes Quindío", 
           "Deportivo Cali", "Deportivo Pasto", "Deportivo Pereira", "Envigado FC", "Independiente Medellín", "Jaguares de Córdoba",
           "Junior FC", "La Equidad", "Millonarios FC", "Once Caldas", "Rionegro Águilas", "Santa Fe", "Tolima", "Unión Magdalena"]

# Crear listas vacías para los equipos locales, visitantes y goles
equipos_locales = []
equipos_visitantes = []
goles_locales = []
goles_visitantes = []

# Generar datos para cada partido
for i in range(len(equipos)):
    for j in range(len(equipos)):
        if i != j:  # El equipo local y visitante no pueden ser el mismo
            equipos_locales.append(equipos[i])
            equipos_visitantes.append(equipos[j])
            goles_locales.append(random.randint(0, 5)) #Los goles son marcados aleatoriamente entre 0 y 5
            goles_visitantes.append(random.randint(0, 5))

while True:
    print("\n========== MENU ==========")
    print("1. Ver número de partidos jugados por cada equipo")
    print("2. Ver número de partidos ganados, perdidos y empatados por cada equipo")
    print("3. Ver número de goles marcados por cada equipo local y crear gráfico")
    print("4. Ver número de goles marcados por cada equipo visitante y crear gráfico")
    print("5. Ver número total de goles marcados en todos los partidos")
    print("6. Ver cantidad total de partidos por equipo")
    print("7. Ver listado para cada equipo con sus goles de local y de visitante")
    print("8. Ver equipos que más y menos goles realizaron en TOTAL")
    print("9. Ver nombre del equipo, los partidos en lo que ha participado y sus marcadores")
    print("10. Ver tabla de posiciones y lista con los puntos por equipo")
    print("11. Ver tabla de posiciones según los puntos obtenidos")
    print("12. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # (PUNTO 1) Calcular el número de partidos jugados por cada equipo
        partidos_jugados = {}  # Diccionario para almacenar el número de partidos jugados por cada equipo
        for equipo in equipos:
            partidos_jugados[equipo] = 0  # Inicializa el contador para cada equipo en 0
            for local in equipos_locales:
                if local == equipo:
                    partidos_jugados[equipo] += 1
            for visitante in equipos_visitantes:
                if visitante == equipo:
                    partidos_jugados[equipo] += 1

        print("PARTIDOS JUGADOS POR CADA EQUIPO")
        # Imprimir el número de partidos jugados por cada equipo
        for equipo in equipos:
            print(equipo + ": " + str(partidos_jugados[equipo]) + " partidos jugados")

    elif opcion == "2":
        # (PUNTOS 2, 3 Y 4) Calcular el número de partidos ganados, perdidos y empatados por cada equipo
        partidos_ganados = {}  # Diccionario para almacenar el número de partidos ganados por cada equipo
        partidos_perdidos = {}  # Diccionario para almacenar el número de partidos perdidos por cada equipo
        partidos_empatados = {}  # Diccionario para almacenar el número de partidos empatados por cada equipo

        for equipo in equipos:
            partidos_ganados[equipo] = 0
            partidos_perdidos[equipo] = 0
            partidos_empatados[equipo] = 0
            for i in range(len(equipos_locales)):
                if equipos_locales[i] == equipo:
                    if goles_locales[i] > goles_visitantes[i]:
                        partidos_ganados[equipo] += 1
                    elif goles_locales[i] < goles_visitantes[i]:
                        partidos_perdidos[equipo] += 1
                    else:
                        partidos_empatados[equipo] += 1
                elif equipos_visitantes[i] == equipo:
                    if goles_visitantes[i] > goles_locales[i]:
                        partidos_ganados[equipo] += 1
                    elif goles_visitantes[i] < goles_locales[i]:
                        partidos_perdidos[equipo] += 1
                    else:
                        partidos_empatados[equipo] += 1

        print("PARTIDOS GANADOS, PERDIDOS Y EMPATADOS POR CADA EQUIPO")
        # Imprimir el número de partidos ganados, perdidos y empatados por cada equipo
        for equipo in equipos:
            print(equipo + ": " + str(partidos_ganados[equipo]) + " partidos ganados, " + str(partidos_perdidos[equipo]) + " partidos perdidos, " + str(partidos_empatados[equipo]) + " partidos empatados")
    
    elif opcion == "3":
        # (PUNTO 5) Calcular el número de goles marcados por cada equipo local y crear un gráfico
        goles_equipo_local = {}
        for equipo in equipos:
            goles_equipo_local[equipo] = 0
            for i in range(len(equipos_locales)):
                if equipos_locales[i] == equipo:
                    goles_equipo_local[equipo] += goles_locales[i]

        print("GOLES MARCADOS POR CADA EQUIPO LOCAL")
        #Imprimir la cantidad de goles marcados por cada equipo jugando como local
        for equipo in equipos:
            print(equipo + ": " + str(goles_equipo_local[equipo]) + " goles como local")
        
        #Utilizar la biblioteca Matplotlib para elaborar el gráfico
        plt.bar(goles_equipo_local.keys(), goles_equipo_local.values(), color='g')
        plt.title('Número de goles marcados por equipos locales') #Título del gráfico
        plt.xlabel('Equipos') #Título del eje horizontal
        plt.ylabel('Goles') #Título del eje vertical
        plt.show()

