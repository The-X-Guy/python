import tkinter as tk

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = MainFrame(container, self)

        self.frames[MainFrame] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainFrame)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class MainFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10,padx=10)

class AddFrame():
    def __init__(self):
        tk.Frame.__init__()


app = MainWindow()
app.mainloop()