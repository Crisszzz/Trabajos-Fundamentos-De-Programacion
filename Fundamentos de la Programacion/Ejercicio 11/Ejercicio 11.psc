Algoritmo Ejercicio11
	// �rea de documentaci�n
	// Enunciado: determinar la cantidad total a pagar por una llamada telef�nica
	// Versi�n: 1.0
	// Desarrollado por: Cristian Vargas
	// Fecha: 03/03/23
	
	// �rea de definici�n de variables
	Definir v_nPas Como Entero;
	Definir v_prec Como Real;
	
	// Inicializaci�n de variables
	
	// �rea de entradas
    Escribir "Ingrese el n�mero de pasos hablados por tel�fono: ";
    Leer v_nPas;
	
	// �rea de procesos y de salidas
	Si v_nPas > 0 Entonces
        Si v_nPas < 5 Entonces
            v_prec = 10
        Sino
            v_prec = (v_nPas - 5) * 5 + 10
        FinSi
        Escribir "El costo total de la llamada es: ", v_prec, " c�ntimos";
    Sino
        Escribir "Error: el n�mero de pasos debe ser mayor que cero";
    FinSi 

FinAlgoritmo
