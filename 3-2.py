import random
import time
import matplotlib.pyplot as plt

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Shell Sort
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

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def compare_sort():
    sizes = [100, 500, 1000, 5000, 10000]  # ขยายขนาดข้อมูล
    selection_times = []
    shell_times = []
    quick_times = []
    
    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-99999
        data = [random.randint(0, 99999) for _ in range(size)]
        
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

    # วาดกราฟเปรียบเทียบ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort', linestyle='-')
    plt.plot(sizes, shell_times, marker='d', label='Shell Sort', linestyle='--')
    plt.plot(sizes, quick_times, marker='o', label='Quick Sort', linestyle='-.')
    plt.title('Comparison of Sorting Algorithms (Random Data 0-99999). Created By [Suphawadee]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_Selection_Shell_Quick.png')  # บันทึกเป็นรูปภาพ
    plt.show()

# เปรียบเทียบประสิทธิภาพ
compare_sort()
