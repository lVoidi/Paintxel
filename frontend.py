import tkinter as tk

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



        #Creacion de todos los botones
        self.blanco = tk.Button(self, bg ="#ffffff", width=10, height=3)
        self.blanco.grid(column=3, row=1)
        self.rosado = tk.Button(self, bg ="#ffaaaa", width=10, height=3)
        self.rosado.grid(column=3, row=2)
        self.verde = tk.Button(self, bg ="#aaffaa", width=10, height=3)
        self.btn3.grid(column=3, row=3)
        self.btn4 = tk.Button(self, bg ="#aaaaff", width=10, height=3)
        self.btn4.grid(column=3, row=4)
        self.btn5 = tk.Button(self, bg ="#00ff00", width=10, height=3)
        self.btn5.grid(column=3, row=5)
        self.btn6 = tk.Button(self, bg ="#ff00ff", width=10, height=3)
        self.btn6.grid(column=3, row=6)
        self.btn7 = tk.Button(self, bg ="#ff0000", width=10, height=3)
        self.btn7.grid(column=3, row=7)
        self.btn8 = tk.Button(self, bg ="#0000ff", width=10, height=3)
        self.btn8.grid(column=3, row=8)
        self.btn9 = tk.Button(self, bg ="#000077", width=10, height=3)
        self.btn9.grid(column=3, row=9)
        self.btn10 = tk.Button(self, bg ="#000000", width=10, height=3)
        self.btn10.grid(column=3, row=10)
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

        for i in range(24):
            for j in range(24):
                self.canvas.create_rectangle(i*25, j *25, i*25+25, j*25+25)

app = FrontApp()
app.mainloop()
