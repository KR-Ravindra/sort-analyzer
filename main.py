from plotter.visualizer import Visualizer
import matplotlib.pyplot as plt

if __name__ == "__main__":
    """Invokes when this application is called; by defaults asks for user input of an array and sort algo,
    if not defaults to a predefined one and calls bubble sort
    """
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if arr == []:
        arr = [10, 3, 15, 2, 19, 6, 56, 12, 19, 23, 38]

    visualizer = Visualizer()
    try:
         visualizer.call_algo(arr.copy(), "bubble_sort", 1)
         visualizer.show_list()
         plt.show()

         visualizer.call_algo(arr.copy(), "insertion_sort", 2)
         visualizer.show_list()
         plt.figure()

         visualizer.call_algo(arr.copy(), "quick_sort", 3)
         visualizer.show_list()
         plt.show()




    except Exception as ex:
        print("Exception occured, Given function is not defined")