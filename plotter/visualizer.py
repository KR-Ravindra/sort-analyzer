import matplotlib.pyplot as plt
from algorithms.sorters import Sorters
from matplotlib.figure import Figure


class Visualizer():
    """
    Responsible for calling sorters. This is exposed to end-user/GUI.
    Workflow: UserInput/GUI >> Visualizer >> Sorters
    
    Initialization Parameters: None
    """
    def __init__(self, unsorted_elements: list) -> None:
        # self.fig = Figure(figsize=(6, 4), dpi=100)
        # self.ax = self.fig.add_subplot(111)
        self.unsorted_elements = unsorted_elements
        self.fig, self.ax = plt.subplots()
        self.sorters = Sorters(unsorted_elements)

    
    def call_algo(self, algo_choice: str, speed: int = 1):
        """Calls sorters for each algorithm

        Args:
            algo_choice (string): Algorithm Name (allowed values: bubble_sort)
        """
        self.algo_choice = algo_choice
        self.dataset = self.unsorted_elements
        self.no_of_elements = len(self.dataset)
        
        sorted_array, steps_recording, execution_time = self.sorters.start_sorting(self.algo_choice) #gets all the iterations from sorters instance
        
        # for step in steps_recording: # plots and records graph for each step
        #     self.ax.clear()
        #     bar = self.ax.bar(range(self.no_of_elements), step)
        #     self.ax.set_title(f'{self.algo_choice} Visualization')
        #     self.ax.bar_label(bar, labels = step)
        #     plt.pause(speed) #Implements speed control on UI
        
        return self.fig, sorted_array, execution_time, steps_recording
    
    def compare_algo(self):
        self.available_algos = ["bubble_sort", "insertion_sort"]
        execution_times = []
                
        for each_algo in self.available_algos:
            _,_,execution_time = self.sorters.start_sorting(each_algo)
            execution_times.append(execution_time)
            
        print(execution_times)
        
        self.ax.clear()
        bar = self.ax.bar(range(len(self.available_algos)), execution_times)
        self.ax.set_title(f'Algo Comparision')
        self.ax.bar_label(bar, labels = self.available_algos)
        return self.fig
    
    # def show_list(self):
    #     # Displays graph, called by instance of GUI
    #     plt.show()

        
if __name__ == "__main__":
    print("Visualizer Only Mode!") 

    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if arr == []:
        arr = [10, 3, 15, 2, 19, 6, 56, 12, 19, 23, 38]

    visualizer = Visualizer(arr)
    try:
        _ = visualizer.compare_algo()
        visualizer.show_list()
    except Exception as ex:
        print(f"Exception occured, Given function is not defined {ex}")

