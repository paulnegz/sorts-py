from copy import deepcopy
from functools import reduce
from util import timeit, get_random_list, merge


@timeit
def bubble_sort(unordered_list :list)->list:
    for y in range(1, len(unordered_list)):
        swapped: bool = False
        for x in range(1,len(unordered_list)-(y-1)):
            if unordered_list[x]<unordered_list[x-1]:
                unordered_list[x], unordered_list[x-1], swapped = unordered_list[x-1], unordered_list[x], True
        if not swapped: break
    return unordered_list


@timeit
def selection_sort(unordered_list :list)->list:
    for index_y, _ in enumerate(unordered_list):
        min_index = index_y
        for index in range(index_y,len(unordered_list)):
            if unordered_list[index] < unordered_list[min_index]: min_index = index
        unordered_list[min_index], unordered_list[index_y] = unordered_list[index_y], unordered_list[min_index]
    return unordered_list


@timeit
def insertion_sort(unordered_list :list)->list:
    return insertion_sort_rec(unordered_list)

def insertion_sort_rec(unordered_list :list)->list:
    for index in range(1,len(unordered_list)):
        behind=index-1
        while behind>=0 and unordered_list[behind] > unordered_list[behind+1]:
            unordered_list[behind], unordered_list[behind+1] = unordered_list[behind+1], unordered_list[behind]
            behind-=1
    return unordered_list


@timeit
def merge_sort(unordered_list :list)->list:
    def merge_sort_rec(unordered_list :list)->list:
        length = len(unordered_list)
        if length <= 1: return unordered_list
        
        mid = length//2
        left = merge_sort_rec(unordered_list[:mid])
        right = merge_sort_rec(unordered_list[mid:])
        return merge(left,right)
    return merge_sort_rec(unordered_list)


@timeit
def quick_sort(unordered_list :list)->list:
    def quick_sort_rec(unordered_list :list)->list:
        if len(unordered_list)<=1: return unordered_list
        
        pivot = unordered_list.pop()
        is_bigger = lambda x: x>pivot
        left_list = [x for x in unordered_list if not is_bigger(x)]
        right_list = [x for x in unordered_list if is_bigger(x)]
        left, right = quick_sort_rec(left_list), quick_sort_rec(right_list)
        return [*left, pivot, *right]
    return quick_sort_rec(unordered_list)


@timeit
def radix_sort(unordered_list :list)->list:
    base, max_length = 10, len(str(max(unordered_list)))
    for n in range(max_length+1):
        bucket=[[] for _ in range(base)]
        for item in unordered_list:
            bucket[item//base**n %base].append(item)
        unordered_list = reduce(lambda acc, current: [*acc,*current], bucket)
    return unordered_list


@timeit
def tim_sort(unordered_list :list)->list:
    run_size = 64
    if len(unordered_list)<run_size:
        run_size=len(unordered_list)
    run_index = len(unordered_list) // run_size
    bucket_outter=[[] for _ in range(run_index+1)]
    for index, item in enumerate(unordered_list):
        bucket_outter[index//run_size].append(item)
    bucket = list(map(lambda inner_bucket: insertion_sort_rec(inner_bucket), bucket_outter))
    return merge(*bucket) 


@timeit
def python_sort(random_list: list)->list:
    return sorted(random_list)


if __name__ == "__main__":
    WIDTH = 4000
    random_list = get_random_list(WIDTH)
    print(f"Sorting list with {WIDTH} elements...")
    bubble_result = bubble_sort(deepcopy(random_list))
    selection_result = selection_sort(deepcopy(random_list))
    insertion_result = insertion_sort(deepcopy(random_list))
    merge_result = merge_sort(deepcopy(random_list))
    quick_result = quick_sort(deepcopy(random_list))
    radix_result = radix_sort(deepcopy(random_list))
    tim_result = tim_sort(deepcopy(random_list))
    python_result = python_sort(deepcopy(random_list))

    assert bubble_result == selection_result == insertion_result
    assert insertion_result == merge_result == quick_result
    assert quick_result == radix_result == tim_result