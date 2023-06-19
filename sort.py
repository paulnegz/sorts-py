from math import ceil
from functools import reduce
from heapq import heapify, heappop
from util import timeit, merge


RUN_SIZE = 64

@timeit
def quick_sort(unordered_list :list)->list:
    def _quick_sort(unordered_list :list)->list:
        if len(unordered_list)<=1: return unordered_list
        
        pivot = unordered_list.pop()
        is_bigger = lambda x: x>pivot
        left_list = [x for x in unordered_list if not is_bigger(x)]
        right_list = [x for x in unordered_list if is_bigger(x)]
        left, right = _quick_sort(left_list), _quick_sort(right_list)
        return [*left, pivot, *right]
    return _quick_sort(unordered_list)


@timeit
def merge_sort(unordered_list :list)->list:
    def _merge_sort(unordered_list :list)->list:
        length = len(unordered_list)
        if length <= 1: return unordered_list
        
        mid = length//2
        left = _merge_sort(unordered_list[:mid])
        right = _merge_sort(unordered_list[mid:])
        return merge(left,right)
    return _merge_sort(unordered_list)


@timeit
def tim_sort(unordered_list :list)->list:
    run_num = ceil(len(unordered_list)/RUN_SIZE)
    buckets = [[] for _ in range(run_num)]
    for index in range(run_num):
        start, stop = RUN_SIZE*index, RUN_SIZE*(index+1) 
        buckets[index] = unordered_list[start:stop]
    bucket = (_insertion_sort(inner) for inner in buckets)
    return merge(*bucket) 


@timeit
def tim_sort_recursive(unordered_list :list)->list:
    return _tim_sort_recursive(unordered_list)

def _tim_sort_recursive(unordered_list :list)->list:
    left = _insertion_sort(unordered_list[:RUN_SIZE]) 
    if len(unordered_list)<RUN_SIZE: return left

    right = _tim_sort_recursive(unordered_list[RUN_SIZE:])
    return merge(left, right)


@timeit
def heap_sort(random_list: list)->list:
    heapify(random_list)
    result = []
    while random_list:
        result.append(heappop(random_list))
    return result


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
def insertion_sort(unordered_list :list)->list:
    return _insertion_sort(unordered_list)

def _insertion_sort(unordered_list :list)->list:
    for index in range(1,len(unordered_list)):
        behind=index-1
        while behind>=0 and unordered_list[behind] > unordered_list[behind+1]:
            unordered_list[behind], unordered_list[behind+1] = unordered_list[behind+1], unordered_list[behind]
            behind-=1
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
def radix_sort(unordered_list :list)->list:
    base, max_length = 10, len(str(max(unordered_list)))
    for n in range(max_length+1):
        bucket=[[] for _ in range(base)]
        for item in unordered_list:
            bucket[item//base**n %base].append(item)
        unordered_list = reduce(lambda acc, current: [*acc,*current], bucket)
    return unordered_list


@timeit
def python_sort(random_list: list)->list:
    return sorted(random_list)