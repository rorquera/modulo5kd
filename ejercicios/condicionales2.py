import random

aleatorio=random.randint(1,9)
aleatorio_dos=random.randint(1,9)

if aleatorio==4:
    print("Te ganaste un chupete")
elif aleatorio==8:
    print("Te ganaste un balon")
elif aleatorio==3 and aleatorio_dos==7:
    print("Te ganaste un tv")
else:
    print("persiste!!!")
