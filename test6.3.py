
def merge_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    # แบ่งข้อมูลออกเป็นสองส่วน
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")
    
    # เรียกใช้ recursive กับส่วนย่อย
    left = merge_sort_with_steps(left, depth + 1)
    right = merge_sort_with_steps(right, depth + 1)
    
    # รวมสองส่วนกลับเข้าด้วยกัน
    result = merge_with_steps(left, right, depth)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

def merge_with_steps(left, right, depth=0):
    indent = "  " * depth
    print(f"{indent}merge({left}, {right})")
    
    result = []
    i = j = 0
    
    # เปรียบเทียบและนำค่าที่น้อยกว่าใส่ในผลลัพธ์
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print(f"{indent}  {left[i]} <= {right[j]}, เลือก {left[i]} จาก left")
            result.append(left[i])
            i += 1
        else:
            print(f"{indent}  {left[i]} > {right[j]}, เลือก {right[j]} จาก right")
            result.append(right[j])
            j += 1
        print(f"{indent}  ผลลัพธ์ชั่วคราว: {result}")
    
    # เพิ่มส่วนที่เหลือ
    if i < len(left):
        print(f"{indent}  เพิ่มส่วนที่เหลือจาก left: {left[i:]}")
        result.extend(left[i:])
    if j < len(right):
        print(f"{indent}  เพิ่มส่วนที่เหลือจาก right: {right[j:]}")
        result.extend(right[j:])
    
    print(f"{indent}  ผลลัพธ์สุดท้าย: {result}")
    return result

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
merge_sort_with_steps(test_data.copy())
