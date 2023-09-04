from plotter.visualizer import Visualizer

if __name__ == "__main__":
    """Invokes when this application is called; by defaults asks for user input of an array and sort algo,
    if not defaults to a predefined one and calls bubble sort
    """
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if arr == []:
        arr = [10, 3, 15, 2, 19, 6, 56, 12, 19, 23, 38]
        
    visualizer = Visualizer()
    visualizer.call_algo(arr, "bubble_sort")
    visualizer.show_list()