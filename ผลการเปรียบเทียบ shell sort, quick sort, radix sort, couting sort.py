import random
import time
import matplotlib.pyplot as plt
import sorting  # ต้องแน่ใจว่า sorting.py มีฟังก์ชันที่ต้องการทั้งหมด

def compare_sort():
    # ทดสอบกับขนาดข้อมูลต่างๆ
    sizes = [1000,5000, 10000, 20000, 40000,100000]
    bubble_times = []
    insertion_times = []
    selection_times = []
    shell_times = []
    quick_times = []
    radix_times = []
    counting_times = []

    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-99999
        data = [random.randint(0, 99999) for _ in range(size)]
        
        # วัดเวลา Bubble Sort
        start_time = time.time()
        sorting.bubble_sort(data.copy())
        bubble_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Insertion Sort
        start_time = time.time()
        sorting.insertion_sort(data.copy())
        insertion_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Selection Sort
        start_time = time.time()
        sorting.selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Shell Sort
        start_time = time.time()
        sorting.shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        sorting.quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Radix Sort
        start_time = time.time()
        sorting.radix_sort(data.copy())
        radix_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Counting Sort
        start_time = time.time()
        sorting.counting_sort(data.copy())
        counting_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Bubble Sort: {bubble_times[-1]:.2f} มิลลิวินาที")
        print(f"  Insertion Sort: {insertion_times[-1]:.2f} มิลลิวินาที")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")
        print(f"  Counting Sort: {counting_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
    plt.plot(sizes, insertion_times, marker='d', label='Insertion Sort')
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.plot(sizes, shell_times, marker='^', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='p', label='Quick Sort')
    plt.plot(sizes, radix_times, marker='h', label='Radix Sort')
    plt.plot(sizes, counting_times, marker='x', label='Counting Sort')
    plt.title('Performance Comparison of Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_comparison.png')
    plt.show()

# เปรียบเทียบประสิทธิภาพ
sorttype = sorting
compare_sort()
