# Pedimos al usuario el número del cual queremos generar la tabla de multiplicar
numero = int(input("Ingresa el número del cual deseas ver la tabla de multiplicar: "))

# Iteramos del 1 al 10 para imprimir la tabla de multiplicar del número ingresado
for i in range(1, 11):
    # Multiplicamos el número ingresado por el número de la iteración actual
    resultado = numero * i
    
 # Imprimimos el resultado de la multiplicación
    print(numero, "x", i, "=", resultado)
