from ejercicios_generales.vehiculo import Vehiculo
from ejercicios_generales.moto import Moto
from ejercicios_generales.auto import Auto

moto=Moto("Kawasaki","Ninja",2025,"Deportiva")
auto=Auto("Kawasaki","Ninja",2025,5)

print("**Descripcion Moto**")
print(moto.descripcion())
print("**Descripcion Auto**")
print(auto.descripcion())
print("**Polimorfismo**")

vehiculos=[moto,auto]
for vehiculo in vehiculos:
    print(vehiculo.descripcion())