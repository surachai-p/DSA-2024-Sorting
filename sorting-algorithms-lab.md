# อัลกอริทึมการเรียงลำดับ (Sorting Algorithms)

## วัตถุประสงค์
1. อธิบายหลักการทำงานของอัลกอริทึมการเรียงลำดับแบบต่างๆ
2. เขียนโค้ด Python เพื่อนำอัลกอริทึมการเรียงลำดับไปใช้งาน
3. วิเคราะห์และเปรียบเทียบประสิทธิภาพของอัลกอริทึมการเรียงลำดับแต่ละแบบ

## อุปกรณ์ที่ใช้
1. คอมพิวเตอร์ที่ติดตั้ง Python 3.x
2. โปรแกรม text editor หรือ IDE สำหรับเขียนโค้ด Python (เช่น VSCode, PyCharm)
3. ไลบรารี time สำหรับวัดประสิทธิภาพ

## เนื้อหาทฤษฎี
อัลกอริทึมการเรียงลำดับ (Sorting Algorithms) เป็นชุดคำสั่งที่ใช้ในการจัดเรียงข้อมูลให้อยู่ในลำดับที่ต้องการ ไม่ว่าจะเป็นลำดับจากน้อยไปมาก หรือจากมากไปน้อย ในใบงานจะศึกษาอัลกอริทึม 8 แบบ ได้แก่:

1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Quick Sort
5. Shell Sort
6. Merge Sort
7. Radix Sort
8. Counting Sort


แต่ละอัลกอริทึมมีวิธีการทำงานและประสิทธิภาพที่แตกต่างกัน

## การทดลองที่ 1: Bubble Sort

### ทฤษฎี
Bubble Sort เป็นอัลกอริทึมที่ง่ายที่สุด โดยทำการเปรียบเทียบข้อมูลที่อยู่ติดกันทีละคู่ แล้วสลับตำแหน่งกันหากพบว่าข้อมูลไม่อยู่ในลำดับที่ถูกต้อง ทำซ้ำไปเรื่อยๆ จนกว่าข้อมูลทั้งหมดจะเรียงลำดับถูกต้อง

### ขั้นตอนการทดลอง
1. เขียนฟังก์ชัน Bubble Sort ตามโค้ดตัวอย่าง
```python
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
```

2. ทดสอบฟังก์ชันด้วยชุดข้อมูลต่อไปนี้
```python
import time

# ทดสอบ Bubble Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = bubble_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
```

### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

