print("Ingrese el nombre de los 3 estudiantes ")
est=str(input("Estudiante #1: "))
est2=str(input("Estudiante #2: "))
est3=str(input("Estudiante #3: "))

validar=0

while validar==0:
    print("\nDigite 1 para ingresar las notas de "+str(est))
    print("Digite 2 para ingresar las notas de "+str(est2))
    print("Digite 3 para ingresar las notas de "+str(est3))
    num=int(input())
    print("")

    match num: 
        case 1:
            print("Ingrese las notas de "+str(est))
            nota=float(input("Nota #1: "))
            nota2=float(input("Nota #2: "))
            nota3=float(input("Nota #3: "))

            total=(nota+nota2+nota3)/3

            print("Desea continar? 1 para SI 0 para NO")
            z=int(input())
            if z==0:
                break

        case 2:
            print("Ingrese las notas de "+str(est2))
            notae=float(input("Nota #1: "))
            notae2=float(input("Nota #2: "))
            notae3=float(input("Nota #3: "))

            totale2=(notae+notae2+notae3)/3

            print("Desea continar? 1 para SI 0 para NO")
            z=int(input())
            if z==0:
                break

        case 3:
            print("Ingrese las notas de "+str(est3))
            notaes=float(input("Nota #1: "))
            notaes2=float(input("Nota #2: "))
            notaes3=float(input("Nota #3: "))
            
            totale3=(notaes+notaes2+notaes3)/3

            print("Desea continar? 1 para SI 0 para NO")
            z=int(input())
            if z==0:
                break

if total>=2 :
    print("\nEl estudiante "+est+" aprobo")
else: 
    print("\nEl estudiante "+est+" reprobo")

if totale2>=2 :
    print("\nEl estudiante "+est2+" aprobo")
else: 
    print("\nEl estudiante "+est2+" reprobo")

if totale3>=2 :
    print("\nEl estudiante "+est3+" aprobo")
else: 
    print("\nEl estudiante "+est3+" reprobo")


promedio=(total+totale2+totale3)/3

print("\nEl estudiante "+est+" saco "+str(total))
print("El estudiante "+est2+" saco "+str(totale2))
print("El estudiante "+est3+" saco "+str(totale3))
print("\nEl promedio del curso fue de "+str(promedio))







