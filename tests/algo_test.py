from algorithms.sorters import Sorters


def test_bubble_sort_sorted_array():
    """
    Test that bubble sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters(input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output

def test_bubble_sort_unsorted_array():
    """
    Test that bubble sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]


    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output

def test_bubble_sort_empty_array():
    """
    Test that bubble sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output

def test_bubble_sort_single_element_array():
    """
    Test that bubble sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output

def test_bubble_sort_duplicate_element_array():
    """
    Test that bubble sort correctly sorts an array with duplicate elements.
    """
    input_array = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output

def test_bubble_sort_negative_element_array():
    """
    Test that bubble sort correctly sorts an array with negative elements.
    """
    input_array = [-1, -2, -3, -4, -5]
    expected_output = [-5, -4, -3, -2, -1]


    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output

def test_insertion_sort_sorted_array():
    """
    Test that insertion sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("insertion_sort")

    assert output_array == expected_output

def test_insertion_sort_unsorted_array():
    """
    Test that insertion sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
   
    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("insertion_sort")

    assert output_array == expected_output

def test_insertion_sort_empty_array():
    """
    Test that insertion sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("insertion_sort")

    assert output_array == expected_output

def test_insertion_sort_single_element_array():
    """
    Test that insertion sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("insertion_sort")

    assert output_array == expected_output

def test_insertion_sort_duplicate_element_array():
    """
    Test that insertion sort correctly sorts an array with duplicate elements.
    """
    input_array = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("insertion_sort")

    assert output_array == expected_output
    
def test_insertion_sort_negative_element_array():
    """
    Test that insertion sort correctly sorts an array with negative elements.
    """
    input_array = [-1, -2, -3, -4, -5]
    expected_output = [-5, -4, -3, -2, -1]
  

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("insertion_sort")

    assert output_array == expected_output

def test_merge_sort_sorted_array():
    """
    Test that merge sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("merge_sort")

    assert output_array == expected_output

def test_merge_sort_unsorted_array():
    """
    Test that merge sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("merge_sort")

    assert output_array == expected_output

def test_merge_sort_empty_array():
    """
    Test that merge sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("merge_sort")

    assert output_array == expected_output

def test_merge_sort_single_element_array():
    """
    Test that merge sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("merge_sort")

    assert output_array == expected_output

def test_merge_sort_duplicate_element_array():
    """
    Test that merge sort correctly sorts an array with duplicate elements.
    """
    input_array = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("merge_sort")

    assert output_array == expected_output

def test_merge_sort_negative_element_array():
    """
    Test that merge sort correctly sorts an array with negative elements.
    """
    input_array = [-1, -2, -3, -4, -5]
    expected_output = [-5, -4, -3, -2, -1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("merge_sort")

    assert output_array == expected_output

def test_quick_sort_sorted_array():
    """
    Test that quick sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("quick_sort")

    assert output_array == expected_output

def test_quick_sort_unsorted_array():
    """
    Test that quick sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("quick_sort")

    assert output_array == expected_output

def test_quick_sort_empty_array():
    """
    Test that quick sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("quick_sort")

    assert output_array == expected_output

def test_quick_sort_single_element_array():
    """
    Test that quick sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("quick_sort")

    assert output_array == expected_output
    
def test_quick_sort_duplicate_element_array():
    """
    Test that quick sort correctly sorts an array with duplicate elements.
    """
    input_array = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("quick_sort")

    assert output_array == expected_output

def test_quick_sort_negative_element_array():
    """
    Test that quick sort correctly sorts an array with negative elements.
    """
    input_array = [-1, -2, -3, -4, -5]
    expected_output = [-5, -4, -3, -2, -1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("quick_sort")

    assert output_array == expected_output
    
def test_heap_sort_sorted_array():
    """
    Test that heap sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("heap_sort")

    assert output_array == expected_output

def test_heap_sort_unsorted_array():
    """
    Test that heap sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("heap_sort")

    assert output_array == expected_output

def test_heap_sort_empty_array():
    """
    Test that heap sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("heap_sort")

    assert output_array == expected_output

def test_heap_sort_single_element_array():
    """
    Test that heap sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("heap_sort")

    assert output_array == expected_output

def test_heap_sort_duplicate_element_array():
    """
    Test that heap sort correctly sorts an array with duplicate elements.
    """
    input_array = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("heap_sort")

    assert output_array == expected_output

def test_heap_sort_negative_element_array():
    """
    Test that heap sort correctly sorts an array with negative elements.
    """
    input_array = [-1, -2, -3, -4, -5]
    expected_output = [-5, -4, -3, -2, -1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("heap_sort")

    assert output_array == expected_output

def test_radix_sort_sorted_array():
    """
    Test that radix sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("radix_sort")

    assert output_array == expected_output

def test_radix_sort_unsorted_array():
    """
    Test that radix sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("radix_sort")

    assert output_array == expected_output

# def test_radix_sort_empty_array():
#     """
#     Test that radix sort correctly sorts an empty array.
#     """
#     input_array = []
#     expected_output = []

#     sorter = Sorters( input_array)
#     output_array, output_steps,_ = sorter.start_sorting("radix_sort")

#     assert output_array == expected_output

def test_radix_sort_single_element_array():
    """
    Test that radix sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("radix_sort")

    assert output_array == expected_output
    
# def test_radix_sort_duplicate_element_array():
#     """
#     Test that radix sort correctly sorts an array with duplicate elements.
#     """
#     input_array = [1, 1, 1, 1, 1]
#     expected_output = [1, 1, 1, 1, 1]

#     sorter = Sorters( input_array)
#     output_array, output_steps,_ = sorter.start_sorting("radix_sort")

#     assert output_array == expected_output

# def test_radix_sort_negative_element_array():
#     """
#     Test that radix sort correctly sorts an array with negative elements.
#     """
#     input_array = [-1, -2, -3, -4, -5]
#     expected_output = [-5, -4, -3, -2, -1]

#     sorter = Sorters( input_array)
#     output_array, output_steps,_ = sorter.start_sorting("radix_sort")

#     assert output_array == expected_output

# def test_counting_sort_sorted_array():
#     """
#     Test that counting sort correctly sorts a sorted array.
#     """
#     input_array = [1, 2, 3, 4, 5]
#     expected_output = [1, 2, 3, 4, 5]

#     sorter = Sorters( input_array)
#     output_array, output_steps,_ = sorter.start_sorting("counting_sort")

#     assert output_array == expected_output

def test_counting_sort_unsorted_array():
    """
    Test that counting sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("counting_sort")

    assert output_array == expected_output

# def test_counting_sort_empty_array():
#     """
#     Test that counting sort correctly sorts an empty array.
#     """
#     input_array = []
#     expected_output = []

#     sorter = Sorters( input_array)
#     output_array, output_steps,_ = sorter.start_sorting("counting_sort")

#     assert output_array == expected_output

def test_counting_sort_single_element_array():
    """
    Test that counting sort correctly sorts an array with a single element.
    """
    input_array = [1]
    expected_output = [1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("counting_sort")

    assert output_array == expected_output

def test_counting_sort_duplicate_element_array():
    """
    Test that counting sort correctly sorts an array with duplicate elements.
    """
    input_array = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("counting_sort")

    assert output_array == expected_output

# def test_counting_sort_negative_element_array():
#     """
#     Test that counting sort correctly sorts an array with negative elements.
#     """
#     input_array = [-1, -2, -3, -4, -5]
#     expected_output = [-5, -4, -3, -2, -1]

#     sorter = Sorters( input_array)
#     output_array, output_steps,_ = sorter.start_sorting("counting_sort")

#     assert output_array == expected_output
