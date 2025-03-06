import time
from quick_sort_function import quick_sort , quick_sort_with_steps

# ทดสอบ Quick Sort
test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
quick_sort_with_steps(test_data.copy())

start_time = time.time()
sorted_data = quick_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")