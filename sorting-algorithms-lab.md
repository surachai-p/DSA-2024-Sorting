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
![alt text](image.png)

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
![alt text](image-1.png)
![alt text](image-2.png)

### แบบทดสอบ
1. ปรับปรุงโค้ด ในฟังก์ชัน bubble_sort(arr)  ให้มีประสิทธิภาพมากขึ้นโดยเพิ่มการตรวจสอบว่ามีการสลับตำแหน่งในแต่ละรอบหรือไม่ ถ้าไม่มีการสลับแสดงว่าข้อมูลเรียงลำดับแล้ว สามารถหยุดการทำงานได้ทันที
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดแบบทดสอบ
```python
บันทึกโค้ด แบบทดสอบ
```
บันทึกรูปผลแบบทดสอบ
![alt text](image.png)

2. ทดสอบกับชุดข้อมูลที่เรียงลำดับแล้ว เช่น `[1, 2, 3, 4, 5,6,7,8,9,10]` และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
 นการทำงานครั้งแรกของ bubble_sort จะตรวจสอบข้อมูลทั้งหมด แต่เนื่องจากไม่มีการสลับตำแหน่ง ระบบจะหยุดทำงานในทันที
ดังนั้น เวลาที่ใช้ในการเรียงข้อมูลจะต่ำมาก เพราะฟังก์ชัน bubble_sort จะไม่ต้องทำงานทั้งหมดครบทุกรอบ
ผลที่คาดหวัง:
```
บันทึกรูปผลแบบทดสอบ
![alt text](image.png)


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
![alt text](image.png)

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
![alt text](image.png)
![alt text](image.png)

### แบบทดสอบ
1. ปรับปรุงอัลกอริทึม Insertion Sort ให้รองรับการเรียงลำดับจากมากไปน้อย
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1  

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

import time
# ทดสอบ Insertion Sort แบบเรียงจากมากไปน้อย
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = insertion_sort(test_data.copy())
end_time = time.time()
print("ข้อมูลหลังเรียง (จากมากไปน้อย):", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")

```
บันทึกรูปผลการทดสอบ

![alt text](image.png)

2. ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกัน เช่น `[3, 1, 4, 1, 5, 9, 2, 6, 5, 9]` และตรวจสอบผลลัพธ์
### บันทึกผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
จากการทดลองผลลัพธ์จะเรียงตัวเลขที่ซ้ำกัน จากค่ามากไปน้อย
บันทึกรูปผลแบบทดสอบ

![alt text](image.png)

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

![alt text](image.png)

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
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

### แบบทดสอบ
1. ปรับปรุงอัลกอริทึม Selection Sort ให้รองรับการเรียงลำดับจากมากไปน้อย 
  ### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```python
