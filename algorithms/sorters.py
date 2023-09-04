def bubble_sort(unsorted_elements: list) -> list:
    """
    Implements bubble sort. Sorters object call this function.
    
    Input: List of integers
    Output: Sorted Array, List of arrays (every iteration during sort)
    """
    steps = [] # Recording initialization for steps
    arr = unsorted_elements
    n = len(arr)
    for i in range(n):
        swapped =   False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                steps.append(list(arr)) # Appends into the recording, each time the items are altered
        if not swapped:
            break
    return arr, steps


class Sorters():
    """
    Responsible for calling each algorithm. This is exposed to visualizer.
    Workflow: UserInput/GUI >> Visualizer >> Sorters
    
    Initialization Parameters: algo_choice: Choice of Algorithm, unsorted_elements: List
    """
    def __init__(self, algo_choice: str, unsorted_elements: list) -> None:
        self.function = eval(algo_choice)
        self.unsorted_elements = unsorted_elements
    
    def start_sorting(self):
        # To start sorting, called by instance of visualizer
        return self.function(self.unsorted_elements)
    
if __name__ == "__main__":
    pass