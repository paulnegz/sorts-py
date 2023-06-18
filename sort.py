from copy import deepcopy
from functools import reduce
from util import timeit, get_random_list
import logging


@timeit
def bubble_sort(unordered_list :list)->list:
    for y in range(1, len(unordered_list)):
        swapped: bool = False
        for x in range(1,len(unordered_list)-(y-1)):
            if unordered_list[x]<unordered_list[x-1]:
                unordered_list[x], unordered_list[x - 1] = unordered_list[x-1], unordered_list[x]
                swapped=True
        if not swapped:
            break
    return unordered_list

@timeit
def selection_sort(unordered_list :list)->list:
    for index_y in range(len(unordered_list)):
        min_index = index_y
        for index in range(index_y,len(unordered_list)):
            if unordered_list[index] < unordered_list[min_index]:
                min_index = index
        unordered_list[min_index], unordered_list[index_y] = unordered_list[index_y], unordered_list[min_index]
    return unordered_list

@timeit
def insertion_sort(unordered_list :list)->list:
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
        
        mid = length //2
        left = merge_sort_rec(unordered_list[:mid])
        right = merge_sort_rec(unordered_list[mid:])
        return merge(left,right)
    return merge_sort_rec(unordered_list)


def merge(left :list, *args)->list:
    if len(args) < 1:  return left

    merged, right = [], args[0]
    if len(args) > 1: return merge(merge(left, right), *args[1:])
    
    while len(left) and len(right):
        merged.append(left.pop(0)) if left[0] < right[0] else merged.append(right.pop(0))
    return [*merged, *right, *left]


@timeit
def quick_sort(unordered_list :list)->list:
    def quick_sort_rec(unordered_list :list)->list:
        if len(unordered_list)<=1:
            return unordered_list
        
        pivot = unordered_list.pop(0)
        is_positive = lambda x: x>pivot
        left_list = [x for x in unordered_list if not is_positive(x)]
        right_list = [x for x in unordered_list if is_positive(x)]

        left, right = quick_sort_rec(left_list), quick_sort_rec(right_list)
        return [*left, pivot, *right]
    return quick_sort_rec(unordered_list)


@timeit
def radix_sort(unordered_list :list)->list:
    n, base, max_length = 0, 10, len(str(max(unordered_list)))
    while n<=max_length:
        bucket=[[] for _ in range(base)]
        for item in unordered_list:
            bucket[item//base**n %10].append(item)
        n+=1
        unordered_list = reduce(lambda acc, current: acc+current, bucket)
    return unordered_list

@timeit
def tim_sort(unordered_list :list)->list:
    run_size = 64
    if len(unordered_list)<run_size:
        run_size=len(unordered_list)

    run_index = len(unordered_list) // run_size
    bucket=[[] for _ in range(run_index+1)]
    for index, item in enumerate(unordered_list):
        bucket[index//run_size].append(item)
    bucket = list(map(lambda inner_bucket: insertion_tim_sort(inner_bucket), bucket))
    return merge(*bucket)


def insertion_tim_sort(unordered_list :list)->list:
    for card_index in range(1,len(unordered_list)):
        behind_index=card_index-1
        while behind_index>=0 and unordered_list[behind_index] > unordered_list[behind_index+1]:
            unordered_list[behind_index+1], unordered_list[behind_index] =  unordered_list[behind_index], unordered_list[behind_index+1]
            behind_index-=1
    return unordered_list


@timeit
def python_sort(random_list: list)->list:
    return sorted(random_list)


if __name__ == "__main__":
    WIDTH = 4000
    random_list = get_random_list(WIDTH)
    print(f"Sorting list with {WIDTH} elements...")
    logging.info(f"random_list: \t{random_list}")
    logging.info("========================"*4)
    bubble_sort(deepcopy(random_list))
    selection_sort(deepcopy(random_list))
    insertion_sort(deepcopy(random_list))
    merge_sort(deepcopy(random_list))
    quick_sort(deepcopy(random_list))
    radix_sort(deepcopy(random_list))
    tim_sort(deepcopy(random_list))
    python_sort(deepcopy(random_list))

    #assert bubble_sort(deepcopy(random_list)) == selection_sort(deepcopy(random_list))
    #assert insertion_sort(deepcopy(random_list)) == merge_sort(deepcopy(random_list))
    #assert merge_sort(deepcopy(random_list)) == quick_sort(deepcopy(random_list))
    #assert quick_sort(deepcopy(random_list)) == radix_sort(deepcopy(random_list))
    #assert radix_sort(deepcopy(random_list)) == tim_sort(deepcopy(random_list))
    # print(bubble_sort(deepcopy(random_list)))
    # print(selection_sort(deepcopy(random_list)))
    # print(insertion_sort(deepcopy(random_list)))
    # print(merge_sort(deepcopy(random_list)))
    # print(quick_sort(deepcopy(random_list)))
    # print(radix_sort(deepcopy(random_list)))
    # print(tim_sort(deepcopy(random_list)))
    # print(python_sort(deepcopy(random_list)))