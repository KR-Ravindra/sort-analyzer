# Import Module
from tkinter import *
import tkinter as tk
import random
  
# create root window
root = Tk()


# root window title and dimension
root.title("Algorithm Efficiency Analyzer Tool")
root.state('zoomed')

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
