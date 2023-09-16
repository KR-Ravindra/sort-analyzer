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

    return arr, steps, (time.time() - start)

# Python program for implementation of MergeSort


def merge_sort(arr):
    steps = []
    start = time.time()
    steps.append(list(arr))               
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]

		# Into 2 halves
        R = arr[mid:]

		# Sorting the first half
        merge_sort(L)

		# Sorting the second half
        merge_sort(R)

        i = j = k = 0

		# Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
		# Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    steps.append(list(arr))               
    return arr, steps, (time.time() - start)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    steps = []
    start = time.time()
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        steps.append(list(arr))
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append(list(arr))
        heapify(arr, i, 0)
    return arr, steps, (time.time() - start)


def radix_sort(arr):
    steps = []
    start = time.time()
    max_num = max(arr)
    exp = 1
    n = len(arr)
    output = [0] * n
    
    while max_num // exp > 0:
        counting = [0] * 10
        for i in arr:
            counting[(i // exp) % 10] += 1
        for i in range(1, 10):
            counting[i] += counting[i-1]
        for i in range(n-1, -1, -1):
            output[counting[(arr[i] // exp) % 10] - 1] = arr[i]
            counting[(arr[i] // exp) % 10] -= 1
            steps.append(list(arr))
        for i in range(n):
            arr[i] = output[i]
        exp *= 10
        steps.append(list(arr))
    return arr, steps, (time.time() - start)

def counting_sort(arr):
    steps = []
    start = time.time()
    max_v = max(arr)
    count = [0] * (max_v + 1)
    output = [-1] * len(arr)
    for i in arr:
        count[i] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        steps.append(list(arr))
        count[arr[i]] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
        
    return arr, steps, (time.time() - start)


def bucket_sort(arr):
    steps = []
    start = time.time()
    if len(arr) == 0:
        return arr

    # Find the minimum and maximum values in the input array
    min_v, max_v = min(arr), max(arr)
    
    # Calculate the range of values in the array
    value_range = max_v - min_v

    # Determine the number of buckets
    bucket_count = len(arr)

    # Initialize the buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_v) / (value_range / (bucket_count - 1)))
        buckets[index].append(num)

    # Sort each bucket (you can use any sorting algorithm here)
    for i in range(bucket_count):
        buckets[i].sort()

    # Concatenate the sorted buckets to get the final sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
        steps.append(list(arr))

    return sorted_arr, steps, (time.time() - start)



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