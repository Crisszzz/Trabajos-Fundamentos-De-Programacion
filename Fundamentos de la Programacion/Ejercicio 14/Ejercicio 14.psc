Algoritmo sintitulo
	//Descripcion: Resolver una ecuacion de segundo grado
	//Programador:Cristian Vargas
	//Version: 1.0
	//Fecha: 03/03/2023
    // Declaraci�n de variables
    Definir A, B, C, x1, x2, discriminante Como Real
    
    // Lectura de coeficientes de la ecuaci�n
    Escribir "Introduce el coeficiente A de la ecuaci�n: "
    Leer A
    Escribir "Introduce el coeficiente B de la ecuaci�n: "
    Leer B
    Escribir "Introduce el coeficiente C de la ecuaci�n: "
    Leer C
    
    // C�lculo del discriminante
    discriminante <- B^2 - 4*A*C
    
    // Verificar si la ecuaci�n tiene soluci�n real
    Si discriminante >= 0 Entonces
        // Calcular las ra�ces de la ecuaci�n
        x1 <- (-B + Raiz(discriminante))/(2*A)
        x2 <- (-B - Raiz(discriminante))/(2*A)
        
        // Mostrar resultados
        Escribir "Las soluciones de la ecuaci�n son:"
        Escribir "x1 = ", x1
        Escribir "x2 = ", x2
    SiNo
        // Mostrar mensaje de error si la ecuaci�n no tiene soluci�n real
        Escribir "La ecuaci�n no tiene soluci�n real."
    Fin Si
    
FinAlgoritmo
