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

# Profiling and Timing function
def profile_and_time_sorting(sort_function, data):
    profiler = cProfile.Profile()
    profiler.enable()  # Start profiling

    start_time = time.time()  # Start timing
    sort_function(data)  # Call the sorting function
    end_time = time.time()  # End timing
    
    profiler.disable()  # Stop profiling
    
    # Print time taken
    print(f"Time for {sort_function.__name__}: {end_time - start_time} seconds")
    
    # Print profiling stats
    profiler.print_stats()  # Print stats
    
    # Save profiling data for visualization
    profiler.dump_stats(f"{sort_function.__name__}_profiling.prof")

# Main execution
if __name__ == "__main__":
    # Generate random data
    data_size = 100000
    data = generate_data(data_size)

    # Profile and time the non-parallel merge sort
    print("Profiling Non-Parallel Merge Sort:")
    profile_and_time_sorting(merge_sort, data)

    # Profile and time the parallel merge sort
    print("\nProfiling Parallel Merge Sort:")
    profile_and_time_sorting(parallel_merge_sort, data)
