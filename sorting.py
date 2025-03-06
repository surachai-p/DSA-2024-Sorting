# ไฟล์หลัก (เช่น sorting.py)
import random
import time
import matplotlib.pyplot as plt
from sorting import selection_sort, shell_sort, quick_sort  # เพิ่มการ import ฟังก์ชัน

def compare_sort():
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    selection_times = []
    shell_times = []
    quick_times = []
    
    for size in sizes:
        data = [random.randint(0, 999) for _ in range(size)]
        
        # วัดเวลา Selection Sort
        start_time = time.time()
        selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Shell Sort
        start_time = time.time()
        shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.plot(sizes, shell_times, marker='x', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='^', label='Quick Sort')
    
    plt.title('Performance comparison of sorting algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_comparison.png')
    plt.show()

# เรียกใช้ฟังก์ชัน compare_sort()
compare_sort()
