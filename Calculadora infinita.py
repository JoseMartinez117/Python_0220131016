infinito=0

while infinito==0:
    print("Digite 1 para sumar")
    print("Digite 2 para restar")
    print("Digite 3 para multiplicar")
    print("Digite 4 para dividr")
    num=int(input())

    match num: 
        case 1:
            print("Ingrese los valores a sumar")
            a=float(input("A: "))
            b=float(input("B: "))
            r=a+b
            print("\nEl resultado de la suma es "+str(r))
            
            print("\n desea continar? 1 para SI 0 para NO")
            x=int(input())

            if x==0:
                break

        case 2:
            print("Ingrese los valores a restar") 
            a=float(input("A: "))
            b=float(input("B: "))
            r=a-b
            print("\nEl resultado de la resta es "+str(r))

            print("\n desea continar? 1 para SI 0 para NO")
            x=int(input())
            if x==0:
                break

        case 3:
            print("Ingrese los valores a multiplicar")
            a=float(input("A: "))
            b=float(input("B: "))
            r=a*b
            print("\nEl resultado de la multiplicacion es "+str(r))
            
            print("\n desea continar? 1 para SI 0 para NO")
            x=int(input())
            if x==0:
                break

        case 4:
            print("Ingrese los valores a dividir")
            a=float(input("A: "))
            b=float(input("B: "))
            if b!=0:
                r=a*b
                print("\nEl resultado de la multiplicacion es "+str(r))
            else:
                print("\nMathError")
            
            print("\nDesea continar? 1 para SI 0 para NO")
            x=int(input())
            if x==0:
                break    








