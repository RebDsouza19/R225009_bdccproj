import time

# Function to calculate sum of squares
def sum_of_squares(n):
    return sum(i ** 2 for i in range(n))

# Set the size of the problem
size = 1000000  # Adjust the size for performance testing

# List to store execution times
execution_times = []

# Number of operations to repeat the task
num_operations = 5

# Perform benchmarking by repeating the operation
for i in range(1, num_operations + 1):
    start_time = time.time()  # Use time.time() for Jython compatibility
    result = sum_of_squares(size)  # Call the function to compute sum of squares
    end_time = time.time()  # End the timer using time.time()

    # Calculate and store execution time
    execution_time = end_time - start_time
    execution_times.append(execution_time)

    # Print the time taken for this operation using format()
    print("Operation {}: {:.6f} seconds".format(i, execution_time))

# Output the average execution time using format()
average_time = sum(execution_times) / num_operations
print("\nAverage Execution Time: {:.6f} seconds".format(average_time))
