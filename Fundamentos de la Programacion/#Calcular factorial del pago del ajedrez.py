#Calcular factorial del pago del ajedrez
fact=1
valPesoDol=4500
for x in range (1,64):
         fact = (fact * x)
#En dolar
FacValDol= fact * valPesoDol
print("El valor es",FacValDol)



#Tabla de Multiplicar 
mdo=1
mdr=10
for x in range (10):
        mdo=x+1
        print("Tabla", mdo)
        for x in range(1,mdr+1):
                res= x*mdo
                print(mdo,"*",x,"=",res)