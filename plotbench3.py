import matplotlib.pyplot as plt

# Replace these with actual recorded times from CPython and PyPy runs
execution_times_cpython = [0.0784, 0.066, 0.055, 0.066, 0.046, 0.045, 0.042, 0.044, 0.043, 0.037]
execution_times_pypy = [0.061, 0.075, 0.055, 0.057, 0.086, 0.046, 0.046, 0.045, 0.037, 0.034]

x = list(range(1, len(execution_times_cpython) + 1))  # x-axis: Operation numbers

plt.figure(figsize=(10, 6))

# Plot execution times for CPython
plt.plot(x, execution_times_cpython, marker='o', color='blue', linestyle='-', label='CPython')

# Plot execution times for PyPy
plt.plot(x, execution_times_pypy, marker='s', color='green', linestyle='--', label='PyPy')

# Add title and labels
plt.title('Matrix Multiplication Execution Times: CPython vs PyPy', fontsize=14)
plt.xlabel('Matrix Multiplication Number', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)

# Annotate each point with its value (optional)
for i, time_value in enumerate(execution_times_cpython):
    plt.text(x[i], time_value + 0.0002, f'{time_value:.4f}', ha='center', va='bottom', fontsize=10, color='blue')

for i, time_value in enumerate(execution_times_pypy):
    plt.text(x[i], time_value - 0.0002, f'{time_value:.4f}', ha='center', va='top', fontsize=10, color='green')

# Show the plot
plt.tight_layout()
plt.show()
