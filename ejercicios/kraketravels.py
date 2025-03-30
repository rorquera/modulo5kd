#KRAKETRAVELS

print("***DESTINOS***")
print("Ecuador")
print("Colombia")
print("Perú")

print("***ZONAS***")
print("urbana")
print("rural")
print("perimetral")

destino=input("Ingrese el destino: ")
zona=input("Ingrese la zona: ")
velocidad=float(input("Ingrese la velocidad: "))

print(f"Destino: {destino} Zona: {zona} Velocidad: {velocidad}")

if destino=="Ecuador":
    if zona=="urbana":
        if velocidad>=10 and velocidad<=50:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")
    elif zona=="rural":
        if velocidad>=51 and velocidad<=70:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")
    elif zona=="perimetral":
        if velocidad>=71 and velocidad<=90:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")

if destino=="Colombia":
    if zona=="urbana":
        if velocidad>=10 and velocidad<=30:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")
    elif zona=="rural":
        if velocidad>=31 and velocidad<=80:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")
    elif zona=="perimetral":
        if velocidad>=81 and velocidad<=100:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")

if destino=="Perú" or destino=="Peru":
    if zona=="urbana":
        if velocidad>=10 and velocidad<=40:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")
    elif zona=="rural":
        if velocidad>=41 and velocidad<=60:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")
    elif zona=="perimetral":
        if velocidad>=61 and velocidad<=120:
            print("Velocidad esta en el límite permitido")
        else:
            print("Velocidad fuera del límite")