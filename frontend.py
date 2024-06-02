from tkinter import filedialog as fd
from backend import PaintxelCanvas
from tkinter import messagebox
from threading import Thread
import tkinter as tk


class FrontApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="#ffffff")
        self.geometry("765x790")
        self.resizable(False, False)
        self.selected_color = 0
        self.painting = False
        self.do_draw_rectangle = False
        self.do_draw_circle = False
        self.canvas_top = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        self.canvas_top.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.canvas_bottom = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        self.canvas_bottom.grid(column=0, row=11, columnspan=4, sticky="nsew")
        self.circle_matrix = []
        self.cover = 0
        self.zoomed = []
        self.zoomed_canvas = None
        self.colors = [
            "#ffffff",
            "#ffaaaa",
            "#aaffaa",
            "#aaaaff",
            "#00ff00",
            "#ff00ff",
            "#ff0000",
            "#0000ff",
            "#000077",
            "#000000",
        ]

        # Creacion de todos los botones de colores
        self.blanco = tk.Button(
            self, bg="#ffffff", width=10, height=3, command=lambda: self.set_color(0)
        )
        self.blanco.grid(column=3, row=1)
        self.rosado = tk.Button(
            self, bg="#ffaaaa", width=10, height=3, command=lambda: self.set_color(1)
        )
        self.rosado.grid(column=3, row=2)
        self.verdeclaro = tk.Button(
            self, bg="#aaffaa", width=10, height=3, command=lambda: self.set_color(2)
        )
        self.verdeclaro.grid(column=3, row=3)
        self.celeste = tk.Button(
            self, bg="#aaaaff", width=10, height=3, command=lambda: self.set_color(3)
        )
        self.celeste.grid(column=3, row=4)
        self.verde = tk.Button(
            self, bg="#00ff00", width=10, height=3, command=lambda: self.set_color(4)
        )
        self.verde.grid(column=3, row=5)
        self.fucsia = tk.Button(
            self, bg="#ff00ff", width=10, height=3, command=lambda: self.set_color(5)
        )
        self.fucsia.grid(column=3, row=6)
        self.rojo = tk.Button(
            self, bg="#ff0000", width=10, height=3, command=lambda: self.set_color(6)
        )
        self.rojo.grid(column=3, row=7)
        self.azul = tk.Button(
            self, bg="#0000ff", width=10, height=3, command=lambda: self.set_color(7)
        )
        self.azul.grid(column=3, row=8)
        self.azuloscuro = tk.Button(
            self, bg="#000077", width=10, height=3, command=lambda: self.set_color(8)
        )
        self.azuloscuro.grid(column=3, row=9)
        self.negro = tk.Button(
            self, bg="#000000", width=10, height=3, command=lambda: self.set_color(9)
        )
        self.negro.grid(column=3, row=10)

        # Botones para opciones
        self.btn11 = tk.Button(
            self,
            text="Rotar a derecha",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_rotate_right,
        )
        self.btn11.grid(column=0, row=1)
        self.btn12 = tk.Button(
            self,
            text="Rotar a la izquierda",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_rotate_left,
        )
        self.btn12.grid(column=0, row=2)
        self.btn13 = tk.Button(
            self,
            text="Reflexión horizontal",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_horizontal_reflex,
        )
        self.btn13.grid(column=0, row=3)
        self.btn14 = tk.Button(
            self,
            text="Reflexión vertical",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_vertical_reflex,
        )
        self.btn14.grid(column=0, row=4)
        self.btn15 = tk.Button(
            self,
            text="Alto contraste",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_high_contrast,
        )
        self.btn15.grid(column=0, row=5)
        self.btn16 = tk.Button(
            self,
            text="Invertir",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_invert,
        )
        self.btn16.grid(column=0, row=6)
        self.btn17 = tk.Button(
            self,
            text="Limpiar pantalla",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.clean_screen,
        )
        self.btn17.grid(column=0, row=7)
        self.btn18 = tk.Button(
            self, text="Cuadrado", bg="#000000", fg="#ffffff", width=10, height=3, command=self.on_draw_rectangle
        )
        self.btn18.grid(column=0, row=8)
        self.btn19 = tk.Button(
            self, text="Circulo", bg="#000000", fg="#ffffff", width=10, height=3, command=self.on_draw_circle
        )
        self.btn19.grid(column=0, row=9)
        self.btn20 = tk.Button(
            self, text="Zoom in", bg="#000000", fg="#ffffff", width=10, height=3, command=self.on_zoom_in
        )
        self.btn20.grid(column=0, row=10)

        self.btn21 = tk.Button(
            self, text="Zoom out", bg="#000000", fg="#ffffff", width=10, height=3, command=self.on_zoom_out
        )
        self.btn21.grid(column=0, row=11)
        

        save_as = tk.Button(
            self, 
            text="Guardar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.save_file_as
        )
        save_as.grid(column=0, row=12)
        load = tk.Button(
            self,
            text="Cargar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.load_file
        )
        load.grid(column=0, row=13)

        show = tk.Button(
            self,
            text="Mostrar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.show_thread
        )
        show.grid(column=0, row=14)
        self.canvas = tk.Canvas(self, bg="#ffffff", width=600, height=600)
        self.canvas.grid(column=1, row=1, rowspan=13, sticky="nsew")

        self.mouse_x = 0
        self.mouse_y = 0
        
        self.do_zoom_in = False

        self.rectangles = [[0] * 24 for _ in range(24)]
        self.program_matrix = PaintxelCanvas([[0] * 24 for _ in range(24)])
        for i in range(24):
            for j in range(24):
                rect = self.canvas.create_rectangle(
                    i * 25, j * 25, i * 25 + 25, j * 25 + 25, fill="#ffffff"
                )
                self.rectangles[i][j] = rect

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    
    def save_file_as(self):
        file = fd.asksaveasfilename(title="Nombre del archivo")
        self.program_matrix.save_image_as(file)
        messagebox.showinfo(title="Guardado con exito", message=f"Guardado en {file}")
    
    def show_thread(self):
        thread = Thread(target=self.show_low_level_matrix)
        thread.start()
    
    def show_low_level_matrix(self):
        sub_window = tk.Toplevel(self)
        sub_window.config(bg="#000000")
        sub_window.resizable(False, False)
        matrix, ascii_art = str(self.program_matrix), self.program_matrix.ascii_art()
        matrix_textbox = tk.Label(
            sub_window,
            text=f"\n{matrix}\n",
            fg="#ffffff",
            bg="#000000"
        )
        ascii_art_textbox = tk.Label(
            sub_window,
            text=f"\n{ascii_art}\n",
            fg="#ffffff",
            bg="#000000"
        )

        matrix_textbox.pack()
        ascii_art_textbox.pack()
        while True:
            matrix, ascii_art = str(self.program_matrix), self.program_matrix.ascii_art()
            matrix_textbox["text"] = f"\n{matrix}\n"
            ascii_art_textbox["text"] = f"\n{ascii_art}\n"


    def load_file(self):
        file = fd.askopenfilename(title="Elige el archivo txt")
        try: 
            self.program_matrix.load_image(file)
            self.update_canvas()
            messagebox.showinfo(title="Exito", message="Se ha abierto el archivo")
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No se ha encontrado el archivo")


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
        self.program_matrix.screen = [[0] * 24 for _ in range(24)]
        self.program_matrix.screen = self.program_matrix.screen
        self.update_canvas()

    def on_mouse_motion(self, event):
        self.mouse_x, self.mouse_y = event.x // 25, event.y // 25

    def on_zoom_out(self):
        self.canvas.delete(self.cover)
        self.zoomed_canvas.destroy()
        self.canvas.grid(column=1, row=1, rowspan=14, sticky="nsew")

    def on_button_press(self, event):
        if self.do_zoom_in:
            thread = Thread(target=self.zoom_in, args=(event,))
            thread.start()
        elif self.do_draw_rectangle:
            thread = Thread(target=self.draw_rectangle, args=(event,))
            thread.start()
        elif self.do_draw_circle:
            thread = Thread(target=self.draw_circle, args=(event,))
            thread.start()
        else:
            thread = Thread(target=self.paint_square, args=(event,))
            thread.start()
    
    def on_draw_rectangle(self):
        self.do_draw_rectangle = True

    def on_draw_circle(self):
        self.do_draw_circle = True
    
    def on_zoom_in(self):
        self.do_zoom_in = True
    
    
    def draw_circle(self, event):
        x, y = event.x//25, event.y//25 
        oval = self.canvas.create_oval(x*25, y*25, x*25 + 25, y*25 + 25, fill=self.colors[self.selected_color])
        coords = [0, 0, 0, 0]
        while self.do_draw_circle:
            x0, y0, x1, y1 = 0, 0, 0, 0
            if self.mouse_x > x:
                x0, x1 = x, self.mouse_x
            elif self.mouse_x <= x:
                x0, x1 = self.mouse_x, x
            
            if self.mouse_y > y:
                y0, y1 = y, self.mouse_y
            elif self.mouse_y <= y: 
                y0, y1 = self.mouse_y, y
            
            if abs(x1 - x0) == abs(y1 - y0):
                coords = [x0 + 1, y0+1, x1-1, y1-1]

                self.canvas.coords(oval, x0*25, y0*25, x1*25 + 25, y1*25 + 25)
        
        self.canvas.delete(oval)
        
        x0, y0, x1, y1 = coords
        print(coords)
        radio = abs(x1 - x0)
        xcnt, ycnt = (x0 + x1) / 2, (y0 + y1) / 2
        for i in range(24):
            for j in range(24):
                dist = ((i - xcnt)**2 + (j - ycnt)**2) ** (1/2)
                if dist < radio:
                    self.program_matrix.screen[j][i] = self.selected_color

        self.update_canvas()

    def draw_rectangle(self, event):
        x, y = event.x//25, event.y//25 
        rectangle = self.canvas.create_rectangle(x*25, y*25, x*25 + 25, y*25 + 25, fill=self.colors[self.selected_color])
        coords = []
        while self.do_draw_rectangle:
            x0, y0, x1, y1 = 0, 0, 0, 0
            if self.mouse_x > x:
                x0, x1 = x, self.mouse_x
            elif self.mouse_x <= x:
                x0, x1 = self.mouse_x, x
            
            if self.mouse_y > y:
                y0, y1 = y, self.mouse_y
            elif self.mouse_y <= y: 
                y0, y1 = self.mouse_y, y

            coords = [x0, y0, x1, y1]

            self.canvas.coords(rectangle, x*25, y*25, self.mouse_x*25 + 25, self.mouse_y*25 + 25)
        
        self.canvas.delete(rectangle)
        for i in range(24):
            for j in range(24):
                if coords[0] <= j <= coords[2] and coords[1] <= i <= coords[3]:
                    self.program_matrix.screen[i][j] = self.selected_color
        self.update_canvas()

    def zoom_in(self, event):
        x, y = event.x//25, event.y//25 
        rectangle = self.canvas.create_rectangle(x*25, y*25, x*25 + 25, y*25 + 25, fill="#00ffaa")
        coords = []
        while self.do_zoom_in:
            x0, y0, x1, y1 = 0, 0, 0, 0
            if self.mouse_x > x:
                x0, x1 = x, self.mouse_x
            elif self.mouse_x <= x:
                x0, x1 = self.mouse_x, x
            
            if self.mouse_y > y:
                y0, y1 = y, self.mouse_y
            elif self.mouse_y <= y: 
                y0, y1 = self.mouse_y, y

            coords = [x0, y0, x1, y1]

            self.canvas.coords(rectangle, x*25, y*25, self.mouse_x*25 + 25, self.mouse_y*25 + 25)

        self.zoomed = []
        self.zoomed_canvas = tk.Canvas(self, bg="#ffffff", width=600, height=600)
        for i in range(24):
            row = []
            for j in range(24):
                if coords[0] <= j <= coords[2] and coords[1] <= i <= coords[3]:
                    color = self.program_matrix.screen[i][j]
                    row.append(color)
                else:
                    continue
            if row:
                self.zoomed.append(row)
        print(self.zoomed)
        size_y, size_x = 600/len(self.zoomed[0]), 600/len(self.zoomed)

        for i in range(len(self.zoomed)):
            for j in range(len(self.zoomed[0])):
                color = self.zoomed[i][j]
                self.zoomed_canvas.create_rectangle(j*size_y, i*size_x, j*size_y + size_y, i*size_x + size_x, fill=self.colors[color])
        self.canvas.delete(rectangle)
        self.cover = self.canvas.create_rectangle(0, 0, 600, 600, fill="#ffffff")
        self.canvas.grid_remove()
        self.zoomed_canvas.grid(column=1, row=1, rowspan=14, sticky="nsew")


    def paint_square(self, event):
        self.painting = True
        self.mouse_x, self.mouse_y = event.x // 25, event.y // 25
        while self.painting:
            self.program_matrix.screen[self.mouse_y][self.mouse_x] = self.selected_color
            self.canvas.itemconfig(
                self.rectangles[self.mouse_x][self.mouse_y],
                fill=self.colors[self.selected_color],
            )

    def on_button_release(self, _):
        self.painting = False
        self.do_zoom_in = False
        self.do_draw_rectangle = False
        self.do_draw_circle = False
        self.program_matrix.screen = self.program_matrix.screen
        print(str(self.program_matrix))

    def update_canvas(self):
        self.program_matrix.screen = self.program_matrix.screen
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles[0])):
                self.canvas.itemconfig(
                    self.rectangles[i][j], fill=self.colors[self.program_matrix.screen[j][i]]
                )

