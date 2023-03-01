infinito=0
pl=0
pm=0
pw=0
pj=0
pv=0
ps=0
pd=0
dl=0
dm=0
dw=0
dj=0
dv=0
ds=0
dd=0
x=0
num=0
tota=0
promedio=0

while infinito==0:
    print("")
    print("Digite 1 para lunes")
    print("Digite 2 para Martes")
    print("Digite 3 para Miercoles")
    print("Digite 4 para Jueves")
    print("Digite 5 para Viernes")
    print("Digite 6 para Sabado")
    print("Digite 7 para Domingo")
    num=int(input())

    match num: 
        case 1:
            print("\nCuantos productos se vendieron?")
            pl=int(input())
            print("\nCuanto dinero se recaudo en total?")
            dl=float(input())

            print("Desea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break

        case 2:
            print("\nCuantos productos se vendieron?")
            pm=int(input())
            print("\nCuanto dinero se recaudo en total?")
            dm=float(input())  

            print("\nDesea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break

        case 3:
            print("\nCuantos productos se vendieron?")
            pw=int(input())
            print("\nCuanto dinero se recaudo en total?")
            dw=float(input())

            print("\nDesea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break

        case 4:
            print("\nCuantos productos se vendieron?")
            pj=int(input())
            print("\nCuanto dinero se recaudo en total?")
            dj=float(input())         

            print("\nDesea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break

        case 5:
            print("\nCuantos productos se vendieron?")
            pv=int(input())
            print("\nCuanto dinero se recaudo en total?")
            dv=float(input())

            print("\nDesea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break
        case 6:
            print("\nCuantos productos se vendieron?")
            ps=int(input())
            print("\nCuanto dinero se recaudo en total?")
            ds=float(input())

            print("\nDesea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break

        case 7:
            print("\nCuantos productos se vendieron?")
            pd=int(input())
            print("\nCuanto dinero se recaudo en total?")
            dd=float(input())

            print("\nDesea continuar? 1 para SI 0 para NO")
            x=int(input())        
            if x==0:
                break

    
total=pl+pm+pw+pj+pv+ps+pd
promedio=(dl+dm+dw+dj+dv+ds+dd)/7

print("\nEl total de ventas fue de: "+str(total))
print("El promedio de ventas fue de: "+str(promedio))



