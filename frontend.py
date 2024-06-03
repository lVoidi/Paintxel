from tkinter import filedialog as fd
from backend import PaintxelCanvas
from tkinter import messagebox
from threading import Thread
import tkinter as tk


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
        self.geometry("765x790")
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
            "#ff00ff",
            "#ff0000",
            "#0000ff",
            "#000077",
            "#000000",
        ]

        top_canvas: tk.Canvas = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)
        bottom_canvas: tk.Canvas = tk.Canvas(self, bg="#9b9b9b", width=700, height=50)

        # Creacion de todos los botones de colores
        white_button = tk.Button(
            self, bg="#ffffff", width=10, height=3, command=lambda: self.set_color(0)
        )
        pink_button = tk.Button(
            self, bg="#ffaaaa", width=10, height=3, command=lambda: self.set_color(1)
        )
        light_green_button = tk.Button(
            self, bg="#aaffaa", width=10, height=3, command=lambda: self.set_color(2)
        )
        light_blue_button = tk.Button(
            self, bg="#aaaaff", width=10, height=3, command=lambda: self.set_color(3)
        )
        green_button = tk.Button(
            self, bg="#00ff00", width=10, height=3, command=lambda: self.set_color(4)
        )
        fuchsia_button = tk.Button(
            self, bg="#ff00ff", width=10, height=3, command=lambda: self.set_color(5)
        )
        red_button = tk.Button(
            self, bg="#ff0000", width=10, height=3, command=lambda: self.set_color(6)
        )
        blue_button = tk.Button(
            self, bg="#0000ff", width=10, height=3, command=lambda: self.set_color(7)
        )
        dark_blue_button = tk.Button(
            self, bg="#000077", width=10, height=3, command=lambda: self.set_color(8)
        )
        black_button = tk.Button(
            self, bg="#000000", width=10, height=3, command=lambda: self.set_color(9)
        )

        # Botones de cada una de las funciones
        rotate_right_button = tk.Button(
            self,
            text="Rotar a derecha",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.rotate_right),
        )

        rotate_left_button = tk.Button(
            self,
            text="Rotar a la izquierda",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.rotate_left),
        )

        horizontal_reflex_button = tk.Button(
            self,
            text="Reflexión horizontal",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.horizontal_reflex),
        )

        vertical_reflex_button = tk.Button(
            self,
            text="Reflexión vertical",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.vertical_reflex),
        )

        high_contrast_button = tk.Button(
            self,
            text="Alto contraste",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.high_contrast),
        )

        invert_button = tk.Button(
            self,
            text="Invertir",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.invert),
        )

        clear_button = tk.Button(
            self,
            text="Limpiar pantalla",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=lambda: self.wrap_event(self.program_matrix.clear_screen),
        )

        square_button = tk.Button(
            self,
            text="Cuadrado",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_draw_rectangle
        )

        circle_button = tk.Button(
            self,
            text="Circulo",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_draw_circle
        )

        zoom_in_button = tk.Button(
            self,
            text="Zoom in",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_zoom_in
        )

        zoom_out_button = tk.Button(
            self,
            text="Zoom out",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.on_zoom_out
        )

        save_as_button = tk.Button(
            self, 
            text="Guardar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.save_file_as
        )

        load_button = tk.Button(
            self,
            text="Cargar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.load_file
        )

        show_button = tk.Button(
            self,
            text="Mostrar",
            bg="#000000",
            fg="#ffffff",
            width=10,
            height=3,
            command=self.show_thread
        )

        self.canvas: tk.Canvas = tk.Canvas(self, bg="#ffffff", width=600, height=600)

        # Guarda las coordenadas del mouse en todo momento, mediante el evento de B1-Motion
        self.mouse_x: int = 0
        self.mouse_y: int = 0

        # Matriz que guarda las IDs de todos los rectangulos creados en self.canvas
        self.rectangles: list[list[int]] = [[0] * 24 for _ in range(24)]

        # Matriz del programa a partir de matriz con ceros, tamaño 24x24. Referenciar backend.py.
        self.program_matrix: PaintxelCanvas = PaintxelCanvas(screen=[[0] * 24 for _ in range(24)])
        for i in range(24):
            for j in range(24):
                rect: int = self.canvas.create_rectangle(
                    i * 25, j * 25, i * 25 + 25, j * 25 + 25, fill="#ffffff"
                )
                self.rectangles[i][j] = rect
        
        # Posicionamiento de elementos por secciones
        top_canvas.grid(column=0, row=0, columnspan=4, sticky="nsew")
        bottom_canvas.grid(column=0, row=11, columnspan=4, sticky="nsew")

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


        rotate_right_button.grid(column=0, row=1)
        rotate_left_button.grid(column=0, row=2)
        horizontal_reflex_button.grid(column=0, row=3)
        vertical_reflex_button.grid(column=0, row=4)
        high_contrast_button.grid(column=0, row=5)
        invert_button.grid(column=0, row=6)
        clear_button.grid(column=0, row=7)
        square_button.grid(column=0, row=8)
        circle_button.grid(column=0, row=9)
        zoom_in_button.grid(column=0, row=10)
        zoom_out_button.grid(column=0, row=11)
        save_as_button.grid(column=0, row=12)
        load_button.grid(column=0, row=13)
        show_button.grid(column=0, row=14)

        self.canvas.grid(column=1, row=1, rowspan=13, sticky="nsew")
        
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
        sub_window: tk.Toplevel = tk.Toplevel(self)
        sub_window.config(bg="#000000")
        sub_window.resizable(False, False)
        
        matrix: str = str(self.program_matrix)
        ascii_art: str = self.program_matrix.ascii_art()
        matrix_textbox: tk.Label = tk.Label(
            sub_window,
            text=f"\n{matrix}\n",
            fg="#ffffff",
            bg="#000000"
        )
        ascii_art_textbox: tk.Label = tk.Label(
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
    
    
    def wrap_event(self, func) -> None:
        """
        Envuelve una funcion *func*, para después actualizar el canvas. 
        Útil para no escribir una función específica para cada uno de 
        los botones.

        :param func: Función del boton que se quiere envolver 
        :type func: function 
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
        self.mouse_x, self.mouse_y = event.x // 25, event.y // 25

    def on_zoom_out(self) -> None:
        """
        Quita el cover que pone la funcion de zoom, destruye el canvas 
        creado y vuelve a colocar el canvas original en la misma posición. 

        :return: None 
        :rtype: NoneType
        """
        self.canvas.delete(self.cover)
        self.zoomed_canvas.destroy()
        self.canvas.grid(column=1, row=1, rowspan=14, sticky="nsew")

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
        x: int = event.x // 25
        y: int = event.y // 25
        oval: int = self.canvas.create_oval(x*25, y*25, x*25 + 25, y*25 + 25, fill=self.colors[self.selected_color])
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
                self.canvas.coords(oval, x0*25, y0*25, x1*25 + 25, y1*25 + 25)
        
        self.canvas.delete(oval)
        
        x0, y0, x1, y1 = coords
        xcnt, ycnt = (x0 + x1) / 2, (y0 + y1) / 2
        radio: int = abs(x1 - x0)//2
        for i in range(24):
            for j in range(24):
                dist: float = ((i - xcnt)**2 + (j - ycnt)**2) ** (1/2)
                if dist <= radio:
                    self.program_matrix.screen[j][i] = self.selected_color

        self.update_canvas()

    def draw_rectangle(self, event) -> None:
        """
        Traza el rectángulo a partir de las coordenadas iniciales y las coordenadas 
        del mouse, mientras está presionado.

        :param event: Evento del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
        x, y = event.x//25, event.y//25 
        rectangle: int = self.canvas.create_rectangle(x*25, y*25, x*25 + 25, y*25 + 25, fill=self.colors[self.selected_color])
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

            self.canvas.coords(rectangle, x*25, y*25, self.mouse_x*25 + 25, self.mouse_y*25 + 25)
        
        self.canvas.delete(rectangle)
        for i in range(24):
            for j in range(24):
                if coords[0] <= j <= coords[2] and coords[1] <= i <= coords[3]:
                    try:
                        self.program_matrix.screen[i][j] = self.selected_color
                    except IndexError:
                        print("Mouse fuera de rango. Ignorando...")
        self.update_canvas()

    def zoom_in(self, event) -> None:
        x, y = event.x//25, event.y//25 
        rectangle = self.canvas.create_rectangle(
            x*25,
            y*25,
            x*25 + 25,
            y*25 + 25,
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

            self.canvas.coords(rectangle, x*25, y*25, self.mouse_x*25 + 25, self.mouse_y*25 + 25)

        self.zoomed: list[list[int]] = []
        self.zoomed_canvas: tk.Canvas = tk.Canvas(self, bg="#ffffff", width=600, height=600)
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
        size_y, size_x = 600/len(self.zoomed[0]), 600/len(self.zoomed)

        for i in range(len(self.zoomed)):
            for j in range(len(self.zoomed[0])):
                color = self.zoomed[i][j]
                self.zoomed_canvas.create_rectangle(j*size_y, i*size_x, j*size_y + size_y, i*size_x + size_x, fill=self.colors[color])
        self.canvas.delete(rectangle)
        self.cover = self.canvas.create_rectangle(0, 0, 600, 600, fill="#ffffff")
        self.canvas.grid_remove()
        self.zoomed_canvas.grid(column=1, row=1, rowspan=14, sticky="nsew")


    def paint_square(self, event) -> None:
        """
        Pinta el cuadrado en la posición del evento.

        :param event: Evento del click del mouse 
        :type event: tkinter Event
        :return: None 
        :rtype: None 
        """
        self.painting = True
        self.mouse_x, self.mouse_y = event.x // 25, event.y // 25
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

    def update_canvas(self) -> None:
        """
        Actualiza el canvas mostrado en pantalla, con los valores actuales 
        del self.program_matrix.screen

        :return: None 
        :rtype: None 
        """
        self.program_matrix.screen = self.program_matrix.screen
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles[0])):
                self.canvas.itemconfig(
                    self.rectangles[i][j], fill=self.colors[self.program_matrix.screen[j][i]]
                )

