lista=[]
for x in range(5):
    valor=int(input("Ingrese un valor entero: "))
    lista.append(valor)
print(lista)


valor=int(input("Ingrese valor ( 0 para finalizar): "))
while valor!=0:
   lista.append(valor)
   valor=int(input("Ingrese valor ( 0 para finalizar): "))
print("El tamaño de la lista: ")
print(len(lista))

mayor=lista[0]
for x in range(1.5):
    if lista[x]>mayor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)