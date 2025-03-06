import random
import time

# ฟังก์ชัน Insertion Sort (จากที่ส่งไป)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ฟังก์ชัน Shell Sort (จากที่ส่งไป)
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# สร้างชุดข้อมูลเกือบเรียงลำดับแล้ว
def generate_nearly_sorted_data(size, swaps=10):
    data = list(range(1, size + 1))  # สร้างชุดข้อมูลที่เรียงลำดับแล้ว
    for _ in range(swaps):
        # สลับค่าระหว่างตำแหน่ง 2 ตำแหน่ง
        i, j = random.sample(range(size), 2)
        data[i], data[j] = data[j], data[i]
    return data

# ทดสอบเวลาในการทำงานของ Insertion Sort
def test_insertion_sort(size, swaps):
    data = generate_nearly_sorted_data(size, swaps)
    start_time = time.time()
    insertion_sort(data)
    end_time = time.time()
    return end_time - start_time

# ทดสอบเวลาในการทำงานของ Shell Sort
def test_shell_sort(size, swaps):
    data = generate_nearly_sorted_data(size, swaps)
    start_time = time.time()
    shell_sort(data)
    end_time = time.time()
    return end_time - start_time

# ทดสอบทั้งสองอัลกอริธึมกับชุดข้อมูลขนาดใหญ่
sizes = [1000, 5000, 10000]  # ขนาดชุดข้อมูลที่ต้องการทดสอบ
swaps = 20  # จำนวนการสลับข้อมูลในชุดข้อมูลที่เกือบเรียงลำดับแล้ว

for size in sizes:
    print(f"ทดสอบกับชุดข้อมูลขนาด {size} (เกือบเรียงลำดับแล้ว):")
    
    # ทดสอบ Insertion Sort
    insertion_time = test_insertion_sort(size, swaps)
    print(f"  Insertion Sort ใช้เวลา: {insertion_time * 1000:.6f} มิลลิวินาที")
    
    # ทดสอบ Shell Sort
    shell_time = test_shell_sort(size, swaps)
    print(f"  Shell Sort ใช้เวลา: {shell_time * 1000:.6f} มิลลิวินาที")
    
    print("-" * 50)
