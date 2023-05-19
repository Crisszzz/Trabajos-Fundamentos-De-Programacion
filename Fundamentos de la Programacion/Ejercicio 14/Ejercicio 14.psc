Algoritmo sintitulo
	//Descripcion: Resolver una ecuacion de segundo grado
	//Programador:Cristian Vargas
	//Version: 1.0
	//Fecha: 03/03/2023
    // Declaración de variables
    Definir A, B, C, x1, x2, discriminante Como Real
    
    // Lectura de coeficientes de la ecuación
    Escribir "Introduce el coeficiente A de la ecuación: "
    Leer A
    Escribir "Introduce el coeficiente B de la ecuación: "
    Leer B
    Escribir "Introduce el coeficiente C de la ecuación: "
    Leer C
    
    // Cálculo del discriminante
    discriminante <- B^2 - 4*A*C
    
    // Verificar si la ecuación tiene solución real
    Si discriminante >= 0 Entonces
        // Calcular las raíces de la ecuación
        x1 <- (-B + Raiz(discriminante))/(2*A)
        x2 <- (-B - Raiz(discriminante))/(2*A)
        
        // Mostrar resultados
        Escribir "Las soluciones de la ecuación son:"
        Escribir "x1 = ", x1
        Escribir "x2 = ", x2
    SiNo
        // Mostrar mensaje de error si la ecuación no tiene solución real
        Escribir "La ecuación no tiene solución real."
    Fin Si
    
FinAlgoritmo
