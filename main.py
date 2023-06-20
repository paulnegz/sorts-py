from util import get_random_list
from rank import rank_sort
from copy import deepcopy
from sort import *


if __name__ == "__main__":
    WIDTH = 4000
    random_list = get_random_list(WIDTH)
    print(f"Sorting list/array with {WIDTH} elements...")
    quick_result = quick_sort(deepcopy(random_list))
    merge_result = merge_sort(deepcopy(random_list))
    tim_result = tim_sort(deepcopy(random_list))
    heap_result = heap_sort(deepcopy(random_list))
    bubble_result = bubble_sort(deepcopy(random_list))
    insertion_result = insertion_sort(deepcopy(random_list))
    selection_result = selection_sort(deepcopy(random_list))
    radix_result = radix_sort(deepcopy(random_list))
    python_result = python_sort(deepcopy(random_list))
    print("========="*10)
    print(f"Result after sorting list/array with {WIDTH} elements...")
    rank_sort.end_ranking()

    assert bubble_result == selection_result == insertion_result
    assert insertion_result == merge_result == quick_result
    assert quick_result == radix_result == tim_result
    assert tim_result == heap_result == python_result