บันทึกโค้ด แบบทดสอบ
```
def selection_sort_desc(arr):
    n = len(arr)
    
    # วนลูปเพื่อหาค่ามากที่สุดในแต่ละรอบ
    for i in range(n):
        # สมมติว่าตำแหน่งปัจจุบันมีค่ามากที่สุด
        max_idx = i
        
        # หาค่าที่มากกว่าในส่วนที่เหลือ
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:  # เปลี่ยนเป็นหาค่ามากที่สุด
                max_idx = j
        
        # สลับค่าที่มากที่สุดกับตำแหน่งปัจจุบัน
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    return arr

import time

# ทดสอบ Selection Sort แบบเรียงจากมากไปน้อย
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = selection_sort_desc(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง (จากมากไปน้อย):", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")

![alt text](image.png)

2. วัดประสิทธิภาพเมื่อทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว (nearly sorted data)
### บันทึกผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
อัลกอริทึมยังคงทำงาน แม้ข้อมูลเกือบเรียงแล้ว แต่การสลับตำแหน่งลดลง ทำให้เร็วขึ้นเล็กน้อย

บันทึกรูปผลแบบทดสอบ

![alt text](image.png)


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

![alt text](image.png)

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
![alt text](image.png)
![alt text](image-1.png)

### แบบทดสอบ
1. ปรับปรุงการเลือก pivot โดยใช้การเปรียบเทียบตำแหน่งแรก ตำแหน่งตรงกลาง และแหน่งสุดท้าย
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```python
def median_of_three(arr):
    """ เลือก pivot โดยใช้ median ของค่าที่ตำแหน่งแรก, กลาง และสุดท้าย """
    if len(arr) < 3:
        return arr[0]  # ถ้าข้อมูลมีน้อยกว่า 3 ตัว ให้ใช้ตัวแรกเป็น pivot
    
    first, mid, last = arr[0], arr[len(arr) // 2], arr[-1]

    # คืนค่าค่าที่อยู่ตรงกลาง (median)
    if (first < mid < last) or (last < mid < first):
        return mid
    elif (mid < first < last) or (last < first < mid):
        return first
    else:
        return last

def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    # เลือก pivot โดยใช้ median of three
    pivot = median_of_three(arr)
    print(f"{indent}เลือก pivot = {pivot}")
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, middle = {middle}, right = {right}")
    
    # เรียกใช้ Quick Sort กับซ้ายและขวา
    result = quick_sort_with_steps(left, depth + 1) + middle + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
quick_sort_with_steps(test_data.copy())
```
![alt text](image.png)

2. ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกันจำนวนมาก และตรวจสอบผลลัพธ์
### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
ชุดข้อมูลที่ใช้ทดสอบ: ชุดข้อมูลที่มีตัวเลขซ้ำกันหลายตัว เช่น 34, 22, 45, และ 6
การเลือก pivot: ใช้ Median of Three เพื่อเลือก pivot จากตำแหน่งแรก, กลาง, และสุดท้าย
แสดงขั้นตอน: แสดงกระบวนการทั้งหมดของ Quick Sort ที่เลือก pivot แบ่งข้อมูลและผลลัพธ์

![alt text](image.png)


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

![alt text](image-1.png)

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

![alt text](image.png)
![alt text](image-1.png)

### แบบทดสอบ
1. เปรียบเทียบประสิทธิภาพกับ Insertion Sort ปกติเมื่อทดสอบกับชุดข้อมูลขนาดใหญ่
   ### บันทึกผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
Shell Sort จะใช้ระยะห่าง (gap) เพื่อลดการเคลื่อนที่ของข้อมูลให้เร็วขึ้นโดยการใช้การจัดเรียงแบบ Insertion Sort กับกลุ่มข้อมูลที่มีระยะห่างจากกัน
Insertion Sort ทำงานโดยการย้ายข้อมูลที่ยังไม่ถูกต้องไปยังตำแหน่งที่ถูกต้องทีละขั้นตอน ซึ่งจะช้าลงเมื่อข้อมูลมีขนาดใหญ่ขึ้น
บันทึกรูปผลแบบทดสอบ

![alt text](image.png)

2. ทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
สร้างชุดข้อมูลเกือบเรียงลำดับ: เราจะเริ่มต้นด้วยข้อมูลที่เรียงลำดับจากน้อยไปหามาก (range(1, size+1)) และสลับตำแหน่งระหว่างสองตัวในชุดข้อมูลเพื่อทำให้มัน เกือบเรียงลำดับแล้ว.
Shell Sort และ Insertion Sort จะถูกทดสอบกับชุดข้อมูลนี้.
การวัดเวลา: เราจะใช้เวลาในการทำงานของทั้งสองอัลกอริธึมในหน่วยมิลลิวินาที
บันทึกรูปผลแบบทดสอบ

![alt text](image.png)

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

![alt text](image.png)

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

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
merge_sort_with_steps(test_data.copy())

### บันทึกผลการทดลอง
บันทึกรูปผลการทดลอง

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
```

### แบบทดสอบ

1. ทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
สร้างชุดข้อมูลเกือบเรียงลำดับ: เราจะเริ่มต้นด้วยข้อมูลที่เรียงลำดับจากน้อยไปหามาก (range(1, size+1)) และสลับตำแหน่งระหว่างสองตัวในชุดข้อมูลเพื่อทำให้มัน เกือบเรียงลำดับแล้ว.
Merge Sort: ใช้ในการจัดเรียงชุดข้อมูลนี้
การวัดเวลา: เราจะใช้เวลาในการทำงานของ Merge Sort ในหน่วยมิลลิวินาที
บันทึกรูปผลแบบทดสอบ

![alt text](image.png)

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

![alt text](image.png)

ผลการเปรียบเทียบ Selection sort, shell sort, quick sort

![alt text](image.png)

ผลการเปรียบเทียบ shell sort, quick sort, radix sort

![alt text](image.png)

ผลการเปรียบเทียบ shell sort, quick sort, radix sort, couting sort

![alt text](image.png)

3. ทดลองเปลี่ยนค่าช่วงข้อมูลให้มีขนาดกว้างขึ้น โดยเปลี่ยนค่า 999 เป็น 99999
   ```python
           # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-999
        data = [random.randint(0, 99999) for _ in range(size)]
   ```

   ผลการเปรียบเทียบ Bubble sort, Insertion sort, Selection sort

![alt text](image.png)

    ผลการเปรียบเทียบ Selection sort, shell sort, quick sort

![alt text](image.png)

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort
![alt text](image.png)

4. ทดลองเปลี่ยนขนาดอินพุต 
   
   ```python
    # ทดสอบกับขนาดข้อมูลต่างๆ
    # sizes = [100,500, 1000, 5000, 10000, 20000]
    sizes = [1000,5000, 10000, 20000, 40000,100000]
    ```

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-999)

