import customtkinter
import random
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk


class App(customtkinter.CTk):
    '''
    This class is responsible for creating the GUI and handling the events
    Workflow: UserInput/GUI >> Visualizer >> Sorters
    '''
    def __init__(self):
        super().__init__()        
        self.display=False

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")
        self.title("SORTING VISUALIZER")
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
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Sorting Visualizer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.left_sidebar_frame, dynamic_resizing=False,
                                                      values=["Bubble Sort","Bucket Sort","Counting Sort","Heap Sort","Insertion Sort","Merge Sort","Quick Sort","Radix Sort"])

        self.optionmenu_1.grid(row=1, column=0, padx=20, pady= 10)
        self.entry = customtkinter.CTkEntry(self.left_sidebar_frame, placeholder_text="Enter Input")
        self.entry.grid(row=2, column=0,  padx=20, pady=10, sticky="nsew")
        self.sorting_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_button_event, text="Sort Me")
        self.sorting_button.grid(row=3, column=0, padx=20, pady=10)
        self.random_input_btn = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_random_array, text="Random Input")
        self.random_input_btn.grid(row=4, column=0, padx=20, pady=10)

        
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.optionmenu_1.set("Select Algorithms")
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")

        self.quit_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="QUIT", command=self.destroy_panel)
        self.quit_button.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        if not self.display:
            image_path="ui/test_images/minion_home_screen.png"
            # Open the image using PIL
            image = Image.open(image_path)
            image_path1="ui/test_images/minion_home_screen.png"
            darkimage = Image.open(image_path1)
            # Create a CTkImage object with the image and size
            custom_image = customtkinter.CTkImage(light_image=image, dark_image=darkimage, size=(800, 600))
            # Create a CTkLabel widget to display the image
            label = customtkinter.CTkLabel(self, image=custom_image)
            label.grid(row=0, column=1, rowspan=2, sticky="nsew")

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
        self.display=True
        # Retrieve the value of input_var
        self.entered_input = self.entry.get()
        try: 
            self.entered_input = [int(num.strip()) for num in self.entered_input.split(",")]
        except Exception as ex:
            CTkMessagebox(title="Error", message=f"Invalid input! Try again!!\n Exception: {ex}", icon="cancel")
            self.entry.delete(0, "end")  

        self.input_array = self.entered_input.copy()
    
        from plotter.visualizer import Visualizer
        self.visualizer = Visualizer(self.entered_input)
        # runs in background; doesnt interrupt process flow
        try:
            _, self.sorted_array, self.execution_time, self.steps_recording = self.visualizer.call_algo(self.optionmenu_1.get().lower().replace(" ","_"))
            self.final_array = self.sorted_array.copy()
            self.figure = self.visualizer.compare_algo()
        except Exception as ex:
            CTkMessagebox(title="Error", message=f"Invalid input! Try again!!\n Exception: {ex}", icon="cancel")
            self.entry.delete(0, "end") 

        msg=CTkMessagebox(title="Sorted",message=f"Given Input: {self.input_array}\nSorted Array: {self.final_array}\nAlgorithm: {self.optionmenu_1.get()}\nTime Taken: {self.execution_time}",
                icon="check", options=["Compare", "Get Steps", "Live"], width = 700, height = 300, fade_in_duration = 4)

        if msg.get()=="Compare":
            self.compare_with_other_algorithms()
        
        if msg.get()=="Get Steps":
            self.get_steps()
        # self.entry.delete(0, "end") 

        if msg.get()=="Live":
            self.watch_live()


    def watch_live(self):
        self.visualizer.call_algo_with_live()
        msg=CTkMessagebox(title="Sorted",message=f"Given Input: {self.input_array}\nSorted Array: {self.sorted_array}\nAlgorithm: {self.optionmenu_1.get()}\nTime Taken: {self.execution_time}",
                icon="check", options=["Compare", "Get Steps", "Live"], width = 700, height = 300, fade_in_duration = 4)

        if msg.get()=="Compare":
            self.compare_with_other_algorithms()
        
        if msg.get()=="Get Steps":
            self.get_steps()
        # self.entry.delete(0, "end") 

        if msg.get()=="Live":
            self.watch_live()

    def get_steps(self):
        all_steps=""
        for i, sublist in enumerate(self.steps_recording, start=1):
            all_steps = all_steps+f"Step{i}: {sublist}\n"
        
        if len(self.steps_recording)>15:
            all_steps = all_steps.replace(all_steps.split("\n")[5], "...")
            all_steps = all_steps.replace(all_steps.split("\n")[-5], "...")
            all_steps = "\n".join(all_steps.split("\n")[:6]+all_steps.split("\n")[-5:])
        msg = CTkMessagebox(title="Steps", message=all_steps, 
                            icon="info", option_1="Compare with other algorithms", option_2="No! I am good!", width = 700, height = 300, fade_in_duration = 4)
        
        self.entry.delete(0, "end")  
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
        
        canvas = FigureCanvasTkAgg(self.figure , master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        self.entry.delete(0, "end")

        
        
    
    def generate_random_array(self):
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(10)]
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
