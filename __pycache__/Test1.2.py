def bubble_sort(arr):
    n = len(arr)
    
    # ทำการวนลูปเพื่อเปรียบเทียบและสลับตำแหน่ง
    for i in range(n):
        swapped = False  # ตัวแปรสำหรับตรวจสอบการสลับตำแหน่ง
        
        # ในแต่ละรอบ ตัวเลขที่มีค่ามากที่สุดจะถูกเลื่อนไปทางขวาสุด
        # จึงไม่จำเป็นต้องตรวจสอบตำแหน่งที่เรียงลำดับแล้ว
        for j in range(0, n-i-1):
            # เปรียบเทียบคู่ติดกัน
            if arr[j] > arr[j+1]:
                # สลับตำแหน่ง
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # มีการสลับตำแหน่ง
        
        # ถ้าไม่มีการสลับตำแหน่งเลย แสดงว่าอาร์เรย์เรียงลำดับแล้ว
        if not swapped:
            break
    
    return arr

import time

# ทดสอบ Bubble Sort กับชุดข้อมูลที่เรียงลำดับแล้ว
test_data_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("ข้อมูลก่อนเรียง:", test_data_sorted)

start_time = time.time()
sorted_data = bubble_sort(test_data_sorted.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
