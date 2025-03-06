def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # เลือก pivot (ในที่นี้เลือกตัวสุดท้าย)
    pivot = arr[-1]
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # รวมผลลัพธ์
    return quick_sort(left) + [pivot] + quick_sort(right)
import time
# ทดสอบ Quick Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = quick_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")