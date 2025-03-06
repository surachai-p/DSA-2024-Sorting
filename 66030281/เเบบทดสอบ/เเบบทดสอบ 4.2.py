import time

def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    
    if len(arr) <= 1:
        return arr  # กรณีฐาน (Base case)
    
    # เลือก pivot แบบ Median-of-Three
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    
    pivot_candidates = [first, middle, last]
    pivot_candidates.sort()
    pivot = pivot_candidates[1]  # เลือกค่ากลางเป็น pivot
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # รองรับค่าซ้ำ
    right = [x for x in arr if x > pivot]
    
    return quick_sort_with_steps(left, depth + 1) + middle + quick_sort_with_steps(right, depth + 1)

# ชุดข้อมูลที่มีค่าซ้ำกันจำนวนมาก
test_data = [5, 1, 3, 5, 2, 1, 3, 5, 2, 1, 4, 4, 5, 3, 2, 5, 1, 4, 3, 2]

# วัดเวลาการทำงาน
start_time = time.time()
sorted_data = quick_sort_with_steps(test_data.copy())
end_time = time.time()

# แสดงผลลัพธ์
print("ชุดข้อมูลก่อนเรียงลำดับ:", test_data)
print("ผลลัพธ์หลังการเรียงลำดับ:", sorted_data)
print("เวลาที่ใช้: %.6f วินาที" % (end_time - start_time))
