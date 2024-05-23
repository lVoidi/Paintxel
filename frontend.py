import tkinter as tk
from tkinter.colorchooser import askcolor

class FrontApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg = "#ffffff")
        self.geometry("765x750")
        self.resizable(False, False)

        self.canvas_top = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        self.canvas_top.grid(column=0, row=0, columnspan=4,sticky="nsew")
        self.canvas_bottom = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        self.canvas_bottom.grid(column=0, row=11, columnspan=4,sticky="nsew")



        #Creacion de todos los botones de colores
        self.blanco = tk.Button(self, bg ="#ffffff", width=10, height=3)
        self.blanco.grid(column=3, row=1)
        self.blanco.config(command=lambda: self.set_color("#ffffff"))
        self.rosado = tk.Button(self, bg ="#ffaaaa", width=10, height=3)
        self.rosado.grid(column=3, row=2)
        self.rosado.config(command=lambda: self.set_color("#ffaaaa"))
        self.verdeclaro = tk.Button(self, bg ="#aaffaa", width=10, height=3)
        self.verdeclaro.grid(column=3, row=3)
        self.verdeclaro.config(command=lambda: self.set_color("#aaffaa"))
        self.celeste = tk.Button(self, bg ="#aaaaff", width=10, height=3)
        self.celeste.grid(column=3, row=4)
        self.celeste.config(command=lambda: self.set_color("#aaaaff"))
        self.verde = tk.Button(self, bg ="#00ff00", width=10, height=3)
        self.verde.grid(column=3, row=5)
        self.verde.config(command=lambda: self.set_color("#00ff00"))
        self.fucsia = tk.Button(self, bg ="#ff00ff", width=10, height=3)
        self.fucsia.grid(column=3, row=6)
        self.fucsia.config(command=lambda: self.set_color("#ff00ff"))
        self.rojo = tk.Button(self, bg ="#ff0000", width=10, height=3)
        self.rojo.grid(column=3, row=7)
        self.rojo.config(command=lambda: self.set_color("#ff0000"))
        self.azul = tk.Button(self, bg ="#0000ff", width=10, height=3)
        self.azul.grid(column=3, row=8)
        self.azul.config(command=lambda: self.set_color("#0000ff"))
        self.azuloscuro = tk.Button(self, bg ="#000077", width=10, height=3)
        self.azuloscuro.grid(column=3, row=9)
        self.azuloscuro.config(command=lambda: self.set_color("#000077"))
        self.negro = tk.Button(self, bg ="#000000", width=10, height=3)
        self.negro.grid(column=3, row=10)
        self.negro.config(command=lambda: self.set_color("#000000"))



        #Botones para opciones
        self.btn11 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn11.grid(column=0, row=1)
        self.btn12 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn12.grid(column=0, row=2)
        self.btn13 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn13.grid(column=0, row=3)
        self.btn14 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn14.grid(column=0, row=4)
        self.btn15 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn15.grid(column=0, row=5)
        self.btn16 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn16.grid(column=0, row=6)
        self.btn17 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn17.grid(column=0, row=7)
        self.btn18 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn18.grid(column=0, row=8)
        self.btn19 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn19.grid(column=0, row=9)
        self.btn20 = tk.Button(self, text = "Prueba", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn20.grid(column=0, row=10)




        self.canvas = tk.Canvas(self, bg= "#ffffff", width=600, height=600)
        self.canvas.grid(column=1, row=1, rowspan= 10, sticky="nsew")


        self.color_matrix = [[None] * 24 for _ in range(24)]
        for i in range(24):
            for j in range(24):
                self.color_matrix[i][j] = "#ffffff"
                self.canvas.create_rectangle(i*25, j *25, i*25+25, j*25+25, fill="#ffffff")
        
        self.canvas.bind("<Button-1>", self.paint_square)


    def set_color(self, color):
       self.selected_color = color


    def paint_square(self, event):
        x, y = event.x // 25, event.y // 25
        self.color_matrix[x][y] = self.selected_color
        self.canvas.create_rectangle(x * 25, y * 25, x * 25 + 25, y * 25 + 25, fill=self.selected_color)

app = FrontApp()
app.mainloop()
