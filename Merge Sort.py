import time
from Merge_Sort_function import merge_sort , merge_sort_with_steps

test_data = [1, 2, 3, 4, 5,6,7,8,9,10]
merge_sort_with_steps(test_data.copy())

start_time = time.time()
sorted_data = merge_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")