def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1  

        # ย้ายค่าที่น้อยกว่า key ไปทางขวา
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # แทรก key ลงในตำแหน่งที่เหมาะสม
        arr[j + 1] = key

    return arr

import time

# ทดสอบ Insertion Sort แบบเรียงจากมากไปน้อย
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = insertion_sort(test_data.copy())
end_time = time.time()
print("ข้อมูลหลังเรียง (จากมากไปน้อย):", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
