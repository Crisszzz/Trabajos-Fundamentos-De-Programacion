# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de documentacion//
	# enunciado: leer velocidad en metros sobre segundo y convertirlas a kilometros sobre hora//
	# Version:1.0//
	# Programador: Cristian Vargas//
	# Version: 1.0//
	# area de definicion de variables//
	# variable de entrada que almacena los metros sobre segundo//
	v_metseg = float()
	# variable de salida que almacena los kilometros por hora//
	v_kilhor = float()
	# constante que almacena el factor de conversion de metros sobre segundos a kilometros sobre hora//
	c_faccon = float()
	# inicializacion de variables//
	v_metseg = 0.0
	v_kilhor = 0.0
	c_faccon = 3.6
	print(" digito metro sobre segundo:")
	v_metseg = float(input())
	# area de procesos//
	v_kilhor = v_metseg*c_faccon
	# area de salida//
	print("la conversion es: ",v_kilhor)
	

