def bubble_sort(arr):
    n = len(arr)
    
    # ทำการวนลูปเพื่อเปรียบเทียบและสลับตำแหน่ง
    for i in range(n):
        # ในแต่ละรอบ ตัวเลขที่มีค่ามากที่สุดจะถูกเลื่อนไปทางขวาสุด
        # จึงไม่จำเป็นต้องตรวจสอบตำแหน่งที่เรียงลำดับแล้ว
        for j in range(0, n-i-1):
            # เปรียบเทียบคู่ติดกัน
            if arr[j] > arr[j+1]:
                # สลับตำแหน่ง
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
import time

# ทดสอบ Bubble Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = bubble_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")