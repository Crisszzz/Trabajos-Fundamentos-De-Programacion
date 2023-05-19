# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripcion: hallar la aceleracion de un camion//
	# Version:1.0//
	# Programador:Cristian Vargas//
	# ultima modificacion: 25/02/2023
	# area de definicion de variables//
	# variable de entrada que almacena la velocidad inicial//
	v_inicial_metseg = float()
	# variable de entrada que almacena la velocidad final//
	v_final_metseg = float()
	# variable de entrada que almacena el tiempo en el que se da la aceleracion//
	tiempo_s = float()
	# inicializacion de variables//
	v_inicial_metseg = 20
	v_final_metseg = 25
	tiempo_s = 5
	# Area de procesos//
	aceleracion_metseg = (v_final_metseg-v_inicial_metseg)/tiempo_s
	# area de salida//
	print("la aceleracion es: ",aceleracion_metseg)

