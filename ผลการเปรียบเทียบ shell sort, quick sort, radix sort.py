import random
import time
import matplotlib.pyplot as plt
import sorting  # ต้องแน่ใจว่า sorting.py มีฟังก์ชัน shell_sort, quick_sort, radix_sort

def compare_sort():
    # ทดสอบกับขนาดข้อมูลต่างๆ
    sizes = [1000,5000, 10000, 20000, 40000,100000]
    shell_times = []
    quick_times = []
    radix_times = []
    
    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-99999
        data = [random.randint(0, 99999) for _ in range(size)]
        
        # วัดเวลา Shell Sort
        start_time = time.time()
        sorting.shell_sort(data.copy())  # ใช้ฟังก์ชัน shell_sort จาก sorting
        shell_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Quick Sort
        start_time = time.time()
        sorting.quick_sort(data.copy())  # ใช้ฟังก์ชัน quick_sort จาก sorting
        quick_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Radix Sort
        start_time = time.time()
        sorting.radix_sort(data.copy())  # ใช้ฟังก์ชัน radix_sort จาก sorting
        radix_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, shell_times, marker='o', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='d', label='Quick Sort')
    plt.plot(sizes, radix_times, marker='s', label='Radix Sort')
    plt.title('Performance comparison of sorting (Data 0-999). Created By [Wipatsasicha Bumpenboon]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_comparison.png')
    plt.show()

# เปรียบเทียบประสิทธิภาพ
sorttype = sorting

compare_sort()