*ตอบ* ![image](https://github.com/user-attachments/assets/cd508067-2370-4a3c-99a3-ef138db9a643)

3. สังเกตขั้นตอนการเรียงลำดับโดยเพิ่มการแสดงผลในแต่ละรอบ
```python
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

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
bubble_sort_with_steps(test_data.copy())
```
### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

*ตอบ* ![image](https://github.com/user-attachments/assets/69bdb291-d075-40c3-9b30-0f0aaaed21e5)

### แบบทดสอบ
1. ปรับปรุงโค้ด ในฟังก์ชัน bubble_sort(arr)  ให้มีประสิทธิภาพมากขึ้นโดยเพิ่มการตรวจสอบว่ามีการสลับตำแหน่งในแต่ละรอบหรือไม่ ถ้าไม่มีการสลับแสดงว่าข้อมูลเรียงลำดับแล้ว สามารถหยุดการทำงานได้ทันที
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดแบบทดสอบ
```python
import time

def insertion_sort_descending(arr):
    """
    เรียงลำดับข้อมูลในอาร์เรย์โดยใช้อัลกอริทึม Insertion Sort จากมากไปน้อย

    Args:
        arr: อาร์เรย์ของข้อมูลที่ต้องการเรียงลำดับ

    Returns:
        อาร์เรย์ของข้อมูลที่เรียงลำดับแล้ว (จากมากไปน้อย)
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # เปลี่ยนเงื่อนไขการเปรียบเทียบเป็น arr[j] < key
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

# ทดสอบ Insertion Sort (เรียงจากมากไปน้อย)
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

data_to_sort = test_data.copy()

start_time = time.time()
sorted_data = insertion_sort_descending(data_to_sort)
end_time = time.time()

print("ข้อมูลหลังเรียง (มากไปน้อย):", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")

บันทึกโค้ด แบบทดสอบ
```
บันทึกรูปผลแบบทดสอบ

*ตอบ* ![image](https://github.com/user-attachments/assets/c5312eab-0946-4c40-8b2f-c7d0e617770f)

1. ทดสอบกับชุดข้อมูลที่เรียงลำดับแล้ว เช่น `[1, 2, 3, 4, 5,6,7,8,9,10]` และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
จากผลการทดลอง อัลกอริทึม Bubble Sort ตรวจสอบข้อมูลที่เรียงลำดับอยู่แล้ว โดยไม่เกิดการสลับตำแหน่งเลยในแต่ละรอบ ทำให้หยุดทำงานก่อนครบทุกขั้นตอน ส่งผลให้การทำงานมีประสิทธิภาพและใช้เวลาน้อยลง

```
บันทึกรูปผลแบบทดสอบ
![image](https://github.com/user-attachments/assets/edecb7f9-7d10-4f2a-8400-9c7b53fc09af)



## การทดลองที่ 2: Insertion Sort
### ทฤษฎี
Insertion Sort คล้ายกับวิธีที่เราเรียงไพ่บนมือ โดยเริ่มจากข้อมูลตัวแรกแล้วค่อยๆ แทรกข้อมูลถัดไปเข้าไปในตำแหน่งที่เหมาะสม

### ขั้นตอนการทดลอง
1. เขียนฟังก์ชัน Insertion Sort ตามโค้ดตัวอย่าง
```python
def insertion_sort(arr):
    # วนลูปตั้งแต่ตัวที่ 2 ถึงตัวสุดท้าย
    for i in range(1, len(arr)):
        key = arr[i]  # ค่าที่จะนำไปแทรก
        j = i - 1  # ดัชนีของตัวก่อนหน้า
        
        # ย้ายตัวที่มีค่ามากกว่า key ไปทางขวา
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        # แทรก key ลงในตำแหน่งที่เหมาะสม
        arr[j+1] = key
    
    return arr
```

2. ทดสอบฟังก์ชันด้วยชุดข้อมูลต่อไปนี้
```python
import time
# ทดสอบ Insertion Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = insertion_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
```
### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/62b04946-90eb-46bc-8ca5-c29e391db868)

3. สังเกตขั้นตอนการเรียงลำดับโดยเพิ่มการแสดงผลในแต่ละรอบ
```python
def insertion_sort_with_steps(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
insertion_sort_with_steps(test_data.copy())
```
### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/3e223bdf-dc38-4783-8c98-ed7732db326c)

### แบบทดสอบ
1. ปรับปรุงอัลกอริทึม Insertion Sort ให้รองรับการเรียงลำดับจากมากไปน้อย
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```python
def insertion_sort_descending(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] < key:  # เปลี่ยนเงื่อนไขเพื่อเรียงจากมากไปน้อย
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
insertion_sort_descending(test_data.copy())
```
![image](https://github.com/user-attachments/assets/b8d163b9-dba8-4eb0-81a8-454a8d873d2c)


2. ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกัน เช่น `[3, 1, 4, 1, 5, 9, 2, 6, 5, 9]` และตรวจสอบผลลัพธ์
### บันทึกผลแบบทดสอบ
```html
def insertion_sort_descending(arr):
    print(f"เริ่มต้น: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nรอบที่ {i}: พิจารณา key = {key}")
        
        while j >= 0 and arr[j] < key:  # เรียงจากมากไปน้อย
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกัน
test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
sorted_data = insertion_sort_descending(test_data.copy())

print("\nผลลัพธ์ที่เรียงลำดับแล้ว:", sorted_data)

```
บันทึกรูปผลแบบทดสอบ

![image](https://github.com/user-attachments/assets/0fcd2045-874f-4191-a69d-232d9e7ba65f)
![image](https://github.com/user-attachments/assets/a696e9b7-bd46-4b05-92d2-f97570b8273e)


## การทดลองที่ 3: Selection Sort
### ทฤษฎี
Selection Sort ทำงานโดยการค้นหาค่าที่น้อยที่สุดในส่วนที่ยังไม่ได้เรียงลำดับ แล้วนำมาไว้ในตำแหน่งแรกของส่วนที่ยังไม่ได้เรียงลำดับ ทำซ้ำจนครบทุกตำแหน่ง

### ขั้นตอนการทดลอง
1. เขียนฟังก์ชัน Selection Sort ตามโค้ดตัวอย่าง
```python
def selection_sort(arr):
    n = len(arr)
    
    # วนลูปเพื่อหาค่าน้อยที่สุดในแต่ละรอบ
    for i in range(n):
        # สมมติว่าตำแหน่งปัจจุบันมีค่าน้อยที่สุด
        min_idx = i
        
        # หาค่าที่น้อยกว่าในส่วนที่เหลือ
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # สลับค่าที่น้อยที่สุดกับตำแหน่งปัจจุบัน
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
```

2. ทดสอบฟังก์ชันด้วยชุดข้อมูลต่อไปนี้
```python
import time
# ทดสอบ Selection Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = selection_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
```
### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![Screenshot 2025-03-06 211254](https://github.com/user-attachments/assets/2d808e27-e374-4a4b-9417-c0b7dc097df8)

3. สังเกตขั้นตอนการเรียงลำดับโดยเพิ่มการแสดงผลในแต่ละรอบ
```python
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

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
selection_sort_with_steps(test_data.copy())
```

### แบบทดสอบ
1. ปรับปรุงอัลกอริทึม Selection Sort ให้รองรับการเรียงลำดับจากมากไปน้อย 
  ### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```python
def selection_sort_descending_with_steps(arr):
    n = len(arr)
    
    for i in range(n):
        max_idx = i
        print(f"\nรอบที่ {i+1}:")
        print(f"  ข้อมูลปัจจุบัน: {arr}")
        print(f"  ค้นหาค่ามากที่สุดในตำแหน่ง {i} ถึง {n-1}")
        
        for j in range(i+1, n):
            print(f"    เปรียบเทียบ {arr[max_idx]} กับ {arr[j]}", end=" -> ")
            if arr[j] > arr[max_idx]:  # เปลี่ยนเป็นการหาค่าที่มากที่สุด
                max_idx = j
                print(f"พบค่าที่มากกว่า: {arr[j]}")
            else:
                print("ไม่มีการเปลี่ยนแปลง")
        
        print(f"  ค่ามากที่สุดคือ {arr[max_idx]} ที่ตำแหน่ง {max_idx}")
        if i != max_idx:
            print(f"  สลับ {arr[i]} กับ {arr[max_idx]}")
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            print(f"  ไม่ต้องสลับเนื่องจากอยู่ในตำแหน่งที่ถูกต้องแล้ว")
        
        print(f"  ข้อมูลหลังรอบที่ {i+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
selection_sort_descending_with_steps(test_data.copy())
```

*ตอบ* 
![image](https://github.com/user-attachments/assets/5b8a77c4-06df-4169-8adf-825fc3242978)
![image](https://github.com/user-attachments/assets/1e3af6c3-b024-42d0-b29b-08a214a072ad)
![image](https://github.com/user-attachments/assets/6edff28e-1f89-4e8f-8ec9-d62a2ce3d59a)

2. วัดประสิทธิภาพเมื่อทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว (nearly sorted data)
### บันทึกผลแบบทดสอบ
```html
มันจะต้องทำการเปรียบเทียบทุกคู่ของข้อมูลในทุกๆ รอบ แม้ว่าข้อมูลจะเกือบเรียงลำดับแล้วก็ตาม

แม้ในกรณีที่มีการเปลี่ยนแปลงเพียงเล็กน้อย 
```
บันทึกรูปผลแบบทดสอบ

![image](https://github.com/user-attachments/assets/4801bd52-db92-4ae9-93e2-a9f4415ee963)

## การทดลองที่ 4: Quick Sort

### ทฤษฎี
Quick Sort เป็นอัลกอริทึมที่ใช้หลักการ "แบ่งแล้วเอาชนะ" (divide and conquer) โดยเลือกตัวเลขหนึ่งเป็น "pivot" แล้วแบ่งข้อมูลออกเป็นสองส่วน: ส่วนที่น้อยกว่า pivot และส่วนที่มากกว่า pivot จากนั้นทำซ้ำกับแต่ละส่วนย่อย

### ขั้นตอนการทดลอง
1. เขียนฟังก์ชัน Quick Sort ตามโค้ดตัวอย่าง
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # เลือก pivot (ในที่นี้เลือกตัวสุดท้าย)
    pivot = arr[-1]
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # รวมผลลัพธ์
    return quick_sort(left) + [pivot] + quick_sort(right)
```

2. ทดสอบฟังก์ชันด้วยชุดข้อมูลต่อไปนี้
```python
import time
# ทดสอบ Quick Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = quick_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
```

### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/89e68052-f962-4dd3-93a5-9387d5898984)

3. เขียนฟังก์ชันที่แสดงขั้นตอนการทำงาน
```python
def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    pivot = arr[-1]
    print(f"{indent}เลือก pivot = {pivot}")
    
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")
    
    result = quick_sort_with_steps(left, depth + 1) + [pivot] + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
quick_sort_with_steps(test_data.copy())
```

### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/60945db8-b24d-45d9-8a52-c6be14f24434)

### แบบทดสอบ
1. ปรับปรุงการเลือก pivot โดยใช้การเปรียบเทียบตำแหน่งแรก ตำแหน่งตรงกลาง และแหน่งสุดท้าย
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```python
import time

# ฟังก์ชัน Quick Sort ที่เลือก pivot โดยใช้ Median of Three
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # เลือก pivot โดยใช้การเปรียบเทียบตำแหน่งแรก, ตำแหน่งกลาง และตำแหน่งสุดท้าย
    first = arr[0]
    last = arr[-1]
    middle = arr[len(arr) // 2]
    
    # ใช้ median of three เพื่อเลือก pivot
    pivot = sorted([first, middle, last])[1]  # เลือกค่ากลางจากสามค่าที่เปรียบเทียบ
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr if x < pivot]  # ใช้ < แทน <= เพื่อหลีกเลี่ยงค่าที่เท่ากับ pivot
    right = [x for x in arr if x > pivot]  # ใช้ > แทน >= เพื่อหลีกเลี่ยงค่าที่เท่ากับ pivot
    
    # รวมผลลัพธ์
    return quick_sort(left) + [pivot] + quick_sort(right)

# ทดสอบ Quick Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = quick_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")

# ฟังก์ชัน Quick Sort พร้อมการแสดงขั้นตอน
def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    first = arr[0]
    last = arr[-1]
    middle = arr[len(arr) // 2]
    
    # ใช้ median of three เพื่อเลือก pivot
    pivot = sorted([first, middle, last])[1]
    print(f"{indent}เลือก pivot = {pivot} (จาก {first}, {middle}, {last})")
    
    left = [x for x in arr if x < pivot]  # ใช้ < แทน <=
    right = [x for x in arr if x > pivot]  # ใช้ > แทน >=
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")
    
    result = quick_sort_with_steps(left, depth + 1) + [pivot] + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
quick_sort_with_steps(test_data.copy())
```

![image](https://github.com/user-attachments/assets/8043cf30-6dc9-4197-9bb3-4b03154c366e)

2. ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกันจำนวนมาก และตรวจสอบผลลัพธ์
### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```html
- ลดโอกาสกรณีที่ Quick Sort ทำงานช้า (เมื่อข้อมูลเรียงลำดับแล้วหรือเกือบเรียงลำดับ)
- ทำให้แบ่งข้อมูลได้สมดุลมากขึ้น ส่งผลให้ประสิทธิภาพดีขึ้นในกรณีข้อมูลหลากหลาย
- ลดจำนวนขั้นตอนการเรียกซ้ำ (recursive calls) ในกรณีข้อมูลมีค่าซ้ำกันจำนวนมาก
```

![image](https://github.com/user-attachments/assets/09ee0604-fc62-45da-bb9d-43c8b0ecf413)


## การทดลองที่ 5: Shell Sort

### ทฤษฎี
Shell Sort เป็นการปรับปรุงจาก Insertion Sort โดยเริ่มจากการเปรียบเทียบและสลับตำแหน่งของข้อมูลที่อยู่ห่างกันด้วยระยะทางค่อนข้างมากก่อน แล้วค่อยๆ ลดระยะทางลงจนเป็นการเปรียบเทียบข้อมูลที่อยู่ติดกัน

### ขั้นตอนการทดลอง
1. เขียนฟังก์ชัน Shell Sort ตามโค้ดตัวอย่าง
```python
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
```

2. ทดสอบฟังก์ชันด้วยชุดข้อมูลต่อไปนี้
```python
import time
# ทดสอบ Shell Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = shell_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
```
### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/ddddf7d3-ac89-4fe0-9cd7-3e065fab63c0)


3. เขียนฟังก์ชันที่แสดงขั้นตอนการทำงาน
```python
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

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
shell_sort_with_steps(test_data.copy())
```
### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/209e1a2c-073c-49d8-83ef-a3abc295a3c3)
![image](https://github.com/user-attachments/assets/fd8cec38-5779-4050-939b-4dd33955b547)
![image](https://github.com/user-attachments/assets/76d34352-2c2b-4d14-b527-1296a1d80c0b)
![image](https://github.com/user-attachments/assets/731a4a05-a3c5-4763-9a7f-3666538bd810)

### แบบทดสอบ
1. เปรียบเทียบประสิทธิภาพกับ Insertion Sort ปกติเมื่อทดสอบกับชุดข้อมูลขนาดใหญ่
   ### บันทึกผลแบบทดสอบ
```html
  import time
import random

# Shell Sort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# สร้างชุดข้อมูลขนาดใหญ่
large_data = [random.randint(1, 10000) for _ in range(10000)]

# ทดสอบ Shell Sort
shell_data = large_data.copy()
start_time = time.time()
shell_sort(shell_data)
shell_time = time.time() - start_time

# ทดสอบ Insertion Sort
insertion_data = large_data.copy()
start_time = time.time()
insertion_sort(insertion_data)
insertion_time = time.time() - start_time

print(f"Shell Sort ใช้เวลา: {shell_time:.6f} วินาที")
print(f"Insertion Sort ใช้เวลา: {insertion_time:.6f} วินาที")
```
บันทึกรูปผลแบบทดสอบ

![image](https://github.com/user-attachments/assets/22e4e50d-03ec-4ac2-bbe9-c04811e3edfc)

2. ทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
 import time
import random

# Shell Sort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# สร้างชุดข้อมูลที่เกือบเรียงลำดับแล้ว
nearly_sorted_data = list(range(1, 10001))
random.shuffle(nearly_sorted_data[:100])  # สลับตำแหน่งบางส่วน

# ทดสอบ Shell Sort
shell_data = nearly_sorted_data.copy()
start_time = time.time()
shell_sort(shell_data)
shell_time = time.time() - start_time

# ทดสอบ Insertion Sort
insertion_data = nearly_sorted_data.copy()
start_time = time.time()
insertion_sort(insertion_data)
insertion_time = time.time() - start_time

print(f"Shell Sort ใช้เวลา: {shell_time:.6f} วินาที")
print(f"Insertion Sort ใช้เวลา: {insertion_time:.6f} วินาที")
```
บันทึกรูปผลแบบทดสอบ

![image](https://github.com/user-attachments/assets/a8f9048a-6905-4860-81d8-de1afc46022f)

## การทดลองที่ 6: Merge Sort

### ทฤษฎี
Merge Sort เป็นอัลกอริทึมที่ใช้หลักการ "แบ่งแล้วเอาชนะ" เช่นเดียวกับ Quick Sort แต่ทำงานโดยการแบ่งข้อมูลออกเป็นสองส่วนเท่าๆ กัน เรียงลำดับแต่ละส่วน แล้วรวมกลับเข้าด้วยกัน

### ขั้นตอนการทดลอง
1. เขียนฟังก์ชัน Merge Sort ตามโค้ดตัวอย่าง
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # แบ่งข้อมูลออกเป็นสองส่วน
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # เรียกใช้ recursive กับส่วนย่อย
    left = merge_sort(left)
    right = merge_sort(right)
    
    # รวมสองส่วนกลับเข้าด้วยกัน
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # เปรียบเทียบและนำค่าที่น้อยกว่าใส่ในผลลัพธ์
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # เพิ่มส่วนที่เหลือ
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

2. ทดสอบฟังก์ชันด้วยชุดข้อมูลต่อไปนี้
```python
import time
# ทดสอบ Merge Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = merge_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")
```

### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![image](https://github.com/user-attachments/assets/1259b22c-d0e5-4440-9670-e149ddcbd87d)


3. เขียนฟังก์ชันที่แสดงขั้นตอนการทำงาน
```python
def merge_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    # แบ่งข้อมูลออกเป็นสองส่วน
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")
    
    # เรียกใช้ recursive กับส่วนย่อย
    left = merge_sort_with_steps(left, depth + 1)
    right = merge_sort_with_steps(right, depth + 1)
    
    # รวมสองส่วนกลับเข้าด้วยกัน
    result = merge_with_steps(left, right, depth)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

def merge_with_steps(left, right, depth=0):
    indent = "  " * depth
    print(f"{indent}merge({left}, {right})")
    
    result = []
    i = j = 0
    
    # เปรียบเทียบและนำค่าที่น้อยกว่าใส่ในผลลัพธ์
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print(f"{indent}  {left[i]} <= {right[j]}, เลือก {left[i]} จาก left")
            result.append(left[i])
            i += 1
        else:
            print(f"{indent}  {left[i]} > {right[j]}, เลือก {right[j]} จาก right")
            result.append(right[j])
            j += 1
        print(f"{indent}  ผลลัพธ์ชั่วคราว: {result}")
    
    # เพิ่มส่วนที่เหลือ
    if i < len(left):
        print(f"{indent}  เพิ่มส่วนที่เหลือจาก left: {left[i:]}")
        result.extend(left[i:])
    if j < len(right):
        print(f"{indent}  เพิ่มส่วนที่เหลือจาก right: {right[j:]}")
        result.extend(right[j:])
    
    print(f"{indent}  ผลลัพธ์สุดท้าย: {result}")
    return result
```
# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
merge_sort_with_steps(test_data.copy())

### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![Screenshot 2025-03-06 220358](https://github.com/user-attachments/assets/189d991b-9242-4b09-9646-c06d7d3abfb2)
![image](https://github.com/user-attachments/assets/84c16e22-54af-4bfe-aa1a-6fd79ea39f85)
![image](https://github.com/user-attachments/assets/4a1d06a2-2a62-4cd8-9ed4-d2c9bcea3a2c)

```

### แบบทดสอบ

1. ทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
 import time

# ชุดข้อมูลที่เกือบเรียงลำดับแล้ว
nearly_sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]

# ฟังก์ชัน Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # แบ่งข้อมูลออกเป็นสองส่วน
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # เรียกใช้ recursive กับส่วนย่อย
    left = merge_sort(left)
    right = merge_sort(right)
    
    # รวมสองส่วนกลับเข้าด้วยกัน
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # เปรียบเทียบและนำค่าที่น้อยกว่าใส่ในผลลัพธ์
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # เพิ่มส่วนที่เหลือ
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# วัดประสิทธิภาพ
start_time = time.time()
sorted_data = merge_sort(nearly_sorted_data.copy())
end_time = time.time()

# แสดงผล
print("ข้อมูลที่เรียงลำดับ:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time) * 1000:.6f} มิลลิวินาที")
```
บันทึกรูปผลแบบทดสอบ

![image](https://github.com/user-attachments/assets/311d93c5-d446-436d-b16e-dd2598a3b719)


## เปรียบเทียบประสิทธิภาพการเรียงข้อมูลแต่ละวิธี
1. สร้างไฟล์เพื่อรวมโค้ดการเรียงข้อมูลทุกแบบ ตั้งชื่อไฟล์ sorting.py
```python
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

def insertion_sort(arr):
    # วนลูปตั้งแต่ตัวที่ 2 ถึงตัวสุดท้าย
    for i in range(1, len(arr)):
        key = arr[i]  # ค่าที่จะนำไปแทรก
        j = i - 1  # ดัชนีของตัวก่อนหน้า
        
        # ย้ายตัวที่มีค่ามากกว่า key ไปทางขวา
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        # แทรก key ลงในตำแหน่งที่เหมาะสม
        arr[j+1] = key
    
    return arr
def selection_sort(arr):
    n = len(arr)
    
    # วนลูปเพื่อหาค่าน้อยที่สุดในแต่ละรอบ
    for i in range(n):
        # สมมติว่าตำแหน่งปัจจุบันมีค่าน้อยที่สุด
        min_idx = i
        
        # หาค่าที่น้อยกว่าในส่วนที่เหลือ
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # สลับค่าที่น้อยที่สุดกับตำแหน่งปัจจุบัน
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # เลือก pivot (ในที่นี้เลือกตัวสุดท้าย)
    pivot = arr[-1]
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # รวมผลลัพธ์
    return quick_sort(left) + [pivot] + quick_sort(right)

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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # แบ่งข้อมูลออกเป็นสองส่วน
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # เรียกใช้ recursive กับส่วนย่อย
    left = merge_sort(left)
    right = merge_sort(right)
    
    # รวมสองส่วนกลับเข้าด้วยกัน
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # เปรียบเทียบและนำค่าที่น้อยกว่าใส่ในผลลัพธ์
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # เพิ่มส่วนที่เหลือ
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
def counting_sort(arr):
    # หาค่าสูงสุดและต่ำสุดในข้อมูล
    max_val = max(arr)
    min_val = min(arr)
    
    # คำนวณขนาดของตารางนับ
    range_of_elements = max_val - min_val + 1
    
    # สร้างตารางนับและอาร์เรย์ผลลัพธ์
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    # นับจำนวนของแต่ละค่า
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    
    # ปรับตารางนับให้เป็นตำแหน่งสะสม
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # สร้างอาร์เรย์ผลลัพธ์ (เริ่มจากท้ายสุดเพื่อให้ stable)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    # คัดลอกผลลัพธ์กลับไปยังอาร์เรย์ต้นฉบับ
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr

def radix_sort(arr):
    # หาค่าสูงสุดเพื่อกำหนดจำนวนรอบการเรียงลำดับ
    max_val = max(arr)
    
    # เรียงลำดับตามแต่ละหลัก
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # มี 10 หลัก (0-9)
    
    # นับจำนวนของแต่ละหลัก
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    
    # ปรับตารางนับให้เป็นตำแหน่งสะสม
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # สร้างอาร์เรย์ผลลัพธ์
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # คัดลอกผลลัพธ์กลับไปยังอาร์เรย์ต้นฉบับ
    for i in range(n):
        arr[i] = output[i]
```
2. เขียนโค้ดเพื่อเปรียบเทียบการเรียงข้อมูลแต่ละแบบเมื่อใช้กับอินพุตแต่ละขนาดตามตัวอย่าง การเปรียบเทียบ Bubble sort, Insertion sort และ Selection sort
   ** ทำการติดตั้ง matplotlib ด้วยคำสั่ง  pip install matplotlib  หรือ pip3 install matplotlib **
```python
import random
import time
import matplotlib.pyplot as plt
import sorting

def compare_sort():
    # ทดสอบกับขนาดข้อมูลต่างๆ
    sizes = [100,500, 1000, 5000, 10000, 20000]
    bubble_times = []
    insertion_times = []
    selection_times =[]
    
    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-999
        data = [random.randint(0, 999) for _ in range(size)]
        
        # วัดเวลา bubble Sort
        start_time = time.time()
        sorttype.bubble_sort(data.copy())
        bubble_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา insertion Sort
        start_time = time.time()
        sorttype.insertion_sort(data.copy())
        insertion_times.append((time.time() - start_time) * 1000)

            # วัดเวลา selection Sort
        start_time = time.time()
        sorttype.selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Bubble Sort: {bubble_times[-1]:.2f} มิลลิวินาที")
        print(f"  Insertion Sort: {insertion_times[-1]:.2f} มิลลิวินาที")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
    plt.plot(sizes, insertion_times, marker='d', label='Insertion Sort')
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.title('Performance comparison of sorting (Data 0-999). Created By [Student Name]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance.png')
    plt.show()

# เปรียบเทียบประสิทธิภาพ
sorttype=sorting

compare_sort()
```

### บันทึกรูปผลการทดลอง
ผลการเปรียบเทียบ Bubble sort, Insertion sort, Selection sort

![image](https://github.com/user-attachments/assets/da909027-76a1-435a-8439-b6ed6db06415)

ผลการเปรียบเทียบ Selection sort, shell sort, quick sort

![image](https://github.com/user-attachments/assets/48627e5f-dc62-41ee-bd82-760ca1e1be52)

ผลการเปรียบเทียบ shell sort, quick sort, radix sort

![image](https://github.com/user-attachments/assets/c659aed8-eeff-4f72-8066-97aff9265858)

ผลการเปรียบเทียบ shell sort, quick sort, radix sort, couting sort

![image](https://github.com/user-attachments/assets/af5f4506-471e-40af-a40b-9a3375133a1f)

3. ทดลองเปลี่ยนค่าช่วงข้อมูลให้มีขนาดกว้างขึ้น โดยเปลี่ยนค่า 999 เป็น 99999
   ```python
           # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-999
        data = [random.randint(0, 99999) for _ in range(size)]
   ```

   ผลการเปรียบเทียบ Bubble sort, Insertion sort, Selection sort

![image](https://github.com/user-attachments/assets/43eb63e6-5be0-4aa8-ab7d-c5e5719397b1)

ผลการเปรียบเทียบ Selection sort, shell sort, quick sort

![image](https://github.com/user-attachments/assets/90267215-461e-4d99-9d3f-60dfd5847646)

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort
![image](https://github.com/user-attachments/assets/3df0db16-60dc-4a96-ad4e-ace62d0c4ada)



4. ทดลองเปลี่ยนขนาดอินพุต 
   
   ```python
    # ทดสอบกับขนาดข้อมูลต่างๆ
    # sizes = [100,500, 1000, 5000, 10000, 20000]
    sizes = [1000,5000, 10000, 20000, 40000,100000]
    ```

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-999)

![image](https://github.com/user-attachments/assets/cc425666-0dd9-45be-aa5e-b16743c39fca)

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-99999)

![image](https://github.com/user-attachments/assets/109afa9d-cb46-41b9-a019-4a9bdc0cbe61)

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-999999)

![Uploading image.png…]()



### สรุปผลการลอง เปรียบเทียบประสิทธิภาพของการเรียงข้อมูลแต่ละแบบ เมื่อใช้กับข้อมูลขนาดเล็ก ขนาดใหญ่ และข้อมูลที่มีความความแตกต่างของข้อมูลน้อย และความแตกต่างของข้อมูลมาก

```html
ข้อมูลขนาดเล็ก: Bubble Sort และ Selection Sort ทำงานช้าใกล้เคียงกัน
Insertion Sort ทำงานได้เร็วกว่าเมื่อข้อมูลเกือบเรียงแล้ว

ข้อมูลขนาดใหญ่: Bubble Sort และ Insertion Sort ช้ามาก
Selection Sort ทำงานได้เร็วกว่าเล็กน้อย

ข้อมูลที่มีความแตกต่างน้อย (เกือบเรียงแล้ว):Insertion Sort ทำงานได้ดีที่สุด

ข้อมูลที่มีความแตกต่างมาก: Selection Sort ทำงานได้เร็วที่สุด
Bubble Sort และ Insertion Sort ช้ามาก
``` 
