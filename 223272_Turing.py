import tkinter as tk
from tkinter import messagebox

class MaquinaDeTuring:
    def __init__(self):
        self.cinta = []
        self.estado = 'q0'
        self.posicion = 0
        self.resultado = ''

    def configurar_cinta(self, num1, num2):
        self.cinta = list(num1 + 'B' + num2 + 'B')
        self.posicion = 0
        self.estado = 'q0'
        self.resultado = ''

    def ejecutar(self):
        while self.estado != 'q2':
            self.procesar()

    def procesar(self):
        if self.estado == 'q0':
            # num bina lee
            if self.cinta[self.posicion] in ['0', '1']:
                self.posicion += 1  # mov derecha
            else:
                self.estado = 'q1'  # cam estad a suma
        elif self.estado == 'q1':
            # suma
            bit1 = self.cinta[self.posicion - 1] if self.posicion > 0 else '0'
            bit2 = self.cinta[self.posicion + 1] if self.posicion + 1 < len(self.cinta) else '0'
            suma = (int(bit1) + int(bit2)) % 2
            self.resultado += str(suma)
            self.posicion += 2  # pos siguiente
            if self.posicion >= len(self.cinta) or self.cinta[self.posicion] == 'B':
                self.estado = 'q2'
        elif self.estado == 'q2':
            pass

# funciones de la interfaz 
maquina = MaquinaDeTuring()

def validar_numero(numero):
    return all(bit in '01' for bit in numero)

def sumar():
    num1 = entrada_numero1.get().strip()
    num2 = entrada_numero2.get().strip()

    # valida
    if not num1 or not num2:
        messagebox.showerror("Error", "Por favor, introduce ambos nmeros binarios.")
        return

    if not (validar_numero(num1) and validar_numero(num2)):
        messagebox.showerror("Error", "Por favor, introduce numeros binarios válidos (solo 0 y 1).")
        return

    if len(num1) > 10 or len(num2) > 10:
        messagebox.showerror("Error", "Los numeros binarios no deben exceder")
        return

    maquina.configurar_cinta(num1, num2)
    maquina.ejecutar()
    
    resultado_var.set(maquina.resultado) 

ventana = tk.Tk()
ventana.title("Suma de números binarios - Máquina de Turing")
ventana.geometry("400x400")  

fuente = ("Arial", 14)
padding = 10

etiqueta1 = tk.Label(ventana, text="Numero binario 1:", font=fuente)
etiqueta1.pack(pady=padding)

entrada_numero1 = tk.Entry(ventana, width=20, font=fuente)
entrada_numero1.pack(pady=padding)

etiqueta2 = tk.Label(ventana, text="Numero binario 2:", font=fuente)
etiqueta2.pack(pady=padding)

entrada_numero2 = tk.Entry(ventana, width=20, font=fuente)
entrada_numero2.pack(pady=padding)

boton_sumar = tk.Button(ventana, text="sumar", command=sumar, font=fuente, bg="lightblue", padx=10, pady=5)
boton_sumar.pack(pady=padding)

resultado_var = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado_var, font=fuente)
etiqueta_resultado.pack(pady=padding)

ventana.mainloop()
