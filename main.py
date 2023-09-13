import tkinter as tk
import time
from ui.gui import App


def centerWindow(width, height, root):  # Return 4 values needed to center Window
    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight() # Height of the screen     
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    return int(x), int(y)

if __name__ == "__main__":
    """Invokes when this application is called; by defaults asks for user input of an array and sort algo,
    if not defaults to a predefined one and calls bubble sort
    """

    app = App()
    app.title("Sorting Visualizer")
    app.mainloop()
