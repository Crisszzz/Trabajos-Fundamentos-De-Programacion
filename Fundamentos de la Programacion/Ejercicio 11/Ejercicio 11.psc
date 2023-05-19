Algoritmo Ejercicio11
	// Área de documentación
	// Enunciado: determinar la cantidad total a pagar por una llamada telefónica
	// Versión: 1.0
	// Desarrollado por: Cristian Vargas
	// Fecha: 03/03/23
	
	// Área de definición de variables
	Definir v_nPas Como Entero;
	Definir v_prec Como Real;
	
	// Inicialización de variables
	
	// Área de entradas
    Escribir "Ingrese el número de pasos hablados por teléfono: ";
    Leer v_nPas;
	
	// Área de procesos y de salidas
	Si v_nPas > 0 Entonces
        Si v_nPas < 5 Entonces
            v_prec = 10
        Sino
            v_prec = (v_nPas - 5) * 5 + 10
        FinSi
        Escribir "El costo total de la llamada es: ", v_prec, " céntimos";
    Sino
        Escribir "Error: el número de pasos debe ser mayor que cero";
    FinSi 

FinAlgoritmo
