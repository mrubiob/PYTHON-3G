sueldo=int(input("Ingrese su sueldo mensual :"))
antiguedad=int(input("Ingrese la cantidad de años que trabaja en la EA :"))
mes=int(input("Ingrese mes actual 1-12 : "))
if sueldo > 750000 and antiguedad > 5:
    sueldo += 70000
elif (sueldo <=750000):
    sueldo += 100000
else:
    print("no le corresponde bonificación por sueldo y antiguedad")

if mes == 12:
    hijos=int(input("Ingrese la cantidad de hijos :"))
    sueldo += hijos*10000
print("Este mes, ud recibirá un sueldo de :", sueldo)