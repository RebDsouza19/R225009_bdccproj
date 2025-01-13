import random
import time
import cProfile
from multiprocessing import Pool

# Merge Sort (Non-parallelized)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    sorted_arr.extend(left or right)
    return sorted_arr

# Parallelized Merge Sort (Using multiprocessing)
def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    with Pool(2) as pool:
        left, right = pool.map(merge_sort, [arr[:mid], arr[mid:]])
    return merge(left, right)

# Test function to generate random data
def generate_data(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Profiling function
def profile_sorting(sort_function, data, filename):
    profiler = cProfile.Profile()
    profiler.enable()
    sort_function(data)
    profiler.disable()
    profiler.dump_stats(filename)

# Timing function
def time_sorting(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

# Main execution
if __name__ == "__main__":
    # Random data
    data_size = 100000
    data = generate_data(data_size)

    # Profile the non-parallelized merge sort
    print("Profiling Non-Parallel Merge Sort")
    profile_sorting(merge_sort, data, "non_parallel_merge_sort.prof")

    # Measure the time for non-parallel merge sort
    print(f"Time for Non-Parallel Merge Sort: {time_sorting(merge_sort, data)} seconds")

    # Profile the parallelized merge sort
    print("Profiling Parallel Merge Sort")
    profile_sorting(parallel_merge_sort, data, "parallel_merge_sort.prof")

    # Measure the time for parallel merge sort
    print(f"Time for Parallel Merge Sort: {time_sorting(parallel_merge_sort, data)} seconds")
