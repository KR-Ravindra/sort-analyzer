import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Create a Frame to hold the Matplotlib graph
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Function to generate the graph and return the Figure object
def generate_graph():
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4, 5], [2, 3, 5, 7, 11])  # Sample data
    return fig

# Create a Matplotlib figure and canvas widget

canvas = FigureCanvasTkAgg(generate_graph, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Function to update the graph with new data
def update_graph():
    new_data = [1, 4, 6, 8, 9]  # New data
    fig = generate_graph()  # Generate a new figure
    ax = fig.get_axes()[0]  # Get the axis from the new figure
    ax.clear()
    ax.plot([1, 2, 3, 4, 5], new_data)  # Plot the new data
    canvas.get_tk_widget().configure()  # Update the canvas to use the new figure

# Create a button to update the graph
update_button = ttk.Button(root, text="Update Graph", command=update_graph)
update_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
