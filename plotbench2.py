import matplotlib.pyplot as plt

# Time taken for matrix multiplication in seconds (replace with your actual timings)
cp_time = 1.29  # Example CPython time for matrix multiplication
pypy_time = 0.060 # Example PyPy time for matrix multiplication

# Bar chart comparing CPython and PyPy
implementations = ['CPython', 'PyPy']
times = [cp_time, pypy_time]

plt.figure(figsize=(8, 6))
plt.bar(implementations, times, color=['blue', 'green'])

# Adding title and labels
plt.title('Matrix Multiplication Benchmark: CPython vs PyPy', fontsize=14)
plt.ylabel('Time (seconds)', fontsize=12)
plt.xlabel('Python Implementations', fontsize=12)

# Display the value of time on top of the bars
for i, v in enumerate(times):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', va='bottom', fontsize=12)

# Display the chart
plt.tight_layout()
plt.show()
