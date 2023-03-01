

print("Digite 1 para calcular el area y perimetro de un triangulo")
print("Digite 2 para calcular el area y perimetro de un cuadrado")
print("Digite 3 para calcular el area y perimetro de un circulo")
num=int(input())


match num: 
    case 1:
        print("\nDigite la base y la altura")
        b=float(input("B:"))
        h=float(input("H:"))
        print("Ingresa los otros dos lados del triangulo")
        l=float(input("Lado n1: "))
        l2=float(input("Lado n2: "))
        area=(b*h)/2
        perimetro=l+l2+b

        print("\nEl area del triangulo es "+str(area)+" y el perimetro es "+str(perimetro))
        
    case 2:
        print("\nDigite el valor de un lado del cuadrado")
        l=float(input("lado: "))
        area=l*l
        perimetro=l*4    
        
        print("\nEl area del cuadrado es "+str(area)+" y el perimetro es "+str(perimetro))

    case 3:
        print("\nDigite el diametro del circulo")
        d=float(input("Diametro: "))
        r=d/2
        area=3.1416*(r**2)
        perimetro=3.1416*r
        print("\nEl area del circulo es "+str(area)+" y el perimetro es "+str(perimetro))

        


