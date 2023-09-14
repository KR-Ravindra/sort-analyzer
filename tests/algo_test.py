from algorithms.sorters import Sorters


def test_bubble_sort_sorted_array():
    """
    Test that bubble sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    expected_steps = []

    sorter = Sorters(input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output
    assert output_steps == expected_steps

def test_bubble_sort_unsorted_array():
    """
    Test that bubble sort correctly sorts an unsorted array.
    """
    input_array = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
    expected_steps = [[4, 5, 3, 2, 1],
                    [4, 3, 5, 2, 1],
                    [4, 3, 2, 5, 1],
                    [4, 3, 2, 1, 5],
                    [3, 4, 2, 1, 5],
                    [3, 2, 4, 1, 5],
                    [3, 2, 1, 4, 5],
                    [2, 3, 1, 4, 5],
                    [2, 1, 3, 4, 5],
                    [1, 2, 3, 4, 5]]

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output
    assert output_steps == expected_steps

def test_bubble_sort_empty_array():
    """
    Test that bubble sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []
    expected_steps = []

    sorter = Sorters( input_array)
    output_array, output_steps,_ = sorter.start_sorting("bubble_sort")

    assert output_array == expected_output
    assert output_steps == expected_steps

def test_insertion_sort_empty_array():
    # Test case 1: Sort an empty list
    input_array = []
    sorter = Sorters(input_array)
    sorted_array, steps, execution_time = sorter.start_sorting("insertion_sort")
    assert sorted_array == []
    assert steps == []
    assert execution_time >= 0  # Execution time should be non-negative

def test_insertion_sort_singleElement_array():
    # Test case 2: Sort a single element list
    input_array = [56]
    sorter = Sorters(input_array)
    sorted_array, steps, execution_time = sorter.start_sorting("insertion_sort")
    assert sorted_array == [56]
    assert steps == []
    assert execution_time >= 0  # Execution time should be non-negative

def test_insertion_sort_unsorted_array():
    # Test case 3: Sort unsorted list
    input_array = [8,9,5,10,3,1,2,7,6,4]
    sorter = Sorters(input_array)
    sorted_array, steps, execution_time = sorter.start_sorting("insertion_sort")
    assert sorted_array == [1,2,3,4,5,6,7,8,9,10]
    assert steps != []
    assert execution_time >= 0  # Execution time should be non-negative

def test_insertion_sort_unsorted_desc_array():
    # Test case 4: Sort unsorted list(desc order)
    input_array = [10,9,8,7,6,5,4,3,2,1]
    sorter = Sorters(input_array)
    sorted_array, steps, execution_time = sorter.start_sorting("insertion_sort")
    assert sorted_array == [1,2,3,4,5,6,7,8,9,10]
    assert steps != []
    assert execution_time >= 0  # Execution time should be non-negative
def test_insertion_sort_unsorted_duplicateElements_array():
    # Test case 5: Sort unsorted list(duplicate elements)
    input_array = [10,9,8,8,6,10,4,1,3,2,10]
    sorter = Sorters(input_array)
    sorted_array, steps, execution_time = sorter.start_sorting("insertion_sort")
    assert sorted_array == [1,2,3,4,6,8,8,9,10,10,10]
    assert steps != []
    assert execution_time >= 0  # Execution time should be non-negative

def test_insertion_sort_unsorted_singleElementsRepetition_array():
    # Test case 6: Sort unsorted list(Single duplicate elements)
    input_array = [1,1,1,1,1,1,1,1,1,1]
    sorter = Sorters(input_array)
    sorted_array, steps, execution_time = sorter.start_sorting("insertion_sort")
    assert sorted_array == [1,1,1,1,1,1,1,1,1,1]
    assert steps == []
    assert execution_time >= 0  # Execution time should be non-negative



