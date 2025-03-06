import time

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # ถ้าไม่มีการสลับในรอบนี้ แสดงว่าข้อมูลเรียงลำดับแล้ว
        if not swapped:
            break
    return arr
    

    
# ทดสอบกับชุดข้อมูลที่เรียงลำดับแล้ว
test_data_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_time_sorted = time.time()
sorted_data_sorted = optimized_bubble_sort(test_data_sorted.copy())
end_time_sorted = time.time()
print("Sorted already array:", sorted_data_sorted)
print("Execution time for sorted array:", end_time_sorted - start_time_sorted, "seconds")