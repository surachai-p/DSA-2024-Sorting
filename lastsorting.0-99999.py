import random
import time
import matplotlib.pyplot as plt

# ฟังก์ชัน Shell Sort
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

# ฟังก์ชัน Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# ฟังก์ชัน Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ฟังก์ชัน Counting Sort
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr

# ฟังก์ชัน Radix Sort
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
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

# ฟังก์ชันเปรียบเทียบประสิทธิภาพ
def compare_sort():
    sizes = [1000, 5000, 10000, 20000, 40000, 100000]  # เปลี่ยนขนาดอินพุต
    shell_times = []
    quick_times = []
    merge_times = []
    radix_times = []
    counting_times = []

    for size in sizes:
        data = [random.randint(0, 99999) for _ in range(size)]  # เปลี่ยนข้อมูลให้อยู่ในช่วง 0-999
        
        # วัดเวลา Shell Sort
        start_time = time.time()
        shell_sort(data.copy())
        shell_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Quick Sort
        start_time = time.time()
        quick_sort(data.copy())
        quick_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Merge Sort
        start_time = time.time()
        merge_sort(data.copy())
        merge_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Radix Sort
        start_time = time.time()
        radix_sort(data.copy())
        radix_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Counting Sort
        start_time = time.time()
        counting_sort(data.copy())
        counting_times.append((time.time() - start_time) * 1000)

        # แสดงผลลัพธ์
        print(f"ขนาดข้อมูล {size}:")
        print(f"  Shell Sort: {shell_times[-1]:.2f} มิลลิวินาที")
        print(f"  Quick Sort: {quick_times[-1]:.2f} มิลลิวินาที")
        print(f"  Merge Sort: {merge_times[-1]:.2f} มิลลิวินาที")
        print(f"  Radix Sort: {radix_times[-1]:.2f} มิลลิวินาที")
        print(f"  Counting Sort: {counting_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, shell_times, marker='x', label='Shell Sort')
    plt.plot(sizes, quick_times, marker='^', label='Quick Sort')
    plt.plot(sizes, merge_times, marker='s', label='Merge Sort')
    plt.plot(sizes, radix_times, marker='*', label='Radix Sort')
    plt.plot(sizes, counting_times, marker='o', label='Counting Sort')

    plt.title('Performance Comparison of Sorting Algorithms (Data 0-99999). Created By [Phum Akrthum]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Sorting_Performance_Comparison_0-999.png')
    plt.show()

# เรียกใช้ฟังก์ชัน
compare_sort()
