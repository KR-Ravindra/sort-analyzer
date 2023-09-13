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
    app.withdraw()

    # SPLASH SCREEN CODE
    splash_screen = tk.Toplevel(background="white")
    splash_screen.overrideredirect(True)
    splash_screen.title("Splash Screen")
    x, y = centerWindow(800, 600, app)
    splash_screen.geometry(f"400x300+{x}+{y}")

    image = tk.PhotoImage(file="ui/test_images/289687_Algorithm efficiency analyzer tool cartoon for pro_xl-1024-v1-0.png")
    
    label = tk.Label(splash_screen, image = image)    
    label.pack()
    splash_screen.update()

    time.sleep(3)

    # Start the event loop
    app.deiconify()
    splash_screen.destroy()
    app.mainloop()
