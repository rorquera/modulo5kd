from laptop import Laptop

# funcion __dict__ permite reservar el contenido del objeto

laptop_pepe=Laptop("dell", "i7", 32, costo=500)
laptop_maria=Laptop("dell", "i7", 32)
print(laptop_pepe.__dict__)

print("***Llamada al metodo estatico***")
print(Laptop.comparar_costo(laptop_pepe,laptop_maria))

print("***Llamada al metodo de clase***")
# asus_laptop=Laptop.asus_laptop()
# print(asus_laptop.__dict__)

for numero in range(1,1001):
    asus_laptop=Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)