import timeit

def sample_algorithm():
    return sum(range(100000))

# Measure execution time
execution_time = timeit.timeit(sample_algorithm, number=1000)
#print(f"Execution Time: {execution_time} seconds")

# Updated for Jython
print("Execution Time: {} seconds".format(execution_time))