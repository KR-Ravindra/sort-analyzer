import matplotlib.pyplot as plt
from algorithms.sorters import Sorters

class Visualizer():
    """
    Responsible for calling sorters. This is exposed to end-user/GUI.
    Workflow: UserInput/GUI >> Visualizer >> Sorters
    
    Initialization Parameters: None
    """
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
    
    def call_algo(self, unsorted_elements: list, algo_choice: str, speed: int = 1):
        """Calls sorters for each algorithm

        Args:
            unsorted_elements (list): List of Unsorted elements
            algo_choice (string): Algorithm Name (allowed values: bubble_sort)
        """
        self.algo_choice = algo_choice
        self.dataset = unsorted_elements
        self.no_of_elements = len(self.dataset)
        
        sorters = Sorters(self.algo_choice, unsorted_elements)
        _, steps_recording = sorters.start_sorting() #gets all the iterations from sorters instance
        
        for step in steps_recording: # plots and records graph for each step
            self.ax.clear()
            bar = self.ax.bar(range(self.no_of_elements), step)
            self.ax.set_title(f'{self.algo_choice} Visualization')
            self.ax.bar_label(bar, labels = step)
            plt.pause(speed) #Implements speed control on UI
        
    def show_list(self):
        # Displays graph, called by instance of GUI
        plt.show()

if __name__ == "__main__":
    print("Visualizer Only Mode!") 
