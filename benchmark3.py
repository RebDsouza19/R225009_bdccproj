import time
import numpy as np
import matplotlib.pyplot as plt

# Set the dimensions of the matrices
size = 1000  # Increase matrix size to 1000x1000
num_operations = 10  # Number of matrix multiplications

# Create two random matrices
matrix_a = np.random.rand(size, size)
matrix_b = np.random.rand(size, size)

# Initialize a list to store execution times
execution_times = []

# Perform matrix multiplications and record the execution time
for i in range(1, num_operations + 1):
    start_time = time.perf_counter()  # Use higher precision timer
    result = np.dot(matrix_a, matrix_b)  # Matrix multiplication
    end_time = time.perf_counter()
    
    # Calculate time taken for this operation
    execution_time = end_time - start_time
    execution_times.append(execution_time)

    # Print the time for each operation
    print(f"Matrix Multiplication {i}: {execution_time:.6f} seconds")

# Plot the execution times
x = list(range(1, num_operations + 1))  # x-axis: Operation numbers

plt.figure(figsize=(10, 6))
plt.plot(x, execution_times, marker='o', color='blue', linestyle='-', label='Execution Time')

# Add title and labels
plt.title('Matrix Multiplication Execution Times', fontsize=14)
plt.xlabel('Matrix Multiplication Number', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)

# Annotate each point with its value
for i, time_value in enumerate(execution_times):
    plt.text(x[i], time_value + 0.0002, f'{time_value:.4f}', ha='center', va='bottom', fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()
