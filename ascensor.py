piso=int(input("Ingrese el piso en el que se encuentra :"))
asc1=int(input("Ingrese el piso en el que se encuentra el ascensor 1 :"))
asc2=int(input("Ingrese el piso en el que se encuentra el ascensor 2 : "))
dif1=piso-asc1
dif2=piso-asc2

if abs(dif1) < abs(dif2):
    print("El ascensor N° 1 lo viene a buscar")
elif (abs(dif2) < abs(dif1)):
    print("El ascensor N°2 lo viene a buscar")
else:
    print("Se encuentra ubicado en el mismo piso de ambos ascensores, el sistema asignará a uno")