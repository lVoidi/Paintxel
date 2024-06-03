class PaintxelCanvas:
    def __init__(self, screen: list[list[int]]) -> None:
        """
        Esta clase permite controlar de manera sencilla la matriz
        del editor.

        :param screen: Pantalla inicial, en el caso del programa, es una matriz 24x24
        :type screen: list[list[int]]
        :return: None
        :rtype: Nonetype
        """
        self.screen: list[list[int]] = screen
        self.ascii_values: list[str] = [" ", ".", ":", "-", "=", "¡", "&", "$", "%", "@"]

    def rotate_left(self) -> list[list[int]]:
        """
        Rota a la izquierda la matriz. Para esto, se toman las 
        columnas de derecha a izquierda y se convierten en las 
        filas. 
           
        :return: La nueva pantalla 
        :rtype: list[list[int]]
        """
        rows: int = len(self.screen)
        columns: int = len(self.screen[0])
        new: list[list[int]] = [[0] * rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                new[j][i] = self.screen[i][columns - 1 - j]

        self.screen = new

        return new

    def rotate_right(self) -> list[list[int]]:
        """
        Rota a la derecha la matriz. Para esto, hay que sacar 
        la transpuesta de la matriz y, a continuación, sacar 
        el reverso de cada fila. 
        
        Tome una matriz S

           S = 1 2  
               3 4 
        => 
           S_t = 1 3 
                 2 4 
        => 
           S_t_r = 3 1     Para rotarlo a la derecha, no basta con 
                   4 2     sacar la transpuesta de la matriz.
           
        :return: La nueva pantalla 
        :rtype: list[list[int]]
        """
        rows: int = len(self.screen)
        columns: int = len(self.screen[0])

        auxiliar_matrix: list[list[int]] = [[0] * rows for _ in range(columns)]
        result: list[list[int]] = [[0] * rows for _ in range(columns)]

        # Obtiene la transpuesta de la matriz
        for i in range(rows):
            for j in range(columns):
                auxiliar_matrix[j][i] = self.screen[i][j]

        # La transpuesta NO es una rotación a la derecha. Así que se
        # crea una nueva matriz que va a tener el reverso de cada
        # fila de la transpuesta (rotación a la derecha).
        for i in range(columns):
            for j in range(rows):
                result[i][j] = auxiliar_matrix[i][rows - 1 - j]

        self.screen = result

        return result

    def horizontal_reflex(self) -> list[list[int]]:
        """
        Refleja horizontalmente la pantalla. Para esto, solo basta 
        con tomar las últimas columnas y convertirlas en las primeras 
        de la matriz resultante.

        :return: La nueva pantalla 
        :rtype: list[list[int]]
        """
        rows: int = len(self.screen)
        columns: int = len(self.screen[0])
        result: list[list[int]] = [[0] * columns for _ in range(rows)]

        # Este bucle for posiciona el primer elemento de una fila como el último
        # elemento de una lista nueva
        for i in range(rows):
            for j in range(columns):
                result[i][columns - 1 - j] = self.screen[i][j]

        self.screen = result

        return result

    def vertical_reflex(self) -> list[list[int]]:
        """
        Refleja verticalmente la pantalla. Para esto, las últimas 
        filas de la pantalla son asignadas como las primeras filas 
        de la matriz resultante. 

        :return: La nueva pantalla 
        :rtype: list[list[int]]
        """
        rows: int = len(self.screen)
        columns: int = len(self.screen[0])
        result: list[list[int]] = [[0] * columns for _ in range(rows)]

        # Mueve las últimas filas a las primeras posiciones
        for row in range(rows):
            result[rows - 1 - row] = self.screen[row]

        self.screen = result

        return result

    def high_contrast(self) -> list[list[int]]:
        """
        Convierte los valores entre 0 y 4 en 0 y los valores entre 5 y 9 en 9. 
        Después de aplicar esta función, la pantalla se convierte en blanco y negro 
        
        :return: La pantalla con alto contraste
        :rtype: list[list[int]]
        """
        rows: int = len(self.screen)
        columns: int = len(self.screen[0])
        result: list[list[int]] = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                element = self.screen[i][j]
                result[i][j] = 0 if element <= 4 else 9

        self.screen = result
        return result

    def invert(self) -> list[list[int]]:
        """
        Invierte los valores de los colores. Ya que los valores de los colores 
        son representados por números del 0 al 9, según su claridad, para 
        invertirlos basta con restar el número más alto, el cual es el 9 (negro),
        para obtener el color invertido.

        :return: Matriz con los colores invertidos
        :rtype: list[list[int]]
        """
        rows: int = len(self.screen)
        columns: int = len(self.screen[0])
        result: list[list[int]] = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                element = self.screen[i][j]
                result[i][j] = 9 - element

        self.screen = result
        return result

    def ascii_art(self) -> str:
        """
        Toma los valores de ascii_values para convertir la pantalla en un ascii art. 

        :return: Ascii art de la matriz 
        :rtype: str
        """
        result: str = ""
        for row in self.screen:
            for element in row:
                result += self.ascii_values[element]
            result += "\n"
        return result

    def save_image_as(self, name) -> None:
        """
        Guarda la imagen con el nombre dicho. Cada columna separada por comas y
        las filas separadas por newline.

        :param name: Nombre de la imagen
        :return: None 
        :rtype: NoneType
        """
        with open(f"{name}.txt", "w") as file:
            result: str = ""
            for row in self.screen:
                for index, element in enumerate(row):
                    result += f"{element}," if index < len(row) - 1 else f"{element}"
                result += "\n"
            file.write(result)

    def load_image(self, name) -> list[list[int]] | list:
        """
        Carga la imagen. Retorna una lista vacía al no existir el archivo.
        
        :param name: Nombre del archivo a cargar
        :return: La pantalla actual 
        :rtype: list[list[int]] | list
        """
        try:
            with open(f"{name}", "r") as file:
                rows: list[str] = file.read().split()
                self.screen: list[list[int]] = []

                for row in rows:
                    auxiliar_row: list[int] = []
                    elements: list[str] = row.split(",")

                    for element in elements:
                        element_to_int: int = int(element)
                        auxiliar_row.append(element_to_int)

                    self.screen.append(auxiliar_row)

        except FileNotFoundError:
            self.screen: list[list[int]] = []

        return self.screen

    def clear_screen(self) -> list[list[int]]:
        """
        Convierte todos los valores de la matriz en ceros.

        :return: La matriz con ceros 
        :rtype: list[list[int]]
        """
        self.screen = [[0] * 24 for _ in range(24)]
        return self.screen

    def __str__(self) -> str:
        """
        Representación de la matriz actual. 
        :return: La matriz representada 
        :rtype: str
        """
        matr: str = "["
        matr_to_print: list[list[int]] = self.screen

        rows: int = len(matr_to_print) 
        columns: int = len(matr_to_print[0])

        for i in range(rows):
            for j in range(columns):
                if j >= columns - 1 and i >= rows - 1:
                    matr += f" {matr_to_print[i][j]}]\n"
                elif j >= columns - 1:
                    matr += f" {matr_to_print[i][j]}\n"
                elif i >= 1:
                    matr += f" {matr_to_print[i][j]} "
                elif j == 0 and i == 0:
                    matr += f"{matr_to_print[i][j]} "
                else:
                    matr += f" {matr_to_print[i][j]} "
        return matr
