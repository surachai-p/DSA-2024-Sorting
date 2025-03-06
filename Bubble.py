import time
from bubble_function import bubble_sort , bubble_sort_with_steps

test_data = [1, 2, 3, 4, 5,6,7,8,9,10]
## [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
bubble_sort_with_steps(test_data.copy())
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = bubble_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")