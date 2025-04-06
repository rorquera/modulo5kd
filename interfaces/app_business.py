from laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["D:\\desarrollo\\Krakedev\\m5-python\\repositorio git\\interfaces\\img\\asus.webp","D:\\desarrollo\\Krakedev\\m5-python\\repositorio git\\interfaces\\img\\dell.webp","D:\\desarrollo\\Krakedev\\m5-python\\repositorio git\\interfaces\\img\\hp.webp","D:\\desarrollo\\Krakedev\\m5-python\\repositorio git\\interfaces\\img\\huawai.webp"]

        root.title("Laptop Bussines")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca=tk.StringVar()
        ttk.Entry(self.root, textvariable= self.marca).grid(row=0,column=1)

        ttk.Label(self.root, text="Memoria").grid(row=1, column=0)
        self.memoria=tk.StringVar()
        ttk.Entry(self.root, textvariable= self.memoria).grid(row=1,column=1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=2, column=0)
        self.almacenamiento=tk.StringVar()
        ttk.Entry(self.root, textvariable= self.almacenamiento).grid(row=2,column=1)

        ttk.Label(self.root, text="Duracion_bateria").grid(row=3, column=0)
        self.duración_bateria=tk.StringVar()
        ttk.Entry(self.root, textvariable= self.duración_bateria).grid(row=3,column=1)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=5,column=0)

        self.mostrar_laptops=tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2)

        self.canva=tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1,column=3,rowspan=6)

    def agregar_laptop(self):
        nueva_laptop=Laptop_Business(self.marca.get(),self.memoria.get(),self.almacenamiento.get(),self.duración_bateria.get())
        self.laptops.append(nueva_laptop)
        
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aleatorias()

    def mostrar_imagen_aleatorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo  # Previene que la imagen se recolecte por el GC


root = tk.Tk()

app = App(root)
root.mainloop()

