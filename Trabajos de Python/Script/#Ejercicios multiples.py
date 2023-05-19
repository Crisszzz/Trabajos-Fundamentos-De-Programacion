#Ejercicios multiples 1
import random
lista=[]
for x in range (0,30):
    Num=random.randint (0,30)
    lista.append(Num)
print(lista)
#Ejercicio 2
cantNum=len(lista)-1
busNum=int(input("Ingrese el numero a encontrar: "))
for x in range (0,20):
    if lista[x]==busNum:
        lista[x]=-1
        print("La lista remplazando el valor a encontrar por -1",lista)

#Ejercicio 5
