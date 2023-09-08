import time

def bubble_sort(unsorted_elements: list):
    """
    Implements bubble sort. Sorters object call this function.
    
    Input: List of integers
    Output: Sorted Array, List of arrays (every iteration during sort), execution time
    """
    steps = [] # Recording initialization for steps
    start = time.time() # Recording start time 
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
    return arr, steps, (time.time() - start)

def insertion_sort(arr):
    """
    Implements implementation sort. Sorters object call this function.
    
    Input: List of integers
    Output: Sorted Array, List of arrays (every iteration during sort), execution time
    """
    steps = [] # Recording initialization for steps
    start = time.time() # Recording start time 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        steps.append(list(arr)) # Appends into the recording, each time the items are altered 
    return arr, steps, (time.time() - start)

import time

def quick_sort(arr):
    """
    Implements Quick Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """
    def partition(arr, low, high, steps):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(list(arr))

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(list(arr))

        return i + 1

    def quick_sort_recursive(arr, low, high, steps):
        if low < high:
            pivot_index = partition(arr, low, high, steps)
            quick_sort_recursive(arr, low, pivot_index - 1, steps)
            quick_sort_recursive(arr, pivot_index + 1, high, steps)

    steps = []  # Recording initialization for steps
    start = time.time()  # Recording start time

    quick_sort_recursive(arr, 0, len(arr) - 1, steps)

    return arr, steps, time.time() - start


class Sorters():
    """
    Responsible for calling each algorithm. This is exposed to visualizer.
    Workflow: UserInput/GUI >> Visualizer >> Sorters
    
    Initialization Parameters: algo_choice: Choice of Algorithm, unsorted_elements: List
    """
    def __init__(self, unsorted_elements: list) -> None:
        self.unsorted_elements = unsorted_elements
    
    def start_sorting(self, algo_choice: str):
        # To start sorting, called by instance of visualizer
        self.function = eval(algo_choice) # "insertion_sort" > insertion_sort
        return self.function(self.unsorted_elements) # return insertion_sort(unsorted_elements)
    
if __name__ == "__main__":
    pass