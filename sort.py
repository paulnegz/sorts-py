from math import ceil
from functools import reduce
from heapq import heapify, heappop
from util import timeit, merge
from ADT import BST


RUN_SIZE = 2**6
BUCKETS = 2**6

@timeit
def quick_sort(array :list)->list:
    def _quick_sort(array :list)->list:
        if len(array)<=1: return array
        
        pivot, is_bigger = array.pop(), lambda x: x>pivot
        left_partition = _quick_sort([x for x in array if not is_bigger(x)])
        right_partition = _quick_sort([x for x in array if is_bigger(x)])
        return [*left_partition, pivot, *right_partition]
    return _quick_sort(array)


@timeit
def merge_sort(array :list)->list:
    def _merge_sort(array :list)->list:
        length, mid = len(array), len(array)//2
        if length <= 1: return array
        
        left_subarray = _merge_sort(array[:mid])
        right_subarray = _merge_sort(array[mid:])
        return merge(left_subarray,right_subarray)
    return _merge_sort(array)


@timeit
def tim_sort(array :list)->list:
    run_num = ceil(len(array)/RUN_SIZE)
    buckets = [[] for _ in range(run_num)]
    for index in range(run_num):
        start, stop = RUN_SIZE*index, RUN_SIZE*(index+1) 
        buckets[index] = array[start:stop]
    bucket = (_insertion_sort(inner) for inner in buckets)
    return merge(*bucket) 


@timeit
def tim_sort_recursive(array :list)->list:
    return _tim_sort_recursive(array)

def _tim_sort_recursive(array :list)->list:
    left = _insertion_sort(array[:RUN_SIZE]) 
    if len(array)<RUN_SIZE: return left

    right = _tim_sort_recursive(array[RUN_SIZE:])
    return merge(left, right)


@timeit
def heap_sort(random_list: list)->list:
    heapify(random_list)
    result = []
    while random_list:
        result.append(heappop(random_list))
    return result


@timeit
def bubble_sort(array :list)->list:
    for y in range(1, len(array)):
        swap: bool = False
        for x in range(1,len(array)-(y-1)):
            if array[x]<array[x-1]:
                array[x],array[x-1], swap = array[x-1],array[x], True
        if not swap: break
    return array 


@timeit
def insertion_sort(array :list)->list:
    return _insertion_sort(array)

def _insertion_sort(array :list)->list:
    for index in range(1,len(array)):
        back=index-1
        while back>=0 and array[back] > array[back+1]:
            array[back], array[back+1] = array[back+1], array[back]
            back-=1
    return array


@timeit
def selection_sort(array :list)->list:
    for idx_y, _ in enumerate(array):
        min_idx = idx_y
        for idx in range(idx_y,len(array)):
            if array[idx] < array[min_idx]: min_idx = idx
        array[min_idx], array[idx_y] = array[idx_y], array[min_idx]
    return array


@timeit
def tree_sort(array: list)->list:
    bst = BST().create_tree(array)
    result = bst.inorder()
    return result
 

@timeit
def radix_sort(array :list)->list:
    base, max_length = 10, len(str(max(array)))
    for n in range(max_length):
        bucket=[[] for _ in range(base)]
        for item in array: bucket[item//base**n%base].append(item)
        array = reduce(lambda acc, current: [*acc,*current], bucket)
    return array


@timeit
def python_sort(random_list: list)->list:
    return sorted(random_list)