from auto import Auto

print("***Llamada al metodo de clase***")
auto_nuevo=Auto.auto_nuevo()
print(f"Auto nuevo: {auto_nuevo.marca} {auto_nuevo.anio}")
auto_nuevo_modelo=Auto.nuevo_modelo()
print(f"Nuevo modelo: {auto_nuevo_modelo.modelo}")

print("***Llamada al metodo estatico***")
respuesta = Auto.comparar_kilometraje(auto_nuevo, auto_nuevo_modelo)
print(f"{respuesta}")
Auto.cambiar_marca(auto_nuevo,"Nissan")

