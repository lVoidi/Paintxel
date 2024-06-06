from tkinter import filedialog as fd
from backend import PaintxelCanvas
from tkinter import messagebox
from threading import Thread
from typing import Callable
import tkinter as tk
from math import sqrt
from PIL import Image, ImageTk


SIZE: int = 75
CSIZE: int = 1000
BSIZE: int = CSIZE//SIZE

class FrontApp(tk.Tk):
    """
    Esta clase inicializa la interfaz gráfica. Hereda a tk.Tk para iniciar 
    una interfaz gráfica a partir de esta.
    """
    def __init__(self) -> None:
        """
        Inicializa todos los objetos necesarios para el programa.

        :return: None
        :rtype: None
        """
        super().__init__()

        self.config(bg="#ffffff")
        self.resizable(False, False)

        self.selected_color: int = 0
        
        # Eventos de mouse. Mientras el usuario este ejecutando
        # cierta accion, estas variables se convierten en verdaderas.
        # Estos eventos son manejados por hilos independientes.
        self.painting: bool = False
        self.do_draw_rectangle: bool = False
        self.do_draw_circle: bool = False
        self.do_zoom_in: bool = False

        self.circle_matrix: list[list[int]] = []

        # Id del cover que se le aplica al canvas original, a la hora de hacer zoom
        self.cover: int = 0
        
        # Variables que se van a utilizar a la hora de hacer zoom in
        self.zoomed: list[list[int]] = []
        self.zoomed_canvas: tk.Canvas = tk.Canvas()

        # Colores de mayor a menor luminosidad.
        self.colors: list[str] = [
            "#ffffff",
            "#ffaaaa",
            "#aaffaa",
            "#aaaaff",
            "#00ff00",
            "#ffff00",
            "#ff0000",
            "#0000ff",
            "#000077",
            "#000000",
        ]

        top_canvas: tk.Canvas = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        bottom_canvas: tk.Canvas = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)

        # Creacion de todos los botones de colores
        white_button = tk.Button(
            self, bg="#ffffff", width=10, height=4, command=lambda: self.set_color(0)
        )
        pink_button = tk.Button(
            self, bg="#ffaaaa", width=10, height=4, command=lambda: self.set_color(1)
        )
        light_green_button = tk.Button(
            self, bg="#aaffaa", width=10, height=4, command=lambda: self.set_color(2)
        )
        light_blue_button = tk.Button(
            self, bg="#aaaaff", width=10, height=4, command=lambda: self.set_color(3)
        )
        green_button = tk.Button(
            self, bg="#00ff00", width=10, height=4, command=lambda: self.set_color(4)
        )
        fuchsia_button = tk.Button(
            self, bg="#ffff00", width=10, height=4, command=lambda: self.set_color(5)
        )
        red_button = tk.Button(
            self, bg="#ff0000", width=10, height=4, command=lambda: self.set_color(6)
        )
        blue_button = tk.Button(
            self, bg="#0000ff", width=10, height=4, command=lambda: self.set_color(7)
        )
        dark_blue_button = tk.Button(
            self, bg="#000077", width=10, height=4, command=lambda: self.set_color(8)
        )
        black_button = tk.Button(
            self, bg="#000000", width=10, height=4, command=lambda: self.set_color(9)
        )

        # Botones de cada una de las funciones
        rotright = Image.open("PNGs/RotRight.png")
        rotright = rotright.resize((75, 75))
        rotright_image = ImageTk.PhotoImage(rotright)
        rotate_right_button = tk.Button(
            self,
            image=rotright_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.rotate_right),
        )
        rotate_right_button.image = rotright_image

        rotleft = Image.open("PNGs/RotLeft.png")
        rotleft = rotleft.resize((75, 75))
        rotleft_image = ImageTk.PhotoImage(rotleft)
        rotate_left_button = tk.Button(
            self,
            image=rotleft_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.rotate_left),
        )
        rotate_left_button.image = rotleft_image

        reflexhori = Image.open("PNGs/ReflexHori.png")
        reflexhori = reflexhori.resize((75, 75))
        reflexhori_image = ImageTk.PhotoImage(reflexhori)
        horizontal_reflex_button = tk.Button(
            self,
            image=reflexhori_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.vertical_reflex),
        )
        horizontal_reflex_button.image = reflexhori_image


        reflexvert = Image.open("PNGs/ReflexVert.png")
        reflexvert = reflexvert.resize((75, 75))
        reflexvert_image = ImageTk.PhotoImage(reflexvert)
        vertical_reflex_button = tk.Button(
            self,
            image=reflexvert_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.horizontal_reflex),
        )
        vertical_reflex_button.image = reflexvert_image


        high_contrast = Image.open("PNGs/Contrast.png")
        high_contrast = high_contrast.resize((75, 75))
        high_contrast_image = ImageTk.PhotoImage(high_contrast)
        high_contrast_button = tk.Button(
            self,
            image=high_contrast_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.high_contrast),
        )
        high_contrast_button.image = high_contrast_image


        invert = Image.open("PNGs/Invert.png")
        invert = invert.resize((75, 75))
        invert_image = ImageTk.PhotoImage(invert)
        invert_button = tk.Button(
            self,
            image=invert_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.invert),
        )
        invert_button.image = invert_image


        clear = Image.open("PNGs/Clear.png")
        clear = clear.resize((75, 75))
        clear_image = ImageTk.PhotoImage(clear)
        clear_button = tk.Button(
            self,
            image=clear_image,
            width=75,
            height=75,
            command=lambda: self.wrap_event(self.program_matrix.clear_screen),
        )
        clear_button.image = clear_image

        
        square = Image.open("PNGs/Square.png")
        square = square.resize((75, 75))
        square_image = ImageTk.PhotoImage(square)
        square_button = tk.Button(
            self,
            image= square_image, 
            width=75,
            height=75,
            command=self.on_draw_rectangle
        )
        square_button.image = square_image


        circle = Image.open("PNGs/Circle.png")
        circle = circle.resize((75, 75))
        circle_image = ImageTk.PhotoImage(circle)
        circle_button = tk.Button(
            self,
            image=circle_image,
            width=75,
            height=75,
            command=self.on_draw_circle
        )
        circle_button.image = circle_image


        imagein = Image.open("PNGs/ZoomIn.png")
        imagein = imagein.resize((75, 75))
        zoom_in_image = ImageTk.PhotoImage(imagein)
        zoom_in_button = tk.Button(
            self,
            image=zoom_in_image,
            width=75,
            height=75,
            command=self.on_zoom_in
        )
        zoom_in_button.image = zoom_in_image


        imageout = Image.open("PNGs/ZoomOut.png")
        imageout = imageout.resize((75, 75))
        zoom_out_image = ImageTk.PhotoImage(imageout)
        zoom_out_button = tk.Button(
            self,
            image=zoom_out_image,
            width=75,
            height=75,
            command=self.on_zoom_out
        )
        zoom_out_button.image = zoom_out_image

        save_as_button = tk.Button(
            self, 
            text="Guardar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=4,
            command=self.save_file_as
        )

        load_button = tk.Button(
            self,
            text="Cargar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=4,
            command=self.load_file
        )

        show_button = tk.Button(
            self,
            text="Mostrar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=4,
            command=self.show_thread
        )

        self.canvas: tk.Canvas = tk.Canvas(self, bg="#ffffff", width=CSIZE, height=CSIZE)

        # Guarda las coordenadas del mouse en todo momento, mediante el evento de B1-Motion
        self.mouse_x: int = 0
        self.mouse_y: int = 0

        # Matriz que guarda las IDs de todos los rectangulos creados en self.canvas
        self.rectangles: list[list[int]] = [[0] * SIZE for _ in range(SIZE)]

        # Matriz del programa a partir de matriz con ceros, tamaño 24x24. Referenciar backend.py.
        self.program_matrix: PaintxelCanvas = PaintxelCanvas(screen=[[0] * SIZE for _ in range(SIZE)], size=SIZE)
        for i in range(SIZE):
            for j in range(SIZE):
                rect: int = self.canvas.create_rectangle(
                    i * BSIZE, j * BSIZE, i * BSIZE + BSIZE, j * BSIZE + BSIZE, fill="#ffffff"
                )
                self.rectangles[i][j] = rect
        

        white_button.grid(column=3, row=1)
        pink_button.grid(column=3, row=2)
        light_green_button.grid(column=3, row=3)
        light_blue_button.grid(column=3, row=4)
        green_button.grid(column=3, row=5)
        fuchsia_button.grid(column=3, row=6)
        red_button.grid(column=3, row=7)
        blue_button.grid(column=3, row=8)
        dark_blue_button.grid(column=3, row=9)
        black_button.grid(column=3, row=10)
        zoom_in_button.grid(column=3, row=11)
        zoom_out_button.grid(column=3, row=12)


        rotate_right_button.grid(column=0, row=1)
        rotate_left_button.grid(column=0, row=2)
        horizontal_reflex_button.grid(column=0, row=3)
        vertical_reflex_button.grid(column=0, row=4)
        high_contrast_button.grid(column=0, row=5)
        invert_button.grid(column=0, row=6)
        clear_button.grid(column=0, row=7)
        square_button.grid(column=0, row=8)
        circle_button.grid(column=0, row=9)
        save_as_button.grid(column=0, row=10)
        load_button.grid(column=0, row=11)
        show_button.grid(column=0, row=12)
        
        self.canvas_rowspan = 12

        self.canvas.grid(column=1, row=1, rowspan=self.canvas_rowspan, sticky="nsew")
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)


    def save_file_as(self) -> None:
        """
        Abre un diálogo para guardar el archivo en una dirección específica.

        :return: None 
        :rtype: NoneType
        """
        file_path: str = fd.asksaveasfilename(title="Nombre del archivo")
        self.program_matrix.save_image_as(file_path)
        messagebox.showinfo(title="Guardado con exito", message=f"Guardado en {file_path}")
    
    def show_thread(self) -> None:
        """
        Inicializa el hilo para mostrar la matriz y el ascii art, en tiempo real 

        :return: None 
        :rtype: NoneType
        """
        thread: Thread = Thread(target=self.show_low_level_matrix)
        thread.start()
    
    def show_low_level_matrix(self) -> None:
        """
        Muestra la matriz de la pantalla en tiempo real. A su vez, 
        muestra un ascii art generado a partir de los valores de 
        color de la pantalla. Este se crea en una nueva ventana.

        :return: None 
        :rtype: None
        """
        sub_window_matrix: tk.Toplevel = tk.Toplevel(self)
        sub_window_matrix.config(bg="#000000")
        sub_window_matrix.resizable(False, False)
        
        sub_window_ascii_art: tk.Toplevel = tk.Toplevel(self)
        sub_window_ascii_art.config(bg="#000000")
        sub_window_ascii_art.resizable(False, False)

        matrix: str = str(self.program_matrix)
        ascii_art: str = self.program_matrix.ascii_art()
        matrix_textbox: tk.Label = tk.Label(
            sub_window_matrix,
            text=f"\n{matrix}\n",
            fg="#ffffff",
            bg="#000000",
            font="Arial"
        )
        ascii_art_textbox: tk.Label = tk.Label(
            sub_window_ascii_art,
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


    def load_file(self) -> None:
        """
        Carga el archivo. También, se asegura que el archivo exista. 

        :return: None 
        :rtype: NoneType
        """
        file = fd.askopenfilename(title="Elige el archivo txt")
        new_screen: list[list[int]] = self.program_matrix.load_image(file)
        
        # El método load_image devuelve una lista vacía si el archivo no existe.
        # Este if se asegura que la nueva pantalla tenga contenido
        if new_screen:
            self.update_canvas()
            messagebox.showinfo(title="Exito", message="Se ha abierto el archivo")
        else:
            messagebox.showerror(title="Error", message="No se ha encontrado el archivo")


    def set_color(self, color) -> None:
        """
        Asigna un nuevo color seleccionado al objeto.

        :param color: Nuevo color 
        :type color: int 
        :return: None 
        :rtype: None
        """
        self.selected_color = color
    
    
    def wrap_event(self, func: Callable) -> None:
        """
        Envuelve una funcion *func*, para después actualizar el canvas. 
        Útil para no escribir una función específica para cada uno de 
        los botones.

        :param func: Función del boton que se quiere envolver 
        :type func: Callable 
        :return: None 
        :rtype: NoneType
        """
        func()
        self.update_canvas()

    def on_mouse_motion(self, event) -> None:
        """
        Actualiza las coordenadas del mouse en tiempo real. Estas 
        coordenadas son utilizadas por todas las funciones que requieren 
        arrastrar el click izquierdo (cuadrado, circulo y zoom in). 

        :param event: Evento del movimiento del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
        self.mouse_x, self.mouse_y = event.x // BSIZE, event.y // BSIZE

    def on_zoom_out(self) -> None:
        """
        Quita el cover que pone la funcion de zoom, destruye el canvas 
        creado y vuelve a colocar el canvas original en la misma posición. 

        :return: None 
        :rtype: NoneType
        """
        self.canvas.delete(self.cover)
        self.zoomed_canvas.destroy()
        self.canvas.grid(column=1, row=1, rowspan=self.canvas_rowspan, sticky="nsew")

    def on_button_press(self, event) -> None:
        """
        Este evento se crea un hilo, dependiendo de qué evento el usuario activó. 
        Este evento crea un thread para hacer el efecto de drag. 

        :param event: Evento del click izquierdo del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
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
    
    def on_draw_rectangle(self) -> None:
        """
        Habilita el evento del rectángulo. 

        :return: None 
        :rtype: None
        """
        self.do_draw_rectangle = True

    def on_draw_circle(self) -> None:
        """
        Habilita el evento del círculo. 

        :return: None 
        :rtype: None
        """
        self.do_draw_circle = True
    
    def on_zoom_in(self) -> None:
        """
        Habilita el evento del zoom in. 

        :return: None 
        :rtype: None
        """
        self.do_zoom_in = True
    
    
    def draw_circle(self, event) -> None:
        """
        Empieza a trazar un círculo mientras el usuario mantenga el click presionado.
        Cuando se activa el button-release, se traza un círculo utilizando el método 
        de la distancia euclideana. Si la distancia de un punto (x, y) al centro del
        círculo es menor al radio, entonces se dice que (x, y) está dentro del círculo. 
        Esta validación se hace para cada i, j dentro de la submatriz del rango seleccionado 
        por el mouse del usuario.

        :param event: Evento del movimiento del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
        x: int = event.x // BSIZE
        y: int = event.y // BSIZE
        oval: int = self.canvas.create_oval(x*BSIZE, y*BSIZE, x*BSIZE + BSIZE, y*BSIZE + BSIZE, fill=self.colors[self.selected_color])
        coords: list[int] = [0, 0, 0, 0]
        while self.do_draw_circle:
            # (x0, y0) es el punto inicial 
            # (x1, y1) es el punto final 
            # Estas validaciones son necesarias pues, dependiendo 
            # de la orientación en la que el usuario seleccionó la zona
            x0, y0, x1, y1 = 0, 0, 0, 0
            
            # Eje x
            if self.mouse_x > x:
                x0, x1 = x, self.mouse_x
            elif self.mouse_x <= x:
                x0, x1 = self.mouse_x, x

            # Eje y
            if self.mouse_y > y:
                y0, y1 = y, self.mouse_y
            elif self.mouse_y <= y: 
                y0, y1 = self.mouse_y, y
            

            if abs(x1 - x0) == abs(y1 - y0):
                coords = [x0, y0, x1, y1]
                self.canvas.coords(oval, x0*BSIZE, y0*BSIZE, x1*BSIZE + BSIZE, y1*BSIZE + BSIZE)
        
        self.canvas.delete(oval)
        
        x0, y0, x1, y1 = coords
        xcnt, ycnt = (x0 + x1) / 2, (y0 + y1) / 2
        radio: int = abs(x1 - x0)//2
        for i in range(SIZE):
            for j in range(SIZE):
                dist: float = sqrt((i - xcnt)**2 + (j - ycnt)**2)
                if dist <= radio:
                    self.program_matrix.screen[j][i] = self.selected_color

        self.update_canvas(*coords)

    def draw_rectangle(self, event) -> None:
        """
        Traza el rectángulo a partir de las coordenadas iniciales y las coordenadas 
        del mouse, mientras está presionado.

        :param event: Evento del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
        x, y = event.x//BSIZE, event.y//BSIZE 
        rectangle: int = self.canvas.create_rectangle(x*BSIZE, y*BSIZE, x*BSIZE + BSIZE, y*BSIZE + BSIZE, fill=self.colors[self.selected_color])
        coords: list[int] = []
        while self.do_draw_rectangle:
            x0, y0, x1, y1 = 0, 0, 0, 0
            # Eje x
            if self.mouse_x > x:
                x0, x1 = x, self.mouse_x
            elif self.mouse_x <= x:
                x0, x1 = self.mouse_x, x
            
            # Eje y
            if self.mouse_y > y:
                y0, y1 = y, self.mouse_y
            elif self.mouse_y <= y: 
                y0, y1 = self.mouse_y, y

            coords = [x0, y0, x1, y1]

            self.canvas.coords(rectangle, x*BSIZE, y*BSIZE, self.mouse_x*BSIZE + BSIZE, self.mouse_y*BSIZE + BSIZE)
        
        self.canvas.delete(rectangle)
        for i in range(SIZE):
            for j in range(SIZE):
                if coords[0] <= j <= coords[2] and coords[1] <= i <= coords[3]:
                    try:
                        self.program_matrix.screen[i][j] = self.selected_color
                    except IndexError:
                        print("Mouse fuera de rango. Ignorando...")
        self.update_canvas(*coords)

    def zoom_in(self, event) -> None:
        x, y = event.x//BSIZE, event.y//BSIZE 
        rectangle = self.canvas.create_rectangle(
            x*BSIZE,
            y*BSIZE,
            x*BSIZE + BSIZE,
            y*BSIZE + BSIZE,
            fill="#00ffaa"
        )
        coords: list[int] = []
        while self.do_zoom_in:
            x0, y0, x1, y1 = 0, 0, 0, 0
            # Eje x
            if self.mouse_x > x:
                x0, x1 = x, self.mouse_x
            elif self.mouse_x <= x:
                x0, x1 = self.mouse_x, x
            
            # Eje y 
            if self.mouse_y > y:
                y0, y1 = y, self.mouse_y
            elif self.mouse_y <= y: 
                y0, y1 = self.mouse_y, y

            coords = [x0, y0, x1, y1]

            self.canvas.coords(rectangle, x*BSIZE, y*BSIZE, self.mouse_x*BSIZE + BSIZE, self.mouse_y*BSIZE + BSIZE)

        self.zoomed: list[list[int]] = []
        self.zoomed_canvas: tk.Canvas = tk.Canvas(self, bg="#ffffff", width=CSIZE, height=CSIZE)
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                if coords[0] <= j <= coords[2] and coords[1] <= i <= coords[3]:
                    color = self.program_matrix.screen[i][j]
                    row.append(color)
                else:
                    continue
            if row:
                self.zoomed.append(row)
        size_y, size_x = CSIZE/len(self.zoomed[0]), CSIZE/len(self.zoomed)

        for i in range(len(self.zoomed)):
            for j in range(len(self.zoomed[0])):
                color = self.zoomed[i][j]
                self.zoomed_canvas.create_rectangle(j*size_y, i*size_x, j*size_y + size_y, i*size_x + size_x, fill=self.colors[color])
        self.canvas.delete(rectangle)
        self.cover = self.canvas.create_rectangle(0, 0, 600, 600, fill="#ffffff")
        self.canvas.grid_remove()
        self.zoomed_canvas.grid(column=1, row=1, rowspan=self.canvas_rowspan, sticky="nsew")


    def paint_square(self, event) -> None:
        """
        Pinta el cuadrado en la posición del evento.

        :param event: Evento del click del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
        self.painting = True
        self.mouse_x, self.mouse_y = event.x // BSIZE, event.y // BSIZE
        while self.painting:
            try:
                self.program_matrix.screen[self.mouse_y][self.mouse_x] = self.selected_color
            except IndexError:
                print("Mouse fuera de rango. Ignorando...")
                continue
            self.canvas.itemconfig(
                self.rectangles[self.mouse_x][self.mouse_y],
                fill=self.colors[self.selected_color],
            )

    def on_button_release(self, _) -> None:
        """
        Este evento se activa cuando se suelta el mouse, reinicia 
        todas las variables de los eventos que requieren de un 
        bucle para funcionar.

        :param _: Evento al soltar el mouse 
        :type _: tkinter Event
        :return: None 
        :rtype: None 
        """
        self.painting = False
        self.do_zoom_in = False
        self.do_draw_rectangle = False
        self.do_draw_circle = False

    def update_canvas(self, x0=0, y0=0, x1=0, y1=0) -> None:
        """
        Actualiza el canvas mostrado en pantalla, con los valores actuales 
        del self.program_matrix.screen

        :return: None 
        :rtype: None 
        """
        
        if not all((x0, y0, x1, y1)):
            for i in range(SIZE):
                for j in range(SIZE):
                    self.canvas.itemconfig(
                        self.rectangles[i][j], fill=self.colors[self.program_matrix.screen[j][i]]
                    )
        else:
            if x1 > SIZE:
                x1 = x0 + abs(SIZE - x0)
            if y1 > SIZE:
                y1 = y0 + abs(SIZE - y0)

            for i in range(x0, x1):
                for j in range(y0, y1):
                    self.canvas.itemconfig(
                        self.rectangles[i][j], fill=self.colors[self.program_matrix.screen[j][i]]
                    )
