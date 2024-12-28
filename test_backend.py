import unittest
from backend import PaintxelCanvas

class TestPaintxelCanvas(unittest.TestCase):
    def setUp(self):
        # Matriz de prueba 3x3 para hacer los tests más manejables
        self.test_screen = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.canvas = PaintxelCanvas(self.test_screen, 3)

    def test_rotate_left(self):
        expected = [
            [2, 5, 8],
            [1, 4, 7],
            [0, 3, 6]
        ]
        result = self.canvas.rotate_left()
        self.assertEqual(result, expected)

    def test_rotate_right(self):
        expected = [
            [6, 3, 0],
            [7, 4, 1],
            [8, 5, 2]
        ]
        result = self.canvas.rotate_right()
        self.assertEqual(result, expected)

    def test_horizontal_reflex(self):
        expected = [
            [2, 1, 0],
            [5, 4, 3],
            [8, 7, 6]
        ]
        result = self.canvas.horizontal_reflex()
        self.assertEqual(result, expected)

    def test_vertical_reflex(self):
        expected = [
            [6, 7, 8],
            [3, 4, 5],
            [0, 1, 2]
        ]
        result = self.canvas.vertical_reflex()
        self.assertEqual(result, expected)

    def test_high_contrast(self):
        test_screen = [
            [0, 4, 5],
            [3, 6, 9],
            [2, 7, 8]
        ]
        canvas = PaintxelCanvas(test_screen, 3)
        expected = [
            [0, 0, 9],
            [0, 9, 9],
            [0, 9, 9]
        ]
        result = canvas.high_contrast()
        self.assertEqual(result, expected)

    def test_invert(self):
        test_screen = [
            [0, 4, 5],
            [3, 6, 9],
            [2, 7, 8]
        ]
        canvas = PaintxelCanvas(test_screen, 3)
        expected = [
            [9, 5, 4],
            [6, 3, 0],
            [7, 2, 1]
        ]
        result = canvas.invert()
        self.assertEqual(result, expected)

    def test_clear_screen(self):
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = self.canvas.clear_screen()
        self.assertEqual(result, expected)

    def test_ascii_art(self):
        test_screen = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        canvas = PaintxelCanvas(test_screen, 3)
        expected = " .:\n-=¡\n&$%\n"
        result = canvas.ascii_art()
        self.assertEqual(result, expected)

    def test_save_and_load_image(self):
        # Test save
        self.canvas.save_image_as("test_image")
        
        # Test load
        loaded_screen = self.canvas.load_image("test_image.txt")
        self.assertEqual(loaded_screen, self.test_screen)

    def test_load_nonexistent_image(self):
        result = self.canvas.load_image("nonexistent_file.txt")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main() 