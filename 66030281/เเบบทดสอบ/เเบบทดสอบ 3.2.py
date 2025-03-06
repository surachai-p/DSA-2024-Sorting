import time

def selection_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:  # ค้นหาค่ามากที่สุด
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]  # สลับค่า
    
    return arr

# สร้างชุดข้อมูลที่เกือบเรียงลำดับแล้ว
nearly_sorted_data = [90, 80, 70, 60, 50, 40, 30, 20, 10, 15]

# วัดเวลาการทำงาน
start_time = time.time()
sorted_data = selection_sort_descending(nearly_sorted_data.copy())
end_time = time.time()

# แสดงผลลัพธ์
print("ผลลัพธ์หลังการเรียงลำดับ:", sorted_data)
print("เวลาที่ใช้: %.6f วินาที" % (end_time - start_time))
