# Import Module
from tkinter import *
import tkinter as tk
import random
   
input_entry = ""
def tk_initalize():    
    # create root window
    root = tk.Tk()

    # root window title and dimension
    root.title("Algorithm Efficiency Analyzer Tool")
    # root.state('zoomed')

    input_var=tk.StringVar()

    # adding a label to the root window
    input_label = Label(root, text = 'Input', font=('calibre',10, 'bold'))
    
    # creating a entry for input
    input_entry = Entry(root,textvariable = input_var, width=60,font=('calibre',10,'normal'))

        
    def generate_random_array():
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(10)]
        
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))
        
        # Update the Entry widget with the generated array
        input_entry.delete(0, tk.END)  # Clear the previous content
        input_entry.insert(0, array_str)
    random_button=Button(root, text = "random",
        width = 10, height = 1, command = generate_random_array).grid(row=5, column=2)

    # function to display text when
    # button is clicked
    def clicked():
        # input.configure(text = "I just got clicked")

        input_entry=input_var.get()
        print("The input  is : " + input_entry)
        input_var.set("")
        root.destroy()
        return input_entry



    # button widget with red color text
    # inside

    btn = Button(root, text = "Generate" ,
                fg = "red", command=clicked)
    # set Button grid
    # btn.grid(column=1, row=0)
    input_label.grid(row=0,column=0)
    input_entry.grid(row=0,column=1)


    btn.grid(row=2,column=1)
    # random_button.grid(row=2,column=1)

    # Execute Tkinter
    root.mainloop()

    
def show_data():
    print(f"Input entry I have with me is {input_entry}")
    


# import tkinter

# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg, NavigationToolbar2Tk)
# # Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure

# import numpy as np


# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")

# fig = Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# def on_key_press(event):
#     print("you pressed {}".format(event.key))
#     key_press_handler(event, canvas, toolbar)


# canvas.mpl_connect("key_press_event", on_key_press)


# def _quit():
#     root.quit()     # stops mainloop
#     root.destroy()  # this is necessary on Windows to prevent
#                     # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)

# tkinter.mainloop()