![alt text](image.png)

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-99999)

![alt text](image.png)

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-999999)

![alt text](image.png)


### สรุปผลการลอง เปรียบเทียบประสิทธิภาพของการเรียงข้อมูลแต่ละแบบ เมื่อใช้กับข้อมูลขนาดเล็ก ขนาดใหญ่ และข้อมูลที่มีความความแตกต่างของข้อมูลน้อย และความแตกต่างของข้อมูลมาก

```html
ข้อมูลขนาดเล็ก 
Bubble Sort:
ประสิทธิภาพ: ค่อนข้างช้า เนื่องจากใช้วิธีการเปรียบเทียบทุกคู่ในลูปซ้ำหลายครั้ง
เวลา: สูงที่สุดเมื่อเทียบกับอัลกอริธึมอื่น ๆ
เหมาะสม: ใช้กับข้อมูลขนาดเล็กที่ไม่ซับซ้อน
Insertion Sort:
ประสิทธิภาพ: ทำงานได้ดีมากสำหรับข้อมูลขนาดเล็กหรือเกือบเรียงลำดับแล้ว
เวลา: พอใช้ได้ แต่มีประสิทธิภาพดีกว่า Bubble Sort
เหมาะสม: เหมาะกับข้อมูลที่มีขนาดเล็กและเกือบเรียงลำดับแล้ว
Selection Sort:
ประสิทธิภาพ: คล้ายกับ Bubble Sort แต่มีการเปรียบเทียบเพียงครั้งเดียวในแต่ละรอบ
เวลา: ค่อนข้างช้าในการทำงานกับข้อมูลขนาดเล็ก
เหมาะสม: ใช้ในกรณีที่ต้องการอัลกอริธึมที่มีความซับซ้อนไม่มาก
Quick Sort:
ประสิทธิภาพ: ทำงานได้เร็วที่สุดในขนาดข้อมูลเล็ก โดยเฉพาะเมื่อมีการเลือก pivot ที่เหมาะสม
เวลา: รวดเร็ว
เหมาะสม: เหมาะกับการใช้งานทั่วไปและข้อมูลขนาดเล็ก
Shell Sort:
ประสิทธิภาพ: เร็วกว่า Bubble และ Insertion Sort
เวลา: เร็วพอสมควรในการจัดเรียงข้อมูลขนาดเล็ก
เหมาะสม: ใช้งานได้ดีในข้อมูลขนาดเล็กถึงขนาดกลาง
Merge Sort:
ประสิทธิภาพ: ดี แต่ไม่ได้เร็วที่สุดสำหรับข้อมูลขนาดเล็ก
เวลา: เวลาในการประมวลผลจะสูงกว่า Quick Sort แต่ต่ำกว่า Bubble และ Insertion Sort
เหมาะสม: ใช้ได้ดีในกรณีที่ต้องการการเรียงลำดับที่เสถียร
Radix Sort:
ประสิทธิภาพ: อาจไม่เหมาะสมมากในขนาดข้อมูลเล็ก แต่ทำงานได้ดีในกรณีข้อมูลมีหลายหลัก
เวลา: ดีในกรณีที่ข้อมูลมีจำนวนหลักน้อย
เหมาะสม: ใช้กับข้อมูลที่มีการจำกัดช่วงหรือหลักจำนวนมาก
Counting Sort:
ประสิทธิภาพ: ดีเมื่อมีช่วงค่าจำกัด
เวลา: เร็ว แต่พื้นที่หน่วยความจำสูง
เหมาะสม: ใช้กับข้อมูลที่มีค่าสูงสุดและต่ำสุดจำกัด
ข้อมูลขนาดใหญ่ (เช่น ขนาด 5000 ขึ้นไป)
Bubble Sort:
ประสิทธิภาพ: ไม่เหมาะสมกับข้อมูลขนาดใหญ่ เนื่องจากเวลาในการทำงานเพิ่มขึ้นอย่างรวดเร็ว
เวลา: ช้า
Insertion Sort:
ประสิทธิภาพ: ยังทำงานได้ช้าเมื่อข้อมูลมีขนาดใหญ่
เวลา: ช้า
Selection Sort:
ประสิทธิภาพ: ยังทำงานได้ช้าเหมือนกับ Bubble Sort และ Insertion Sort
เวลา: ช้า
Quick Sort:
ประสิทธิภาพ: ดีที่สุดในขนาดข้อมูลใหญ่
เวลา: เร็วที่สุดในหลายกรณี
Shell Sort:
ประสิทธิภาพ: ดีขึ้นเมื่อขนาดข้อมูลใหญ่ขึ้น แต่ยังไม่เร็วเท่า Quick Sort
เวลา: ดี แต่ไม่เร็วที่สุด
Merge Sort:
ประสิทธิภาพ: เป็นอัลกอริธึมที่เสถียรและมีประสิทธิภาพดีในข้อมูลขนาดใหญ่
เวลา: ค่อนข้างดี
Radix Sort:
ประสิทธิภาพ: ทำงานได้ดีในกรณีที่ข้อมูลมีช่วงค่าสำคัญและจำกัด
เวลา: อาจมีประสิทธิภาพดีกว่า Quick Sort ในบางกรณี
Counting Sort:
ประสิทธิภาพ: ใช้ได้ดีในกรณีที่ข้อมูลมีช่วงที่จำกัด
เวลา: ดี แต่ใช้พื้นที่หน่วยความจำสูง
3. ข้อมูลที่มีความแตกต่างน้อย (เช่น ข้อมูลที่ซ้ำกันมาก)
Bubble Sort:
ประสิทธิภาพ: ดีเมื่อข้อมูลเกือบเรียงลำดับแล้ว
เวลา: เร็วขึ้นในกรณีนี้
Insertion Sort:
ประสิทธิภาพ: เหมาะสมที่สุดสำหรับข้อมูลที่เกือบเรียงลำดับแล้ว
เวลา: เร็ว
Selection Sort:
ประสิทธิภาพ: ไม่ได้รับผลกระทบจากความซ้ำของข้อมูล
เวลา: ช้าเหมือนเดิม
Quick Sort:
ประสิทธิภาพ: สามารถจัดการได้ดี แต่ไม่เหมาะสมที่สุดสำหรับข้อมูลที่มีค่าซ้ำกันมาก
เวลา: เร็ว
Shell Sort:
ประสิทธิภาพ: ดี แต่ไม่เร็วที่สุดเมื่อข้อมูลซ้ำกันมาก
เวลา: เร็วพอสมควร
Merge Sort:
ประสิทธิภาพ: เสถียรและดี
เวลา: ค่อนข้างดี
Radix Sort:
ประสิทธิภาพ: ดีสำหรับข้อมูลที่มีค่าซ้ำกันมาก
เวลา: เร็ว
Counting Sort:
ประสิทธิภาพ: เหมาะสมมากกับข้อมูลที่ซ้ำกันมาก
เวลา: เร็วที่สุดในกรณีนี้
ข้อมูลที่มีความแตกต่างมาก 
Bubble Sort:
ประสิทธิภาพ: ช้า
เวลา: สูง
Insertion Sort:
ประสิทธิภาพ: ไม่เหมาะสมกับข้อมูลที่มีความแตกต่างมาก
เวลา: ช้า
Selection Sort:
ประสิทธิภาพ: ช้า
เวลา: ช้า
Quick Sort:
ประสิทธิภาพ: ทำงานได้ดีในกรณีที่มีการแบ่งข้อมูล
เวลา: เร็ว
Shell Sort:
ประสิทธิภาพ: ทำงานได้ดีขึ้นเมื่อข้อมูลมีการกระจายตัว
เวลา: เร็ว
Merge Sort:
ประสิทธิภาพ: เสถียรที่สุด
เวลา: ค่อนข้างดี
Radix Sort:
ประสิทธิภาพ: ทำงานได้ดี แต่ประสิทธิภาพอาจลดลงหากข้อมูลกระจายตัวมาก
เวลา: พอใช้
Counting Sort:
ประสิทธิภาพ: ไม่เหมาะสมถ้าข้อมูลมีความแตกต่างมาก
เวลา: ช้า
``` 
