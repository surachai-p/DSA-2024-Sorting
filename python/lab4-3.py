def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    # เลือก pivot โดยใช้ค่าของตำแหน่งแรก ตรงกลาง และสุดท้าย
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    
    pivot_candidates = [first, middle, last]
    pivot_candidates.sort()
    pivot = pivot_candidates[1]  # เลือก pivot เป็นค่ากลางของสามค่าดังกล่าว
    
    print(f"{indent}เลือก pivot = {pivot} จาก {first}, {middle}, {last}")
    
    # แบ่งข้อมูลโดยไม่ให้ pivot เข้ามาใน left และ right
    left = [x for x in arr if x < pivot]  # ค่าที่น้อยกว่า pivot
    right = [x for x in arr if x > pivot]  # ค่าที่มากกว่า pivot
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")
    
    # เรียกฟังก์ชัน recursive สำหรับ left และ right
    result = quick_sort_with_steps(left, depth + 1) + [pivot] + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

# ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกัน
test_data_with_duplicates = [10, 5, 8, 10, 10, 6, 7, 10]
sorted_data = quick_sort_with_steps(test_data_with_duplicates.copy())
print(f"ผลลัพธ์สุดท้าย: {sorted_data}")
