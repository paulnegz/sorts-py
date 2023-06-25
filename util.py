from functools import wraps, reduce
from time import perf_counter
from random import randint
from rank import rank_sort

get_ordered_list = lambda WIDTH: [x for x in range(WIDTH)]
get_reversed_list = lambda WIDTH: [(WIDTH-x) for x in range(WIDTH)]
get_random_list = lambda WIDTH: [randint(0,WIDTH) for _ in range(WIDTH)]
flat_map = lambda arr: reduce(lambda acc, curr: [*acc,*curr], arr)

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
        start_time, result = perf_counter(), func(*args, **kwargs)
        end_time = perf_counter()
        total_time = end_time - start_time
        # print(f'Function {func.__name__}\t{result} took {total_time:.4f} seconds')

        rank_sort(func.__name__).report_time(total_time)
        print(f'{func.__name__}\t took {total_time:.4f} seconds')
        return result
    return timeit_wrapper