import tkinter as tk

class FrontApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg = "#ffffff")
        self.geometry("765x750")  
        self.resizable(False, False)

        
        self.canvas_top = tk.Canvas(self, bg="#ffffff", width=700, height=50, background = "#9b9b9b")
        self.canvas_top.grid(column=0, row=0, columnspan=4, sticky="nsew")
        self.canvas_bottom = tk.Canvas(self, bg="#ffffff", width=700, height=50, background=  "#9b9b9b")
        self.canvas_bottom.grid(column=0, row=2, columnspan=4, sticky="nsew")

       
        self.color1 = tk.Button(self, text = "Prueba", bg="#000000", fg="#ffffff", width=10)
        self.color1.grid(column=0, row=1)
        self.color2 = tk.Button(self, text = "Prueba", bg="#000000", fg="#ffffff", width=10)
        self.color2.grid(column=3, row=1)  

        
        self.canvas = tk.Canvas(self, bg="#ffffff", width=600, height=600)
        self.canvas.grid(column=1, row= 1, sticky="nsew")

        for i in range(12):
            for j in range(12):
                self.canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50)

app = FrontApp()
app.mainloop()
