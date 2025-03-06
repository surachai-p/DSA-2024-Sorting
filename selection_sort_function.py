def selection_sort(arr):
    n = len(arr)
    
    # วนลูปเพื่อหาค่าน้อยที่สุดในแต่ละรอบ
    for i in range(n):
        # สมมติว่าตำแหน่งปัจจุบันมีค่าน้อยที่สุด
        min_idx = i
        
        # หาค่าที่น้อยกว่าในส่วนที่เหลือ
        for j in range(i+1, n):
            if arr[j] > arr[min_idx]:
                min_idx = j
        
        # สลับค่าที่น้อยที่สุดกับตำแหน่งปัจจุบัน
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def selection_sort_with_steps(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        print(f"\nรอบที่ {i+1}:")
        print(f"  ข้อมูลปัจจุบัน: {arr}")
        print(f"  ค้นหาค่าน้อยที่สุดในตำแหน่ง {i} ถึง {n-1}")
        
        for j in range(i+1, n):
            print(f"    เปรียบเทียบ {arr[min_idx]} กับ {arr[j]}", end=" -> ")
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"พบค่าที่น้อยกว่า: {arr[j]}")
            else:
                print("ไม่มีการเปลี่ยนแปลง")
        
        print(f"  ค่าน้อยที่สุดคือ {arr[min_idx]} ที่ตำแหน่ง {min_idx}")
        if i != min_idx:
            print(f"  สลับ {arr[i]} กับ {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"  ไม่ต้องสลับเนื่องจากอยู่ในตำแหน่งที่ถูกต้องแล้ว")
        
        print(f"  ข้อมูลหลังรอบที่ {i+1}: {arr}")
    
    return arr