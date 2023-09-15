import time

def bubble_sort(unsorted_elements: list):
    """
    Implementing bubble sort. Sorters object call this function.
    
    Input: List of integers
    Output: Sorted Array, List of arrays (every iteration during sort), execution time
    """
    steps = []  # Initializing an empty list to record intermediate steps during sorting
    start = time.time()  # Recording the current time to measure execution time
    arr = unsorted_elements  # Creating a copy of the input list 'unsorted_elements' to sort
    n = len(arr)  # Calculating the length of the list 'arr'
    
    # Iterating through the list 'arr' 'n' times
    for i in range(n):
        swapped = False  # Initializing a flag to False to track whether any swaps were made
        
        # Iterating through the unsorted portion of the list
        for j in range(0, n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Setting the flag to True to indicate a swap occurred
                steps.append(list(arr))  # Appending a copy of the current state of 'arr' to 'steps'
        
        # If no swaps were made in a pass, the list is already sorted, so break out of the loop
        if not swapped:
            break
    
    # Returning the sorted 'arr', the list of intermediate steps, and the execution time
    return arr, steps, (time.time() - start)


def insertion_sort(arr):
    """
    Implementing insertion sort. Sorters object call this function.
    
    Input: List of integers
    Output: Sorted Array, List of arrays (every iteration during sort), execution time
    """
    
    steps = []  # Creating an empty list to record intermediate steps during sorting
    start = time.time()  # Recording the current time to measure execution time
    
    # Looping through the input list 'arr' starting from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Storing the current element at index 'i' in the variable 'key'
        j = i - 1  # Initializing a variable 'j' to the previous index of 'i'
        
        # Comparing 'key' with the elements before it until we find the correct position
        # or reach the beginning of the list
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shifting elements to the right to make space for 'key'
            j -= 1  # Move 'j' one position to the left
        
        arr[j + 1] = key  # Placing 'key' in its correct sorted position in the list
        steps.append(list(arr))  # Appending a copy of the current state of 'arr' to 'steps'
    
    # Returning the sorted 'arr', the list of intermediate steps, and the execution time
    return arr, steps, (time.time() - start)



def quick_sort(arr):
    """
    Implementing Quick Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """

    # Defininig a helper function for partitioning the array
    def partition(arr, low, high, steps):
        pivot = arr[high]  # Choosing the pivot element (typically the last element)
        i = low - 1  # Initializing an index 'i' to the left of the subarray

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1  # Incrementing 'i' when a smaller element is found
                arr[i], arr[j] = arr[j], arr[i]  # Swaping 'arr[i]' and 'arr[j]'
                steps.append(list(arr))  # Appending a copy of 'arr' to 'steps' after each swap

        # Swaping the pivot element with the element at 'i + 1' to place the pivot in its final position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(list(arr))  # Appending the final state of 'arr' after partitioning

        return i + 1  # Returning the index of the pivot element after partitioning

    # Defininig the main recursive quick sort function
    def quick_sort_recursive(arr, low, high, steps):
        if low < high:
            pivot_index = partition(arr, low, high, steps)  # Getting the pivot index
            # Recursively sort the subarrays to the left and right of the pivot
            quick_sort_recursive(arr, low, pivot_index - 1, steps)
            quick_sort_recursive(arr, pivot_index + 1, high, steps)

    steps = []  # Initializing an empty list to record the intermediate states of 'arr'
    start = time.time()  # Recording the current time to measure execution time

    quick_sort_recursive(arr, 0, len(arr) - 1, steps)  # Calling the recursive quick sort function

    # Returning the sorted 'arr', the list of intermediate steps, and the execution time
    return arr, steps, (time.time() - start)





def merge_sort(arr):
    """
    Implementing Quick Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """
    
    steps = []  # Initializing an empty list to record intermediate steps during sorting
    start = time.time()  # Recording the current time to measure execution time
    steps.append(list(arr))  # Appending a copy of the initial state of 'arr' to 'steps'

    if len(arr) > 1:
        mid = len(arr) // 2  # Calculating the middle index of the array
        L = arr[:mid]  # Spliting the array into two halves: L and R
        R = arr[mid:]

        # Recursively sort the first half (L) and the second half (R)
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0  # Initializing indices for merging the two halves

        # Merging the two sorted halves back into 'arr'
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any elements were left in either L or R
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        steps.append(list(arr))  # Appending a copy of the final sorted state of 'arr' to 'steps'

    return arr, steps, (time.time() - start)  # Returning the sorted 'arr', 'steps', and execution time


def heapify(arr, n, i):
    """
    Implementsing Quick Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """
    largest = i  # Initializing the largest element as the root
    l = 2 * i + 1  # Calculating the left child index
    r = 2 * i + 2  # Calculating the right child index

    # If the left child exists and is greater than the largest element so far, update 'largest'
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If the right child exists and is greater than the largest element so far, update 'largest'
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If the largest element is not the root, swap the root with the largest element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    steps = []  # Initializing an empty list to record intermediate steps during sorting
    start = time.time()  # Recording the current time to measure execution time
    n = len(arr)  # Calculating the length of the input array

    # Building a max-heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        steps.append(list(arr))
        heapify(arr, n, i)

    # Extracting elements from the max-heap one by one and place them in their correct positions
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swaping the root (maximum) element with the last element
        steps.append(list(arr))
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr, steps, (time.time() - start)  # Returning the sorted 'arr', 'steps', and execution time



def radix_sort(arr):
    """
    Implementing Quick Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """
    steps = []  # Initializing an empty list to record intermediate steps during sorting
    start = time.time()  # Recording the current time to measure execution time
    max_num = max(arr)  # Finding the maximum number in the input array
    exp = 1  # Initializing the current digit place (1s, 10s, 100s, etc.)
    n = len(arr)  # Calculating the length of the input array
    output = [0] * n  # Creating an empty output array to store the sorted elements
    
    # Entering a loop that continues until all digits of the maximum number have been processed
    while max_num // exp > 0:
        counting = [0] * 10  # Initializing an array to count the occurrences of each digit (0-9)

        # Iterating through the elements of the input array 'arr'
        for i in arr:
            # Calculating the digit at the current digit place and increment the corresponding count
            counting[(i // exp) % 10] += 1

        # Calculating cumulative counts to determine positions of elements in the output array
        for i in range(1, 10):
            counting[i] += counting[i - 1]

        # Iterating through the input array 'arr' in reverse order
        for i in range(n - 1, -1, -1):
            # Placing each element in its correct sorted position in 'output'
            output[counting[(arr[i] // exp) % 10] - 1] = arr[i]
            # Decrementing the corresponding count in 'counting' to account for the placed element

        # Copying the sorted elements from 'output' back to the original 'arr'
        for i in range(n):
            arr[i] = output[i]

        # Moving to the next digit place (e.g., from 1s to 10s, 10s to 100s, etc.)
        exp *= 10
        
        # Appending a copy of the current state of 'arr' to the 'steps' list to record the intermediate step
        steps.append(list(arr))

    # Returning the sorted 'arr', the list of intermediate steps ('steps'), and the execution time
    return arr, steps, (time.time() - start)


def counting_sort(arr):
    """
    Implementing Quick Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """
    steps = []  # Initializing an empty list to record intermediate steps during sorting
    start = time.time()  # Recording the current time to measure execution time
    max_val = max(arr)  # Finding the maximum value in the input array
    count = [0] * (max_val + 1)  # Creating a counting array with size (max_val + 1)
    output = [-1] * len(arr)  # Creating an output array with the same length as the input 'arr'

    # Counting the occurrences of each element in the input array 'arr'
    for i in arr:
        count[i] += 1

    # Calculating cumulative counts in the counting array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Iterating through the input array 'arr' in reverse order
    for i in range(len(arr) - 1, -1, -1):
        # Placing each element in its correct sorted position in the 'output' array
        output[count[arr[i]] - 1] = arr[i]
        # Appening a copy of the current state of 'arr' to 'steps' to record the intermediate step
        steps.append(list(arr))
        # Decrementing the corresponding count in the counting array to account for the placed element
        count[arr[i]] -= 1

    # Copying the sorted elements from 'output' back to the original input 'arr'
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr, steps, (time.time() - start)  # Returning the sorted 'arr', 'steps', and execution time



def bucket_sort(arr):
    """
    Implementing Bucket  Sort. Sorters object call this function.

    Input: List of integers
    Output: Sorted Array, List of arrays (every partition during sort), execution time
    """
    steps = []
    start = time.time()
    if len(arr) == 0:
        return arr

    # Finding the minimum and maximum values in the input array
    min_val, max_val = min(arr), max(arr)
    
    # Calculating the range of values in the array
    value_range = max_val - min_val

    # Determining the number of buckets
    bucket_count = len(arr)

    # Initializing the buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distributing elements into buckets
    for num in arr:
        index = int((num - min_val) / (value_range / (bucket_count - 1)))
        buckets[index].append(num)

    # Sorting each bucket (you can use any sorting algorithm here)
    for i in range(bucket_count):
        buckets[i].sort()

    # Concatenating the sorted buckets to get the final sorted array
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