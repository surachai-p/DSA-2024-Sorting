import random
import time
import matplotlib.pyplot as plt
import sorting  # โมดูลที่มีฟังก์ชันการเรียงลำดับต่างๆ

def compare_sort():
    # ขนาดข้อมูลที่ทดสอบ
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    selection_times = []
    shell_times = []
    quick_times = []
    
    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-99999
        data = [random.randint(0, 99999) for _ in range(size)]
        
        # วัดเวลา Selection Sort
        start_time = time.time()
        sorting.selection_sort(data.copy())  # เรียกใช้ฟังก์ชัน selection_sort จากโมดูล sorting
        selection_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Shell Sort
        start_time = time.time()
        sorting.shell_sort(data.copy())  # เรียกใช้ฟังก์ชัน shell_sort จากโมดูล sorting
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        sorting.quick_sort(data.copy())  # เรียกใช้ฟังก์ชัน quick_sort จากโมดูล sorting
        quick_times.append((time.time() - start_time) * 1000)

        # แสดงผลระหว่างการทดสอบ
        print(f"ขนาดข้อมูล {size}:")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.plot(sizes, shell_times, marker='d', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='o', label='Quick Sort')
    plt.title('Performance Comparison of Sorting Algorithms (Data 0-99999). Created By Supattra Pankulab')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_Comparison.png')
    plt.show()

# เปรียบเทียบประสิทธิภาพ
sorttype = sorting

compare_sort()

