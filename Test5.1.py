import random
import time

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

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ทดสอบกับข้อมูลขนาดใหญ่
size = 10000  # ขนาดชุดข้อมูล
test_data = [random.randint(1, 10000) for _ in range(size)]

# ทดสอบเวลา Shell Sort
shell_sort_data = test_data.copy()
start_time = time.time()
shell_sort(shell_sort_data)
shell_sort_time = (time.time() - start_time) * 1000  # มิลลิวินาที

# ทดสอบเวลา Insertion Sort
insertion_sort_data = test_data.copy()
start_time = time.time()
insertion_sort(insertion_sort_data)
insertion_sort_time = (time.time() - start_time) * 1000  # มิลลิวินาที

# แสดงผลลัพธ์
print(f"เวลา Shell Sort: {shell_sort_time:.6f} มิลลิวินาที")
print(f"เวลา Insertion Sort: {insertion_sort_time:.6f} มิลลิวินาที")
