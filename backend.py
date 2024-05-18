
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



