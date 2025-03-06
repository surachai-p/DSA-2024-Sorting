import time
from Insertion_function import insertion_sort,insertion_sort_with_steps

test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9 ,10 ,20 ,30 ,41, 515 ,15 ,5151 ,1851, 1152, 16519165 ,1 ,12,8516 ,51 ,651,65,165,1]
insertion_sort_with_steps(test_data.copy())
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = insertion_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")