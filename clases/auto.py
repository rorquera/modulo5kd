class Auto:
    def __init__(self,marca, modelo, anio, kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Kilometraje {self.kilometraje}")
        
    def actualizar_kilometraje(self,kilometraje):
        if kilometraje>self.kilometraje:
            self.kilometraje=kilometraje
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros>0:
            self.kilometraje=self.kilometraje+kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva")

    def estado_auto(self):
        if self.kilometraje<20000:
            print("Estoy como nuevo")
        elif self.kilometraje>20000 and self.kilometraje<100000:
            print("Ya estoy usado")
        elif self.kilometraje>100000:
            print("¡Ya déjame descansar por favor!")

auto_nuevo=Auto("wolsvagen","amarok",2024)
auto_nuevo.mostrar_informacion()
auto_nuevo.actualizar_kilometraje(10000)
auto_nuevo.actualizar_kilometraje(-1025)
auto_nuevo.realizar_viaje(20458)
auto_nuevo.realizar_viaje(-20444)
auto_nuevo.estado_auto()
auto_nuevo.mostrar_informacion()