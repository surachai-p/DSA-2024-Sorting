import random
import time
import matplotlib.pyplot as plt
import sorting  # Import the sorting functions from sorting.py


def compare_selection_shell_quick_sort():
    """Compares the performance of Selection Sort, Shell Sort, and Quick Sort."""

    sizes = [100, 500, 1000, 5000, 10000, 20000, 30000]  # Larger sizes for better comparison
    selection_times = []
    shell_times = []
    quick_times = []

    for size in sizes:
           # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-999
        data = [random.randint(0, 99999) for _ in range(size)]

        # --- Selection Sort ---
        start_time = time.time()
        sorting.selection_sort(data.copy())  # Use data.copy() to avoid modifying the original
        selection_times.append((time.time() - start_time) * 1000)

        # --- Shell Sort ---
        start_time = time.time()
        sorting.shell_sort(data.copy())  # Use data.copy()
        shell_times.append((time.time() - start_time) * 1000)

        # --- Quick Sort ---
        start_time = time.time()
        sorting.quick_sort(data.copy())  # Use data.copy()
        quick_times.append((time.time() - start_time) * 1000)
        
        print(f"ขนาดข้อมูล {size}:")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.plot(sizes, shell_times, marker='o', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='d', label='Quick Sort')
    plt.title('Performance Comparison: Selection Sort vs. Shell Sort vs. Quick Sort (Data 0-999). Created By [Thanakrit Pimarun]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Selection-Shell-Quick-performance.png')  # Save the graph
    plt.show()


# Run the comparison
compare_selection_shell_quick_sort()
