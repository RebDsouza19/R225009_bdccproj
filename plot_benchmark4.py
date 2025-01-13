import matplotlib.pyplot as plt

# Sample data: Replace with actual execution times for each Python flavor
operations = [1, 2, 3, 4, 5]  # Example operation numbers
cpython_times = [0.069,0.065, 0.062, 0.063, 0.064]  # Example CPython times
pypy_times = [0.007, 0.004, 0.004, 0.002, 0.003]  # Example PyPy times
jython_times = [0.516, 0.278, 0.218, 0.416, 0.321]  # Example Jython times

# Plot the data
plt.figure(figsize=(10, 6))

# Plot each line for CPython, PyPy, and Jython
plt.plot(operations, cpython_times, marker='o', label='CPython', color='blue')
plt.plot(operations, pypy_times, marker='o', label='PyPy', color='green')
plt.plot(operations, jython_times, marker='o', label='Jython', color='red')

# Add labels and title
plt.title('Benchmark Comparison of Python Flavors', fontsize=14)
plt.xlabel('Operation Number', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.grid(True)

# Add a legend to distinguish the lines
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
