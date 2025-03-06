import random
import time
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
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

def compare_sort():
    sizes = [100, 500, 1000, 5000]  # ลดขนาดข้อมูลเพื่อให้รันเร็วขึ้น
    bubble_times = []
    insertion_times = []
    selection_times = []
    
    for size in sizes:
        data = [random.randint(0, 999) for _ in range(size)]
        
        # วัดเวลา Bubble Sort
        start_time = time.time()
        bubble_sort(data.copy())
        bubble_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา Insertion Sort
        start_time = time.time()
        insertion_sort(data.copy())
        insertion_times.append((time.time() - start_time) * 1000)

        # วัดเวลา Selection Sort
        start_time = time.time()
        selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Bubble Sort: {bubble_times[-1]:.2f} มิลลิวินาที")
        print(f"  Insertion Sort: {insertion_times[-1]:.2f} มิลลิวินาที")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")

    # วาดกราฟเปรียบเทียบ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort', linestyle='--')
    plt.plot(sizes, insertion_times, marker='d', label='Insertion Sort', linestyle='-.')
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort', linestyle='-')
    plt.title('Comparison of Sorting Algorithms (Random Data 0-999). Created By [Suphawadee] ')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance.png')  # บันทึกเป็นรูปภาพ
    plt.show()

# เปรียบเทียบประสิทธิภาพ
compare_sort()

