def selection_sort_desc(arr):
    n = len(arr)
    
    # วนลูปเพื่อหาค่ามากที่สุดในแต่ละรอบ
    for i in range(n):
        # สมมติว่าตำแหน่งปัจจุบันมีค่ามากที่สุด
        max_idx = i
        
        # หาค่าที่มากกว่าในส่วนที่เหลือ
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:  # เปลี่ยนเป็นหาค่ามากที่สุด
                max_idx = j
        
        # สลับค่าที่มากที่สุดกับตำแหน่งปัจจุบัน
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    return arr

import time

# ทดสอบ Selection Sort แบบเรียงจากมากไปน้อย
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = selection_sort_desc(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง (จากมากไปน้อย):", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
