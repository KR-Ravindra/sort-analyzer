import tkinter as tk
import time
from ui.gui import App

if __name__ == "__main__":
    """Invokes when this application is called; by defaults asks for user input of an array and sort algo,
    if not defaults to a predefined one and calls bubble sort
    """

    app = App()
    app.title("Sorting Visualizer")
    app.mainloop()
