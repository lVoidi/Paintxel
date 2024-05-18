
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
    
    def get_transposed(self) -> list:
        rows, columns = len(self.screen), len(self.screen[0])
        new = [[0]*rows for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                new[j][i] = self.screen[i][j]
        return new

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

    print(f"""
Matriz: {screen.screen},
Transpuesta: {screen.get_transposed()}
    """)

