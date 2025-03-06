import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# ชุดข้อมูลที่เกือบเรียงลำดับแล้ว (Nearly Sorted Data)
nearly_sorted_data = [90, 80, 70, 60, 50, 40, 35, 20, 10, 5]

print("ข้อมูลก่อนเรียง:", nearly_sorted_data)

start_time = time.time()
sorted_data = selection_sort(nearly_sorted_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง (จากมากไปน้อย):", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
