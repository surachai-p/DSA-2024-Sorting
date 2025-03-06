def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # กำหนดระยะห่างเริ่มต้น
    
    # ลดระยะห่างลงเรื่อยๆ จนเหลือ 1
    while gap > 0:
        # ใช้ Insertion Sort กับแต่ละกลุ่มของข้อมูลที่ห่างกันด้วยระยะ gap
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # ย้ายตัวที่มีค่ามากกว่า temp ไปทางขวา
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # ใส่ temp ลงในตำแหน่งที่เหมาะสม
            arr[j] = temp
        
        # ลดระยะห่างลงครึ่งหนึ่ง
        gap //= 2
    
    return arr

def shell_sort_with_steps(arr):
    n = len(arr)
    gap = n // 2
    
    print(f"เริ่มต้น: {arr}")
    
    while gap > 0:
        print(f"\nกำหนดระยะห่าง (gap) = {gap}")
        
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            print(f"  พิจารณาตำแหน่ง {i} (ค่า {temp}):")
            
            while j >= gap and arr[j - gap] > temp:
                print(f"    เปรียบเทียบกับตำแหน่ง {j-gap} (ค่า {arr[j-gap]}) -> ย้าย {arr[j-gap]} ไปตำแหน่ง {j}")
                arr[j] = arr[j - gap]
                j -= gap
            
            if j != i:
                print(f"    ใส่ {temp} ลงในตำแหน่ง {j}")
                arr[j] = temp
            else:
                print(f"    ไม่มีการเปลี่ยนแปลง")
            
            print(f"    ข้อมูลหลังการพิจารณา: {arr}")
        
        gap //= 2
    
    return arr