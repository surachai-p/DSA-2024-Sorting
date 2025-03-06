import random
import time
import matplotlib.pyplot as plt

# Shell Sort
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

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Radix Sort
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_radix(arr, exp)
        exp *= 10
    return arr

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
    return arr

def compare_sort():
    sizes = [100, 500, 1000, 5000]  # ลดขนาดข้อมูลเพื่อให้รันเร็วขึ้น
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

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")

    # วาดกราฟเปรียบเทียบ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, shell_times, marker='o', label='Shell Sort', linestyle='--')
    plt.plot(sizes, quick_times, marker='d', label='Quick Sort', linestyle='-.')
    plt.plot(sizes, radix_times, marker='s', label='Radix Sort', linestyle='-')
    plt.title('Comparison of Sorting Algorithms (Random Data 0-999). Created By [Suphawadee]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance_comparison.png')  # บันทึกเป็นรูปภาพ
    plt.show()

# เปรียบเทียบประสิทธิภาพ
compare_sort()
