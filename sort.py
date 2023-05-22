from random import randint
from copy import deepcopy
from functools import wraps
from math import ceil
import time
from functools import reduce
import logging

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # print(f'Function {func.__name__}\t{result} took {total_time:.4f} seconds')
        print(f'Function {func.__name__}\t took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@timeit
def bubbleSort(unorderedList :list)->list:
    for y in range(1, len(unorderedList)):
        swapped: bool = False
        for x in range(1,len(unorderedList)-(y-1)):
            if unorderedList[x]<unorderedList[x-1]:
                unorderedList[x], unorderedList[x - 1] = unorderedList[x-1], unorderedList[x]
                swapped=True
        if not swapped:
            break
    return unorderedList

@timeit
def selectionSort(unorderedList :list)->list:
    for index_y in range(len(unorderedList)):
        minIndex = index_y
        for index in range(index_y,len(unorderedList)):
            if unorderedList[index] < unorderedList[minIndex]:
                minIndex = index
        unorderedList[minIndex], unorderedList[index_y] = unorderedList[index_y], unorderedList[minIndex]
    return unorderedList

@timeit
def insertionSort(unorderedList :list)->list:
    for index in range(1,len(unorderedList)):
        behind=index-1
        while behind>=0 and unorderedList[behind] > unorderedList[behind+1]:
            unorderedList[behind], unorderedList[behind+1] = unorderedList[behind+1], unorderedList[behind]
            behind-=1
    return unorderedList

@timeit
def mergeSort(unorderedList :list)->list:
    result = mergeSortRec(unorderedList)
    return result

def mergeSortRec(unorderedList :list)->list:
    length = len(unorderedList)
    if length <= 1:
        return unorderedList
    mid = length //2
    left = mergeSortRec(unorderedList[:mid])
    right = mergeSortRec(unorderedList[mid:])
    return merge(left,right)


def merge(left :list, *args)->list:
    if len(args) < 1:  return left

    merged, right = [], args[0]
    if len(args) > 1: return merge(merge(left, right), *args[1:])
    while len(left) and len(right):
        merged.append(left.pop(0)) if left[0] < right[0] else merged.append(right.pop(0))
    return [*merged, *right, *left]


@timeit
def quickSort(unorderedList :list)->list:
    result = quickSortRec(unorderedList)
    return result

def quickSortRec(unorderedList :list)->list:
    if len(unorderedList)<=1:
        return unorderedList
    pivot = unorderedList.pop(0)
    is_positive = lambda x: x>pivot
    leftList = [x for x in unorderedList if not is_positive(x)]
    rightList = [x for x in unorderedList if is_positive(x)]

    left = quickSortRec(leftList)
    right = quickSortRec(rightList)
    return [*left, pivot, *right]


@timeit
def radixSort(unorderedList :list)->list:
    base=10
    max_length=len(str(max(unorderedList)))
    n=0
    while n<=max_length:
        bucket=[[] for _ in range(base)]
        for item in unorderedList:
            bucket[item//base**n %10].append(item)
        n+=1
        unorderedList = reduce(lambda acc, current: acc+current, bucket)
    return unorderedList

@timeit
def timSort(unorderedList :list)->list:
    runSize = 64
    # runSize = 4
    if len(unorderedList)<runSize:
        runSize=len(unorderedList)

    numberOfRun=len(unorderedList) // runSize
    bucket=[[] for _ in range(numberOfRun+1)]
    for index, item in enumerate(unorderedList):
        bucket[index//runSize].append(item)
    bucket = list(map(lambda inner_bucket: insertionTimSort(inner_bucket), bucket))
    return merge(*bucket)


def insertionTimSort(unorderedList :list)->list:
    for cardIndex in range(1,len(unorderedList)):
        behindIndex=cardIndex-1
        while behindIndex>=0 and unorderedList[behindIndex] > unorderedList[behindIndex+1]:
            unorderedList[behindIndex+1], unorderedList[behindIndex] =  unorderedList[behindIndex], unorderedList[behindIndex+1]
            behindIndex-=1
    return unorderedList

@timeit
def pythonSort(randomList: list)->list:
    return sorted(randomList)

if __name__ == "__main__":
    # WIDTH=50
    WIDTH = 9000
    randomList = [randint(0,WIDTH) for _ in range(WIDTH)]
    # randomList = [0 for x in range(WIDTH)]
    logging.info(f"randomList: \t{randomList}")
    logging.info("================================================="*2)
    # bubbleSort(deepcopy(randomList))
    # selectionSort(deepcopy(randomList))
    # insertionSort(deepcopy(randomList))
    # mergeSort(deepcopy(randomList))
    # quickSort(deepcopy(randomList))
    # radixSort(deepcopy(randomList))
    # timSort(deepcopy(randomList))
    # pythonSort(deepcopy(randomList))

    # print(bubbleSort(deepcopy(randomList)))
    # print(selectionSort(deepcopy(randomList)))
    # print(insertionSort(deepcopy(randomList)))
    # print(mergeSort(deepcopy(randomList)))
    # print(quickSort(deepcopy(randomList)))
    # print(radixSort(deepcopy(randomList)))
    # print(timSort(deepcopy(randomList)))
    # print(pythonSort(deepcopy(randomList)))

    assert bubbleSort(deepcopy(randomList)) == selectionSort(deepcopy(randomList))
    assert selectionSort(deepcopy(randomList)) == insertionSort(deepcopy(randomList))
    assert insertionSort(deepcopy(randomList)) == mergeSort(deepcopy(randomList))
    assert mergeSort(deepcopy(randomList)) == quickSort(deepcopy(randomList))
    assert quickSort(deepcopy(randomList)) == radixSort(deepcopy(randomList))
    assert radixSort(deepcopy(randomList)) == timSort(deepcopy(randomList))