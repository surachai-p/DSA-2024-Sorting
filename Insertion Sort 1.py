def insertion_sort(arr):
    # วนลูปตั้งแต่ตัวที่ 2 ถึงตัวสุดท้าย
    for i in range(1, len(arr)):
        key = arr[i]  # ค่าที่จะนำไปแทรก
        j = i - 1  # ดัชนีของตัวก่อนหน้า
        
        # ย้ายตัวที่มีค่าต่ำกว่า key ไปทางขวา (เรียงจากมากไปน้อย)
        while j >= 0 and arr[j] < key:  # เปลี่ยนเงื่อนไขเป็น arr[j] < key เพื่อเรียงจากมากไปน้อย
            arr[j+1] = arr[j]
            j -= 1
        
        # แทรก key ลงในตำแหน่งที่เหมาะสม
        arr[j+1] = key
    
    return arr

import time
# ทดสอบ Insertion Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = insertion_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")

def insertion_sort_with_steps(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] < key:  # เปลี่ยนเงื่อนไขเป็น arr[j] < key เพื่อเรียงจากมากไปน้อย
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+1]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
insertion_sort_with_steps(test_data.copy())
