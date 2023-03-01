num=int(input("Ingrese un numero: "))

facto=1
cont2=0
cont3=0
par=0
impar=0

for i in range (2, num+1, 1):
     
     facto=facto*i   
     
        
     if facto%2!=0:
        cont3+=1
        impar=impar+facto
     else:
         cont2+=1
         par=par+facto


print("El facotrial del numero digitado es: "+str(facto))
print("La cantidad de numeros pares fue "+str(cont2)+" y el acumulado fue "+str(par))
print("La cantidad de numeros impares fue "+str(cont3)+" y el acumulado fue "+str(impar))




