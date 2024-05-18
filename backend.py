
class PaintxelCanvas:
    def __init__(self, screen: list) -> None:
        """
        Esta clase permite controlar de manera sencilla la matriz
        del editor
        """
        # Pantalla que muestra
        self.screen = screen
        self.ascii_values = [" ", ".", ":", "-", "=", "¡", "&", "$", "%", "@"]
        # Historial de cambios a la pantalla 
        self.history = [screen]
        self.pointer = 0 
    
    def rotate_left(self) -> list:
        """
        Rota a la izquierda la matriz
        """
        rows, columns = len(self.screen), len(self.screen[0])
        new = [[0]*rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                new[j][i] = self.screen[i][columns-1-j]

        self.history.append(new)
        self.pointer += 1
        self.screen = new

        return new

    def rotate_right(self) -> list:
        """
        Rota a la derecha la matriz
        """
        rows, columns = len(self.screen), len(self.screen[0])
        new = [[0]*rows for _ in range(columns)]
        
        result = [[0]*rows for _ in range(columns)]
        
        # Obtiene la transpuesta de la matriz
        for i in range(rows):
            for j in range(columns):
                new[j][i] = self.screen[i][j]
        
        # La transpuesta NO es una rotación a la derecha. Así que se 
        # crea una nueva matriz que va a tener el reverso de cada 
        # fila de la transpuesta (rotación a la derecha).
        for i in range(columns):
            for j in range(rows):
                result[i][j] = new[i][rows-1-j]
        

        self.history.append(result)
        self.pointer += 1
        self.screen = result

        return result
    
    def horizontal_reflex(self) -> list:
        rows, columns = len(self.screen), len(self.screen[0])
        result = [[0]*columns for _ in range(rows)]
        
        for i in range(rows):
            for j in range(columns):
                result[i][columns-1-j] = self.screen[i][j]
        
        self.history.append(result)
        self.pointer += 1
        self.screen = result

        return result

    def vertical_reflex(self) -> list:
        rows, columns = len(self.screen), len(self.screen[0])
        result = [[0]*columns for _ in range(rows)]
        for row in range(rows):
            result[rows-1-row] = self.screen[row]
        
        self.history.append(result)
        self.pointer += 1
        self.screen = result

        return result
    
    def undo(self) -> list:
        result = []
        
        if self.pointer > 0:
            self.pointer -= 1

        self.screen = self.history[self.pointer]
        result = self.screen

        return result

    def redo(self) -> list:
        result = []
        
        if self.pointer < len(self.history) - 1:
            self.pointer += 1

        self.screen = self.history[self.pointer]
        result = self.screen

        return result
    
    def high_contrast(self) -> list:
        rows, columns = len(self.screen), len(self.screen[0])
        result = [[0]*columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                element = self.screen[i][j]
                result[i][j] = 0 if element <= 4 else 9

        self.history.append(result)
        self.pointer += 1
        self.screen = result
        return result
        
    def invert(self) -> list:
        rows, columns = len(self.screen), len(self.screen[0])
        result = [[0]*columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                element = self.screen[i][j]
                result[i][j] = 9-element

        self.history.append(result)
        self.pointer += 1
        self.screen = result
        return result
    
    def ascii_art(self) -> str:
        result = ""
        for row in self.screen:
            for element in row:
                result += self.ascii_values[element]
            result += "\n"
        return result
    
    
    def save_image_as(self, name) -> None:
        with open(f"{name}.txt", "w") as file:
            result = ""
            for row in self.screen:
                for index, element in enumerate(row):
                    result += f"{element}," if index < len(row)-1 else f"{element}"
                result += "\n"
            file.write(result)
    
    def load_image(self, name) -> list:
        try:
            with open(f"{name}.txt", "r") as file:
                rows = file.read().split()
                self.screen = []
                for row in rows:
                    auxiliar_row = []
                    elements = row.split(",")
                    for element in elements:
                        auxiliar_row.append(int(element))
                    self.screen.append(auxiliar_row)
                return self.screen
        except FileNotFoundError:
            return []



    def __str__(self) -> str:
        """
        Imprime la matriz de la pantalla
        """
        matr = "["
        matr_to_print = self.screen 

        rows, columns = len(matr_to_print), len(matr_to_print[0])
        
        for i in range(rows):
            for j in range(columns):
                if j >= columns-1 and i >= rows-1:
                    matr += f" {matr_to_print[i][j]}]\n"
                elif j >= columns-1:
                    matr += f" {matr_to_print[i][j]}\n"
                elif i >= 1:
                    matr += f" {matr_to_print[i][j]} "
                elif j == 0 and i == 0:
                    matr += f"{matr_to_print[i][j]} "
                else:
                    matr += f" {matr_to_print[i][j]} "
        return matr
