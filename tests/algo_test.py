from algorithms.sorters import Sorters


def test_bubble_sort_sorted_array():
    """
    Test that bubble sort correctly sorts a sorted array.
    """
    input_array = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    expected_steps = []

    sorter = Sorters("bubble_sort" , input_array)
    output_array, output_steps,_ = sorter.start_sorting()

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

    sorter = Sorters("bubble_sort" , input_array)
    output_array, output_steps,_ = sorter.start_sorting()

    assert output_array == expected_output
    assert output_steps == expected_steps

def test_bubble_sort_empty_array():
    """
    Test that bubble sort correctly sorts an empty array.
    """
    input_array = []
    expected_output = []
    expected_steps = []

    sorter = Sorters("bubble_sort" , input_array)
    output_array, output_steps,_ = sorter.start_sorting()

    assert output_array == expected_output
    assert output_steps == expected_steps
    