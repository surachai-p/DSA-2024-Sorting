def median_of_three(arr):
    """ เลือก pivot โดยใช้ median ของค่าที่ตำแหน่งแรก, กลาง และสุดท้าย """
    if len(arr) < 3:
        return arr[0]  # ถ้าข้อมูลมีน้อยกว่า 3 ตัว ให้ใช้ตัวแรกเป็น pivot
    
    first, mid, last = arr[0], arr[len(arr) // 2], arr[-1]

    # คืนค่าค่าที่อยู่ตรงกลาง (median)
    if (first < mid < last) or (last < mid < first):
        return mid
    elif (mid < first < last) or (last < first < mid):
        return first
    else:
        return last

def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    # เลือก pivot โดยใช้ median of three
    pivot = median_of_three(arr)
    print(f"{indent}เลือก pivot = {pivot}")
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, middle = {middle}, right = {right}")
    
    # เรียกใช้ Quick Sort กับซ้ายและขวา
    result = quick_sort_with_steps(left, depth + 1) + middle + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
quick_sort_with_steps(test_data.copy())
