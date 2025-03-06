def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # เลือก pivot โดยใช้การเปรียบเทียบตำแหน่งแรก ตำแหน่งกลาง และตำแหน่งสุดท้าย
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]

    # เปรียบเทียบเพื่อเลือก pivot ที่ดีที่สุด
    if first > middle:
        first, middle = middle, first
    if first > last:
        first, last = last, first
    if middle > last:
        middle, last = last, middle

    # เลือก pivot เป็นค่ากลาง
    pivot = middle

    # สลับ pivot กับค่าตัวสุดท้ายเพื่อให้ pivot อยู่ในตำแหน่งที่ถูกต้อง
    arr.remove(pivot)
    arr.append(pivot)

    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # รวมผลลัพธ์
    return quick_sort(left) + [pivot] + quick_sort(right)

import time

# ชุดข้อมูลที่มีค่าซ้ำมาก
test_data1 = [5, 5, 5, 5, 5, 5, 5]
test_data2 = [10, 9, 9, 8, 8, 7, 7, 6, 6, 6]

# ทดสอบ Quick Sort กับชุดข้อมูลที่มีค่าซ้ำ
print("ทดสอบกับชุดข้อมูลที่มีค่าซ้ำมาก")

start_time = time.time()
sorted_data1 = quick_sort(test_data1.copy())
end_time = time.time()

print("ข้อมูลก่อนเรียง:", test_data1)
print("ข้อมูลหลังเรียง:", sorted_data1)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที\n")

# ทดสอบกับชุดข้อมูลที่มีค่าซ้ำหลายค่าผสม
start_time = time.time()
sorted_data2 = quick_sort(test_data2.copy())
end_time = time.time()

print("ข้อมูลก่อนเรียง:", test_data2)
print("ข้อมูลหลังเรียง:", sorted_data2)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
