from functools import wraps
import time
from random import randint


get_ordered_list = lambda WIDTH: [x for x in range(WIDTH)]
get_random_list = lambda WIDTH: [randint(0,WIDTH) for _ in range(WIDTH)]

def get_repeated_list(WIDTH: int)->list:
    repeated_value = randint(0,WIDTH)
    return [repeated_value for _ in range(WIDTH)]


def merge(left :list, *args)->list:
    if len(args) < 1:  return left

    merged, right = [], args[0]
    if len(args) > 1: return merge(merge(left, right), *args[1:])
    
    while left and right:
        merged.append(left.pop(0)) if left[0] < right[0] else merged.append(right.pop(0))
    return [*merged, *right, *left]


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
