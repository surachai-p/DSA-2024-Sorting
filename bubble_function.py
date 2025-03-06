def bubble_sort(arr):
    n = len(arr)
    
    # ทำการวนลูปเพื่อเปรียบเทียบและสลับตำแหน่ง
    for i in range(n):
        swapped = False
        # ในแต่ละรอบ ตัวเลขที่มีค่ามากที่สุดจะถูกเลื่อนไปทางขวาสุด
        # จึงไม่จำเป็นต้องตรวจสอบตำแหน่งที่เรียงลำดับแล้ว
        for j in range(0, n-i-1):
            # เปรียบเทียบคู่ติดกัน
            if arr[j] > arr[j+1]:
                # สลับตำแหน่ง
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if swapped == False:
                break
    return arr

def bubble_sort_with_steps(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        print(f"รอบที่ {i+1}:")
        
        for j in range(0, n-i-1):
            # แสดงการเปรียบเทียบในแต่ละขั้นตอน
            print(f"  เปรียบเทียบ {arr[j]} กับ {arr[j+1]}", end=" -> ")
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"สลับ: {arr}")
            else:
                print(f"ไม่สลับ: {arr}")
        
        # ถ้าไม่มีการสลับในรอบนี้ แสดงว่าข้อมูลเรียงเรียบร้อยแล้ว
        if not swapped:
            print(f"  ไม่มีการสลับในรอบนี้ - ข้อมูลเรียงลำดับแล้ว")
            break
    
    return arr