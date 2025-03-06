import random
import time
import matplotlib.pyplot as plt
import sorting  # Import the sorting functions from sorting.py


def compare_shell_quick_radix_counting_sort():
    """Compares the performance of Shell Sort, Quick Sort, Radix Sort, and Counting Sort."""

    sizes = [100, 500, 1000, 5000, 10000, 20000, 30000]
    shell_times = []
    quick_times = []
    radix_times = []
    counting_times = []

    for size in sizes:
        # Create a list of random integers (0 to 999)
        data = [random.randint(0, 999) for _ in range(size)]

        # --- Shell Sort ---
        start_time = time.time()
        sorting.shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # --- Quick Sort ---
        start_time = time.time()
        sorting.quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        # --- Radix Sort ---
        start_time = time.time()
        sorting.radix_sort(data.copy())
        radix_times.append((time.time() - start_time) * 1000)

        # --- Counting Sort ---
        start_time = time.time()
        sorting.counting_sort(data.copy())
        counting_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")
        print(f"  Counting Sort: {counting_times[-1]:.2f} มิลลิวินาที")

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, shell_times, marker='o', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='d', label='Quick Sort')
    plt.plot(sizes, radix_times, marker='s', label='Radix Sort')
    plt.plot(sizes, counting_times, marker='v', label='Counting Sort')
    plt.title('Performance Comparison: Shell Sort vs. Quick Sort vs. Radix Sort vs. Counting Sort (Data 0-999). Created By [Thanakrit Pimarun]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Shell-Quick-Radix-Counting-performance.png')
    plt.show()


# Run the comparison
compare_shell_quick_radix_counting_sort()
