
class PaintxelCanvas:
    def __init__(self, screen: list) -> None:
        """
        Esta clase permite controlar de manera sencilla la matriz
        del editor
        """
        # Pantalla que muestra
        self.screen = screen
        
        # Historial de cambios a la pantalla 
        self.history = []
        self.last = 0 
        
        # Esta es la pantalla modificada actual. Esta se agrega a self.history 
        # cada vez que hay un cambio
        self.modified_screen = []
        self.previous_screen = screen
        
        # Poner en true para que la función de __str__ muestre la matriz modificada en vez de la pantalla normal
        self.show_modified = False
    
    def rotate_left(self) -> list:
        """
        Rota a la izquierda la matriz
        """
        rows, columns = len(self.screen), len(self.screen[0])
        new = [[0]*rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                new[j][i] = self.screen[i][columns-1-j]

        if self.modified_screen:
            self.previous_screen = self.modified_screen

        self.modified_screen = new
        self.history.append(self.previous_screen)

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
        

        if self.modified_screen:
            self.previous_screen = self.modified_screen

        self.modified_screen = result
        self.history.append(self.previous_screen)

        return result
    
    def __str__(self) -> str:
        """
        Imprime la matriz de la pantalla
        """
        matr = "["
        matr_to_print = self.screen 
        
        if self.modified_screen and self.show_modified:
            matr_to_print = self.modified_screen

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
    
    
    


# Interfaz para probar el backend, testeo de rotar a la izquierda y derecha
if __name__ == "__main__":
    screen = PaintxelCanvas(
        screen=[
            [1, 2, 5, 6, 1],
            [3, 2, 5, 6, 1],
            [2, 2, 6, 6, 1],
            [1, 3, 5, 6, 1],
        ]
    )
    print(f"Pantalla sin modificar:\n{str(screen)}")
    screen.show_modified = True
    screen.rotate_right()
    print(f"Rotada a la derecha:\n{str(screen)}")
    screen.rotate_left()
    print(f"Rotada a la izquierda:\n{str(screen)}")
