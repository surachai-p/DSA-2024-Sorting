import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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

# กำหนดชุดข้อมูลทดสอบขนาดใหญ่
import random
random.seed(42)
large_test_data = [random.randint(1, 10000) for _ in range(10000)]

# ทดสอบ Insertion Sort
insertion_data = large_test_data.copy()
start_time = time.time()
insertion_sort(insertion_data)
insertion_time = time.time() - start_time

# ทดสอบ Shell Sort
shell_data = large_test_data.copy()
start_time = time.time()
shell_sort(shell_data)
shell_time = time.time() - start_time

# แสดงผลลัพธ์
print(f"Insertion Sort ใช้เวลา: {insertion_time:.6f} วินาที")
print(f"Shell Sort ใช้เวลา: {shell_time:.6f} วินาที")
