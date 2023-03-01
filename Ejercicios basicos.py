print("Digite un numero: ")
numero = int (input())


if numero > 0:
    print("El numero es positivo")
elif numero==0:
    print("el numero es neutro")
else:
    print("el numero es negativos")

print("\n")

# Ejercicio de while #
print("\n")

while True:
    print("Digite la letra A para actualizar sistema")
    print("Digite la letra E para eleminar catalogo")
    print("Digite la letra C paa crear producti")
    print("Digite la letra S para salir del programa")
    letra=str(input())
    if letra=='S' or letra=='s':
        print("Finalizo con exito")
        break
    elif letra=='a' or letra=='A':
        print("Se ha actualizao el sistema") 
        break
    elif letra=='e' or letra=='E':
        print("Se ha eliminado el catalogo")
        break
    elif letra=='c' or letra=='C':
        print("Se creo un producto")
        break   
    else:
        print("sigue dentro del proceso del do while \n")


print("El do-while ha finalizado...")
print("\n")

# Ejercicio while #
print("\n")
num=1

while num!=0:
    print("digite un numero")
    num=int(input())
    if num%2==0:
        print("El numero es par")
        break
    else:
        print("El numero es impar")
        break
print("finalizo el programa")
print("\n")

# Ejercicio for #
print("\n")
suma=0
print("Digite la cantidad de numeros posibles")
cantidad = int(input())

for i in range (0, cantidad, 1):
    print("Digite el numero "+str(i+1)+": ")
    numero=int(input())
    suma=suma+numero
print("la sumatoria total es: "+str(suma))


# Ejercicio del switch(match) #

print("Digite un numero del 1 al 12")
num=int(input())

match num: 
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4: 
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
    case 13:
        print("Feliz año")
        print("Enero")


 