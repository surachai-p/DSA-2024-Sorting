import random
import time

# Merge Sort
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
size = 10000  # ขนาดชุดข้อมูล
test_data = list(range(1, size + 1))  # ข้อมูลเรียงลำดับจากน้อยไปหามาก
# สลับตำแหน่งสองสามตัวเพื่อให้มันเกือบเรียง
for _ in range(100):
    i, j = random.sample(range(size), 2)
    test_data[i], test_data[j] = test_data[j], test_data[i]

# ทดสอบเวลา Merge Sort
merge_sort_data = test_data.copy()
start_time = time.time()
merge_sort(merge_sort_data)
merge_sort_time = (time.time() - start_time) * 1000  # มิลลิวินาที

# แสดงผลลัพธ์
print(f"เวลา Merge Sort: {merge_sort_time:.6f} มิลลิวินาที")
