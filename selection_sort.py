import time
from selection_sort_function import selection_sort , selection_sort_with_steps

# ทดสอบ Selection Sort
test_data = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
selection_sort_with_steps(test_data.copy())

start_time = time.time()
sorted_data = selection_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")