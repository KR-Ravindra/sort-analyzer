import customtkinter
import os
from PIL import Image
import tkinter
import tkinter as tk
import random
import re
from CTkMessagebox import CTkMessagebox

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")
        self.title("SORT ANALYZER")
        # self.geometry("700x600")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="SortAnalyzer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                      values=["Insertion Sort", "Bubble Sort", "Counting Sort","Heap Sort","Quick Sort","Merge Sort"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady= 10)

        self.entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Input", validate="key", validatecommand=(self.validate_command, '%P'))
        self.entry.grid(row=2, column=0,  padx=20, pady=10, sticky="nsew")
        # Bind the <<Modified>> event to the entry widget
        self.entry.bind("<<Modified>>", self.entry_modified)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.generate_button_event, text="Generate")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.generate_random_array, text="Random Input")
        self.sidebar_button_1.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="QUIT", command=self.destroy_panel)
        self.main_button_1.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Algorithms")
        self.combobox_1.set("CTkCombobox")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

   

    def validate_command(self,data):
        
        # If the input is empty or matches the pattern of comma-separated integers
        if data == re.match(r'^(\d+(,\s*\d+)*)?$',str(data)):
            return True
        else:
            print('Invalid Input')
            return False
        
    def entry_modified(self, event):
        # Check if the entry content is not empty
        if self.entry.get():
            self.sidebar_button_3.configure(state="normal")
        else:
            self.sidebar_button_3.configure(state="disabled")

    def generate_button_event(self):
      # Retrieve the value of input_var
        self.entered_input = self.entry.get()
       
        try: 
            self.entered_input = [int(num.strip()) for num in self.entered_input.split(",")]
        except Exception as ex:
            CTkMessagebox(title="Error", message=f"Invalid input! Try again!!\n Exception: {ex}", icon="cancel")
            return

    
        from plotter.visualizer import Visualizer
        self.visualizer = Visualizer(self.entered_input)
        try:
            _ = self.visualizer.compare_algo()
        except Exception as ex:
            print(f"Exception occured, Given function is not defined {ex}")

        if True:
            msg=CTkMessagebox(message="Sorted Array.",
                  icon="check", option_1="Compare with other algorithms")

            if msg.get()=="Compare with other algorithms":
                    import tkinter as tk
                    from tkinter import ttk
                    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
                    from plotter.visualizer import Visualizer
                    
                    self.canvas_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
                    self.canvas_frame.grid(row=0, column=1, rowspan=7, sticky="nsew")
                    self.canvas_frame.grid_rowconfigure(4, weight=1)
                    # self.canvas_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
                    
                    # Create a FigureCanvasTkAgg widget
                    figure =  self.visualizer.compare_algo()
                    canvas = FigureCanvasTkAgg(figure , master=self.canvas_frame)
                    canvas_widget = canvas.get_tk_widget()
                    canvas_widget.pack(fill=tk.BOTH, expand=True)
        else:
            CTkMessagebox(title="Error", message="Invalid input! Try again!!", icon="cancel")
        self.entry.delete(0, "end") 

        

    def generate_random_array(self):
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(10)]
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))
        # Update the Entry widget with the generated array
        self.entry.delete(0, "end")  # Clear the previous content
        self.entry.insert(0, array_str)
      
    
    def destroy_panel(self):
        self.destroy()   
             
if __name__ == "__main__":
    app = App()
    app.mainloop()
