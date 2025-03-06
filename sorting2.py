import random
import time
import matplotlib.pyplot as plt

# ฟังก์ชันต่างๆ ที่ใช้ในการจัดเรียง
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # กำหนดระยะห่างเริ่มต้น
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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 10 หลัก (0-9)
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# ฟังก์ชันเปรียบเทียบประสิทธิภาพ
def compare_sort():
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    shell_times = []
    quick_times = []
    radix_times = []

    for size in sizes:
        data = [random.randint(0, 999) for _ in range(size)]
        
        # วัดเวลา Shell Sort
        start_time = time.time()
        shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Radix Sort
        start_time = time.time()
        radix_sort(data.copy())
        radix_times.append((time.time() - start_time) * 1000)

        # แสดงผลลัพธ์
        print(f"ขนาดข้อมูล {size}:")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, shell_times, marker='x', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='^', label='Quick Sort')
    plt.plot(sizes, radix_times, marker='*', label='Radix Sort')
    
    plt.title('Performance comparison of sorting (Data 0-999). Created By [Sronsawan]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Sorting_Performance_Comparison.png')
    plt.show()

# เรียกใช้ฟังก์ชัน
compare_sort()
