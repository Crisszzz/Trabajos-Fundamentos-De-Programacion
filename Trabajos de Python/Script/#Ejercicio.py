#Ejercicio
contador = 0
Num = int(input("Digite un numero entero: "))
while Num > 0:
    Num = int(input("Digite numero entero: "))
    contador= contador+1
    if Num <= 0:
        print("Fin del proceso")
print("Usted digito un total de",contador,"numeros")



#Ejercicio 2
sueldos=[]
for x in range(5):
    valor=int(input("ingrese sueldos: "))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
           aux=sueldos[x]
           sueldos[x]=sueldos[x+1]
           sueldos[x+1]=aux

print("Lista con el ultimo elemnto ordenado")
print(sueldos)