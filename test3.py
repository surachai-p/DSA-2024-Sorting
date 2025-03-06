def selection_sort(arr):
    n = len(arr)
    
    # วนลูปเพื่อหาค่าน้อยที่สุดในแต่ละรอบ
    for i in range(n):
        # สมมติว่าตำแหน่งปัจจุบันมีค่าน้อยที่สุด
        min_idx = i
        
        # หาค่าที่น้อยกว่าในส่วนที่เหลือ
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # สลับค่าที่น้อยที่สุดกับตำแหน่งปัจจุบัน
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
import time
# ทดสอบ Selection Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = selection_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")