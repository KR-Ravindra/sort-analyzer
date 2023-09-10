from plotter.visualizer import Visualizer

if __name__ == "__main__":
    """Invokes when this application is called; by defaults asks for user input of an array and sort algo,
    if not defaults to a predefined one and calls bubble sort
    """

    from ui.gui import App
    app = App()
    app.mainloop()
    exit()