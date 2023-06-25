from util import get_random_list
from rank import rank_sort
from copy import deepcopy
from sort import *


if __name__ == "__main__":
    WIDTH = 4000
    # WIDTH = 20
    random_list = get_random_list(WIDTH)
    print(f"Sorting list/array with {WIDTH} items...")
    quick_result = quick_sort(deepcopy(random_list))
    merge_result = merge_sort(deepcopy(random_list))
    tim_result = tim_sort(deepcopy(random_list))
    heap_result = heap_sort(deepcopy(random_list))
    bubble_result = bubble_sort(deepcopy(random_list))
    insertion_result = insertion_sort(deepcopy(random_list))
    selection_result = selection_sort(deepcopy(random_list))
    tree_result = tree_sort(deepcopy(random_list))
    shell_result = shell_sort(deepcopy(random_list))
    bucket_result = bucket_sort(deepcopy(random_list))
    radix_result = radix_sort(deepcopy(random_list))
    counting_result = counting_sort(deepcopy(random_list))
    # counting_result = counting_sort(deepcopy(random_list))
    python_result = python_sort(deepcopy(random_list))
    print("========="*10)
    print(f"Result after sorting {WIDTH} items...")
    rank_sort.end_ranking()

    assert bubble_result == selection_result == python_result
    assert insertion_result == merge_result == python_result
    assert quick_result == radix_result == python_result
    assert tim_result == heap_result == python_result
    assert tree_result == shell_result == python_result
    # assert counting_result == bucket_result == python_result