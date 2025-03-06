import random
import time
import matplotlib.pyplot as plt
import sorting  # ต้องแน่ใจว่า sorting.py มีฟังก์ชันที่ต้องการ

def compare_sort():
    # ทดสอบกับขนาดข้อมูลต่างๆ
    sizes = [1000,5000, 10000, 20000, 40000,100000]
    selection_times = []
    shell_times = []
    quick_times = []

    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-99999
        data = [random.randint(0, 99999) for _ in range(size)]
        
        # วัดเวลา Selection Sort
        start_time = time.time()
        sorttype.selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Shell Sort
        start_time = time.time()
        sorttype.shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        sorttype.quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.plot(sizes, shell_times, marker='^', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='o', label='Quick Sort')
    plt.title('Performance comparison of sorting (Data 0-999). Created By [Wipatsasicha Bumpenboon]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_Comparison.png')
    plt.show()

# เปรียบเทียบประสิทธิภาพ
sorttype = sorting

compare_sort()
