import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # แบ่งข้อมูลออกเป็นสองส่วน
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # เรียกใช้ recursive กับส่วนย่อย
    left = merge_sort(left)
    right = merge_sort(right)
    
    # รวมสองส่วนกลับเข้าด้วยกัน
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # เปรียบเทียบและนำค่าที่น้อยกว่าใส่ในผลลัพธ์
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # เพิ่มส่วนที่เหลือ
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# สร้างชุดข้อมูลที่เกือบเรียงลำดับแล้ว
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# สลับตัวที่ 3 และ 7
test_data[2], test_data[6] = test_data[6], test_data[2]

print("ข้อมูลก่อนเรียง:", test_data)

# วัดเวลาในการทำงาน
start_time = time.time()
sorted_data = merge_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
