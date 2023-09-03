import matplotlib.pyplot as plt
import random
import time

# To Generate random data to be sorted
data = [random.randint(1, 100) for _ in range(10)]

# Function to perform bubble sort and record each step
def bubble_sort_with_steps(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            steps.append(list(arr))  # Record the current state of the array
        if not swapped:
            break
    return steps

# To Perform Bubble Sort and record steps
steps = bubble_sort_with_steps(data.copy())

# To Create a figure and axis for plotting
fig, ax = plt.subplots()

# Function to update the plot for each step
def update_plot(step):
    ax.clear()
    ax.bar(range(len(step)), step, color='skyblue')
    ax.set_title('Bubble Sort Visualization')
    plt.pause(0.1)

# To Plot each step
for step in steps:
    update_plot(step)

# To Keep the plot open
plt.show()
