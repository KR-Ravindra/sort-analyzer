import re

import customtkinter
import random
from CTkMessagebox import CTkMessagebox
from tkinter import *
from tkinter import messagebox

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("green")
        self.title("SORT ANALYZER")
        x, y = self.center_window(800, 600)
        self.geometry(f"800x600+{x}+{y}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create Leftsidebar frame with widgets
        self.left_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="SortAnalyzer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.left_sidebar_frame, dynamic_resizing=False,
                                                      values=["Insertion Sort", "Bubble Sort", "Counting Sort","Heap Sort","Quick Sort","Merge Sort"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady= 10)
        vcmd = (self.left_sidebar_frame.register(self.callback))

        ###############33
        # self.entry = Entry(self.left_sidebar_frame, validate='key', validatecommand=(vcmd, '%P'))
        # self.entry.grid()

        ###############3


        self.entry = customtkinter.CTkEntry(self.left_sidebar_frame, placeholder_text="Enter Input")
        self.entry.grid(row=2, column=0,  padx=20, pady=10, sticky="nsew")
        self.sorting_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_button_event, text="Sorting")
        self.sorting_button.grid(row=3, column=0, padx=20, pady=10)
        self.random_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Random Inputs",
                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
        self.random_label.grid(row=4, column=0, padx=20, pady=(20, 10))
        self.random_input_btn_100 = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_random_array_100,
                                                        text="100")
        self.random_input_btn_100.grid(row=5, column=0, padx=20, pady=10)
        self.random_input_btn_1000 = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_random_array_1000,
                                                        text="1000")
        self.random_input_btn_1000.grid(row=5, column=1, padx=10, pady=10)
        self.random_input_btn_10000 = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_random_array_10000,
                                                        text="10000")
        self.random_input_btn_10000.grid(row=6, column=0, padx=10, pady=10)
        self.random_input_btn_100000 = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_random_array_100000,
                                                        text="100000")
        self.random_input_btn_100000.grid(row=6, column=1, padx=10, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        self.optionmenu_1.set("Select Algorithms")
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")

        self.quit_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="QUIT", command=self.destroy_panel)
        self.quit_button.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def callback(self, P):
        # print(P, "========")
        # Custom validation function to allow only valid comma-separated integers
        if P == "" or re.match(r'^\d+(,\d+)*$', P.replace(",", "")):
            return True
        else:
            messagebox.showerror("Invalid Input", "Please enter valid comma-separated integers.")
            return False

    def center_window(self,width, height):  # Return for values needed to center Window
        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen     
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        return int(x), int(y)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def generate_button_event(self):
      # Retrieve the value of input_var
        self.entered_input = self.entry.get()
        try: 
            self.entered_input = [int(num.strip()) for num in self.entered_input.split(",")]
        except Exception as ex:
            CTkMessagebox(title="Error", message=f"Invalid input! Try again!!\n Exception: {ex}", icon="cancel")
            self.entry.delete(0, "end")  

        input_array = self.entered_input.copy()
    
        from plotter.visualizer import Visualizer
        self.visualizer = Visualizer(self.entered_input)
        # runs in background; doesnt interrupt process flow
        try:
            _, self.sorted_array, self.execution_time, self.steps_recording = self.visualizer.call_algo(self.optionmenu_1.get().lower().replace(" ","_"))
            _ = self.visualizer.compare_algo()
        except Exception as ex:
            CTkMessagebox(title="Error", message=f"Invalid input! Try again!!\n Exception: {ex}", icon="cancel")
            self.entry.delete(0, "end") 

        msg=CTkMessagebox(message=f"Given Input: {input_array}\nSorted Array: {self.sorted_array}\nAlgorithm: {self.optionmenu_1.get()}\nTime Taken: {self.execution_time}",
                icon="check", option_1="Compare with other algorithms", option_2="No! I am good!", option_3="Get Steps", width = 700, height = 300, fade_in_duration = 4)

        if msg.get()=="Compare with other algorithms":
            self.compare_with_other_algorithms()
        
        if msg.get()=="Get Steps":
            self.get_steps()
        self.entry.delete(0, "end") 

    def get_steps(self):
        all_steps=""
        for i, sublist in enumerate(self.steps_recording, start=1):
            all_steps = all_steps+f"Step{i}: {sublist}\n"
            
        msg=CTkMessagebox(title="Get Steps", message=f"{all_steps}",
            icon="check", option_1="Compare with other algorithms", option_2="Close", width = 700, height = 300, fade_in_duration = 2)
        
        if msg.get()=="Compare with other algorithms":
            self.compare_with_other_algorithms()
        
        
    def compare_with_other_algorithms(self):
        import tkinter as tk
        from tkinter import ttk
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from plotter.visualizer import Visualizer
        
        self.canvas_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.canvas_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.canvas_frame.grid_rowconfigure(4, weight=1)
        # self.canvas_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create a FigureCanvasTkAgg widget
        figure =  self.visualizer.compare_algo()
        canvas = FigureCanvasTkAgg(figure , master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
    
    def generate_random_array_100(self):
        print(self.__dict__, "==========")
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(1000)]
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))
        # Update the Entry widget with the generated array
        self.entry.delete(0, "end")  # Clear the previous content
        self.entry.insert(0, array_str)
        self.optionmenu_1.set("Bubble Sort")

    def generate_random_array_1000(self):
        print(self.__dict__, "==========")
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(1000)]
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))
        # Update the Entry widget with the generated array
        self.entry.delete(0, "end")  # Clear the previous content
        self.entry.insert(0, array_str)
        self.optionmenu_1.set("Bubble Sort")

    def generate_random_array_10000(self):
        print(self.__dict__, "==========")
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(10000)]
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))
        # Update the Entry widget with the generated array
        self.entry.delete(0, "end")  # Clear the previous content
        self.entry.insert(0, array_str)
        self.optionmenu_1.set("Bubble Sort")

    def generate_random_array_100000(self):
        print(self.__dict__, "==========")
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(100000)]
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))
        # Update the Entry widget with the generated array
        self.entry.delete(0, "end")  # Clear the previous content
        self.entry.insert(0, array_str)
        self.optionmenu_1.set("Bubble Sort")
      
    
    def destroy_panel(self):
        self.destroy()   
             
if __name__ == "__main__":
    app = App()
    app.mainloop()
