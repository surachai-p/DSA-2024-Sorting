def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # ถ้าไม่มีการสลับในรอบนี้ แสดงว่าข้อมูลเรียงลำดับแล้ว
        if not swapped:
            break
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
sorted_data = bubble_sort(test_data.copy())
print(f"ผลลัพธ์ที่ได้: {sorted_data}")
