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
        plt.close()
        self.algo_choice = algo_choice
        self.dataset = self.unsorted_elements
        self.no_of_elements = len(self.dataset)
        
        sorted_array, steps_recording, execution_time = self.sorters.start_sorting(self.algo_choice) #gets all the iterations from sorters instance
        
        self.steps_recording = steps_recording

        return self.fig, sorted_array, execution_time, steps_recording
    
    def call_algo_with_live(self, speed: float = 0.5):
        """Calls sorters for each algorithm

        Args:
            algo_choice (string): Algorithm Name (allowed values: bubble_sort)
        """
        plt.close()
        self.fig2, self.ax2 = plt.subplots()
        for step in self.steps_recording: # plots and records graph for each step
            self.ax2.clear()
            # set window title as Live sorting instead of Figure 1
            self.fig2.canvas.manager.set_window_title("Live Sorting")
            
            bar = self.ax2.bar(range(self.no_of_elements), step)
            self.ax2.set_title(f'{self.algo_choice} Visualization')
            self.ax2.bar_label(bar, labels = step)
            plt.pause(speed) #Implements speed control on UI
        plt.close()

    def compare_algo(self):
        self.available_algos = ["bubble_sort", "insertion_sort", "merge_sort", "quick_sort","heap_sort","radix_sort","bucket_sort"]

        execution_times = []
                
        for each_algo in self.available_algos:
            _,_,execution_time = self.sorters.start_sorting(each_algo)
            execution_times.append(execution_time)
        plt.close()
        self.ax.clear()
        bar = self.ax.bar(range(len(self.available_algos)), execution_times)
        self.ax.set_title(f'Sorting Algorithm Comparision')
        self.ax.bar_label(bar, labels = [each_algo.replace("_sort","") for each_algo in self.available_algos], label_type= "edge", fmt='%.5f')
        self.ax.set_xlabel("Sorting Algorithms")
        self.ax.set_ylabel("Execution Time (in power of -5 seconds)")
        
        min_index = execution_times.index(min(execution_times))
        bar[min_index].set_color("green")
        
        self.ax.legend(["Fastest Algorithm"], loc="upper right")
        
        # plot a scatter plot instead of bar graph
        self.ax.scatter(range(len(self.available_algos)), execution_times)
        self.ax.set_xticks(range(len(self.available_algos)))
        self.ax.set_xticklabels([each_algo.replace("_sort","") for each_algo in self.available_algos])
        self.ax.set_yticks(execution_times)
        self.ax.grid(True)
        
        return self.fig

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