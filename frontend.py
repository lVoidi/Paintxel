from threading import Thread
from backend import PaintxelCanvas
import tkinter as tk

class FrontApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg = "#ffffff")
        self.geometry("765x750")
        self.resizable(False, False)
        self.selected_color = "#ffffff"
        self.painting = False
        self.canvas_top = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        self.canvas_top.grid(column=0, row=0, columnspan=4,sticky="nsew")
        self.canvas_bottom = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        self.canvas_bottom.grid(column=0, row=11, columnspan=4,sticky="nsew")
        
        
        self.colors = ["#ffffff", "#ffaaaa", "#aaffaa", "#aaaaff", "#00ff00", "#ff00ff", "#ff0000", "#0000ff", "#000077", "#000000"]

        #Creacion de todos los botones de colores
        self.blanco = tk.Button(self, bg ="#ffffff", width=10, height=3, command=lambda: self.set_color(0))
        self.blanco.grid(column=3, row=1)
        self.rosado = tk.Button(self, bg ="#ffaaaa", width=10, height=3, command=lambda: self.set_color(1))
        self.rosado.grid(column=3, row=2)
        self.verdeclaro = tk.Button(self, bg ="#aaffaa", width=10, height=3, command=lambda: self.set_color(2))
        self.verdeclaro.grid(column=3, row=3)
        self.celeste = tk.Button(self, bg ="#aaaaff", width=10, height=3, command=lambda: self.set_color(3))
        self.celeste.grid(column=3, row=4)
        self.verde = tk.Button(self, bg ="#00ff00", width=10, height=3, command=lambda: self.set_color(4))
        self.verde.grid(column=3, row=5)
        self.fucsia = tk.Button(self, bg ="#ff00ff", width=10, height=3, command=lambda: self.set_color(5))
        self.fucsia.grid(column=3, row=6)
        self.rojo = tk.Button(self, bg ="#ff0000", width=10, height=3, command=lambda: self.set_color(6))
        self.rojo.grid(column=3, row=7)
        self.azul = tk.Button(self, bg ="#0000ff", width=10, height=3, command=lambda: self.set_color(7))
        self.azul.grid(column=3, row=8)
        self.azuloscuro = tk.Button(self, bg ="#000077", width=10, height=3, command=lambda: self.set_color(8))
        self.azuloscuro.grid(column=3, row=9)
        self.negro = tk.Button(self, bg ="#000000", width=10, height=3, command=lambda: self.set_color(9))
        self.negro.grid(column=3, row=10)

        #Botones para opciones
        self.btn11 = tk.Button(self, text = "Rotar a derecha", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.on_rotate_right)
        self.btn11.grid(column=0, row=1)
        self.btn12 = tk.Button(self, text = "Rotar a la izquierda", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.on_rotate_left)
        self.btn12.grid(column=0, row=2)
        self.btn13 = tk.Button(self, text = "Reflexión horizontal", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.on_horizontal_reflex)
        self.btn13.grid(column=0, row=3)
        self.btn14 = tk.Button(self, text = "Reflexión vertical", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.on_vertical_reflex)
        self.btn14.grid(column=0, row=4)
        self.btn15 = tk.Button(self, text = "Alto contraste", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.on_high_contrast)
        self.btn15.grid(column=0, row=5)
        self.btn16 = tk.Button(self, text = "Invertir", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.on_invert)
        self.btn16.grid(column=0, row=6)
        self.btn17 = tk.Button(self, text = "Limpiar pantalla", bg ="#000000", fg="#ffffff", width=10, height=3, command=self.clean_screen)
        self.btn17.grid(column=0, row=7)
        self.btn18 = tk.Button(self, text = "Cuadrado", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn18.grid(column=0, row=8)
        self.btn19 = tk.Button(self, text = "Triángulo", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn19.grid(column=0, row=9)
        self.btn20 = tk.Button(self, text = "Zoom in", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn20.grid(column=0, row=10)

        self.btn21 = tk.Button(self, text = "Zoom out", bg ="#000000", fg="#ffffff", width=10, height=3)
        self.btn21.grid(column=0, row=11)


        self.canvas = tk.Canvas(self, bg= "#ffffff", width=600, height=600)
        self.canvas.grid(column=1, row=1, rowspan= 10, sticky="nsew")
        
        self.mouse_x = 0 
        self.mouse_y = 0
        
        self.rectangles = [[0] * 24 for _ in range(24)]
        self.program_matrix = PaintxelCanvas([[0] * 24 for _ in range(24)])
        self.screen = self.program_matrix.screen
        for i in range(24):
            for j in range(24):
                rect = self.canvas.create_rectangle(i*25, j *25, i*25+25, j*25+25, fill="#ffffff")
                self.rectangles[i][j] = rect
        
        self.canvas.bind("<ButtonPress-1>", self.create_painting_thread)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)


    def set_color(self, color):
        self.selected_color = color
    

    def on_rotate_right(self):
        self.program_matrix.rotate_right()
        self.update_canvas()


    def on_rotate_left(self):
        self.program_matrix.rotate_left()
        self.update_canvas()

        
    def on_horizontal_reflex(self):
        self.program_matrix.horizontal_reflex()
        self.update_canvas()

    def on_vertical_reflex(self):
        self.program_matrix.vertical_reflex()
        self.update_canvas()


    def on_high_contrast(self):
        self.program_matrix.high_contrast()
        self.update_canvas()
    

    def on_invert(self):
        self.program_matrix.invert()
        self.update_canvas()
    

    def clean_screen(self):
        self.screen = [[0]*24 for _ in range(24)]
        self.program_matrix.screen = self.screen
        self.update_canvas()


    def on_mouse_motion(self, event):
        self.mouse_x, self.mouse_y = event.x // 25, event.y // 25


    def create_painting_thread(self, event):
        thread = Thread(target=self.paint_square, args=(event,))
        thread.start()

    
    def paint_square(self, event):
        self.painting = True
        self.mouse_x, self.mouse_y = event.x // 25, event.y // 25
        while self.painting:
            self.screen[self.mouse_y][self.mouse_x] = self.selected_color
            self.canvas.itemconfig(
                self.rectangles[self.mouse_x][self.mouse_y],
                fill=self.colors[self.selected_color]
            )


    def on_button_release(self, _):
        self.painting = False
        self.screen = self.program_matrix.screen
        print(str(self.program_matrix))


    def update_canvas(self):
        self.screen = self.program_matrix.screen
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles[0])):
                self.canvas.itemconfig(
                    self.rectangles[i][j], 
                    fill=self.colors[self.screen[j][i]]
                )
                

app = FrontApp()
app.mainloop()
