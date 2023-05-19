import random
lista=[]
for x in range (0,30):
    Num=random.randint (0,30)
    lista.append(Num)
print(lista)
cantNum=len(lista)-1
contador=0
numCont=int(input("Ingrese numero a buscar: "))
for x in range (0,30):
    if lista[x]==numCont:
        contador=contador+1
print("El numero se repite",contador)
#Lista ordenada sin duplicar
NumsinRep = set(lista)
listOrd = sorted(list(NumsinRep))
print("Lista ordenada sin duplicados:", listOrd)
#Lista ordenada y repitiendo el numero sobre si misma
listOrdRep = sorted(list(lista))
print("Lista ordenada repitiendo el valor",listOrdRep)
#Lista de veces que se repite
ListRep = listOrdRep.count
print(ListRep)
