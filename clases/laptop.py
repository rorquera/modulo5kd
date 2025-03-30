class Laptop:
    # declaracion de constructor: siempre con __init__(self)
    # self es el primer parametro que debe tener el contructor y representa una autoreferencia a la instancia
    # self se usa para asignar los parametros a los atributos de la clase
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto

# funcion __dict__ permite reservar el contenido del objeto

Laptop_pepe=Laptop("dell", "i7", 32)
print(Laptop_pepe.__dict__)