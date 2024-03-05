import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib_venn import venn2

class Conjunto:
    def __init__(self, elementos):
        self.elementos = elementos

    def union(self, otro_conjunto):
        """
        Función para calcular la unión de dos conjuntos.
        """
        # Unión de los conjuntos
        return Conjunto(list(set(self.elementos + otro_conjunto.elementos)))

    def interseccion(self, otro_conjunto):
        """
        Función para calcular la intersección de dos conjuntos.
        """
        # Intersección de los conjuntos
        return Conjunto([elemento for elemento in self.elementos if elemento in otro_conjunto.elementos])

    def diferencia(self, otro_conjunto):
        """
        Función para calcular la diferencia entre dos conjuntos (conjunto1 - conjunto2).
        """
        # Diferencia entre los conjuntos
        return Conjunto([elemento for elemento in self.elementos if elemento not in otro_conjunto.elementos])

    def complemento(self, universo):
        """
        Función para calcular el complemento de un conjunto con respecto a un universo dado.
        """
        # Complemento del conjunto
        return Conjunto([elemento for elemento in universo.elementos if elemento not in self.elementos])

    def cardinalidad(self):
        """
        Función para calcular la cardinalidad de un conjunto.
        """
        # Cardinalidad del conjunto
        return len(self.elementos)

    def es_subconjunto(self, otro_conjunto):
        """
        Función para verificar si conjunto1 es subconjunto de conjunto2.
        """
        # Verificar si conjunto1 es subconjunto de conjunto2
        return all(elemento in otro_conjunto.elementos for elemento in self.elementos)

    def son_disjuntos(self, otro_conjunto):
        """
        Función para verificar si dos conjuntos son disjuntos.
        """
        # Verificar si los conjuntos son disjuntos
        return len(self.interseccion(otro_conjunto).elementos) == 0

    def mostrar_diagrama_venn(self, otro_conjunto):
        """
        Función para representar los conjuntos en un diagrama de Venn.
        """
        # Implementación de la representación en diagrama de Venn
        plt.figure()
        venn2(subsets=(len(self.elementos), len(otro_conjunto.elementos), len(self.interseccion(otro_conjunto).elementos)),
                set_labels=('Conjunto 1', 'Conjunto 2'))
        plt.title("Diagrama de Venn")
        plt.show()

# Función para mostrar un reporte en una ventana emergente
def mostrar_reporte(conjunto1, conjunto2):

    reporte = ""
    reporte += "Universo: {}\n".format(universo.elementos)
    reporte += "Conjunto 1: {}\n".format(conjunto1.elementos)
    reporte += "Conjunto 2: {}\n".format(conjunto2.elementos)
    reporte += "Unión: {}\n".format(conjunto1.union(conjunto2).elementos)
    reporte += "Intersección: {}\n".format(conjunto1.interseccion(conjunto2).elementos)
    reporte += "Diferencia del conjunto 1  - conjunto 2: {}\n".format(conjunto1.diferencia(conjunto2).elementos)
    reporte += "Diferencia del conjunto 2 - conjunto 1: {}\n".format(conjunto2.diferencia(conjunto1).elementos)
    reporte += "Complemento del conjunto 1 respecto al universo: {}\n".format(conjunto1.complemento( universo ).elementos)
    reporte += "Cardinalidad del conjunto 1: {}\n".format(conjunto1.cardinalidad())
    reporte += "¿Es el conjunto 1 subconjunto del conjunto 2?: {}\n"
    reporte += "¿Son disjuntos los conjuntos 1 y 2?: {}\n".format(conjunto1.son_disjuntos(conjunto2))
    return reporte

# Crear instancias de conjuntos
universo = Conjunto([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
conjunto1 = Conjunto([1, 2, 3])
conjunto2 = Conjunto([1, 2, 3, 5, 6, 7, 8, 9])

# Mostrar reporte en una ventana emergente
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal
messagebox.showinfo("Reporte de Operaciones entre Conjuntos", mostrar_reporte(conjunto1, conjunto2))

# Mostrar el diagrama de Venn
conjunto1.mostrar_diagrama_venn(conjunto2)
