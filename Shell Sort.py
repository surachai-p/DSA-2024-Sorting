import time
from Shell_Sort_function import shell_sort , shell_sort_with_steps


# ทดสอบ Shell Sort
test_data = [1, 3, 2, 4, 5, 6, 7, 8, 9,10]
shell_sort_with_steps(test_data.copy())

start_time = time.time()
sorted_data = shell_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")