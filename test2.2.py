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
# ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกัน
test_data_dup = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
print("ข้อมูลก่อนเรียง:", test_data_dup)

start_time = time.time()
sorted_data_dup = insertion_sort(test_data_dup.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง (จากมากไปน้อย):", sorted_data_dup)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
