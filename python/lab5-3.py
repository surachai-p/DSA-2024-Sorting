import random
import time

# ฟังก์ชัน Shell Sort
def shell_sort_with_steps(arr):
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

# ฟังก์ชัน Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# สร้างชุดข้อมูลเกือบเรียงลำดับแล้ว
test_data_size = 10000
sorted_data = list(range(1, test_data_size + 1))
# สับเปลี่ยนค่าเล็กน้อยเพื่อให้เกือบเรียงลำดับ
for _ in range(test_data_size // 10):
    i, j = random.sample(range(test_data_size), 2)
    sorted_data[i], sorted_data[j] = sorted_data[j], sorted_data[i]

# ทดสอบ Shell Sort กับชุดข้อมูลเกือบเรียงลำดับแล้ว
start_time = time.time()
shell_sorted_data = shell_sort_with_steps(sorted_data.copy())
shell_sort_time = time.time() - start_time

# ทดสอบ Insertion Sort กับชุดข้อมูลเกือบเรียงลำดับแล้ว
start_time = time.time()
insertion_sorted_data = insertion_sort(sorted_data.copy())
insertion_sort_time = time.time() - start_time

# แสดงผลการทดสอบเวลา
print(f"Shell Sort ใช้เวลา: {shell_sort_time:.5f} วินาที")
print(f"Insertion Sort ใช้เวลา: {insertion_sort_time:.5f} วินาที")
