import timeit
import random
import numpy as np
import functools

# Function to test sorting
def test_sorting():
    random_list = random.sample(range(1, 1000000), 10000)  # Random list of 10,000 elements
    random_list.sort()

# Function to test searching (binary search)
def test_searching():
    sorted_list = sorted(random.sample(range(1, 1000000), 10000))  # Sorted list of 10,000 elements
    random_value = random.choice(sorted_list)
    return binary_search(sorted_list, random_value)

# Binary search implementation
def binary_search(sorted_list, value):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == value:
            return True
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Function to test matrix multiplication
def test_matrix_multiplication():
    matrix_a = np.random.rand(500, 500)  # 500x500 random matrix
    matrix_b = np.random.rand(500, 500)  # 500x500 random matrix
    result = np.dot(matrix_a, matrix_b)

# Wrapper to run and time functions
def run_benchmark(func, number=10):
    return timeit.timeit(func, number=number)

# Function to run all benchmarks and return a summary
def run_all_benchmarks():
    print("Running Sorting Benchmark...")
    sort_time = run_benchmark(test_sorting)
    print(f"Sorting Time: {sort_time:.6f} seconds")

    print("Running Searching Benchmark...")
    search_time = run_benchmark(test_searching)
    print(f"Searching Time: {search_time:.6f} seconds")

    print("Running Matrix Multiplication Benchmark...")
    matrix_time = run_benchmark(test_matrix_multiplication)
    print(f"Matrix Multiplication Time: {matrix_time:.6f} seconds")

# Main function to execute benchmarks
if __name__ == "__main__":
    run_all_benchmarks()
