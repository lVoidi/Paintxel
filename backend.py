
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
    
    def get_transposed(self) -> list:
        rows, columns = len(self.screen), len(self.screen[0])
        new = [[0]*rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                new[j][i] = self.screen[i][j]

        if self.modified_screen:
            self.previous_screen = self.modified_screen

        self.modified_screen = new
        self.history.append(self.previous_screen)

        return new
    
    def show_mat(self) -> str:
        matr = "["
        matr_to_print = self.screen 
        
        if self.modified_screen:
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
    

# Interfaz para probar el backend, testeo de la traspuesta
if __name__ == "__main__":
    screen = PaintxelCanvas(
        screen=[
            [1, 2, 5, 6, 1],
            [3, 2, 5, 6, 1],
            [2, 2, 6, 6, 1],
            [1, 3, 5, 6, 1],
        ]
    )
    screen.get_transposed()
    print(screen.show_mat())

