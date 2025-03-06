def insertion_sort_descending(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] < key:  # เปลี่ยนเงื่อนไขเพื่อเรียงจากมากไปน้อย
            arr[j + 1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j + 1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบฟังก์ชัน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
sorted_data = insertion_sort_descending(test_data.copy())
print("Sorted array (Descending):", sorted_data)