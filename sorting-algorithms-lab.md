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

![Screenshot 2025-03-06 144233](https://github.com/user-attachments/assets/34baae9a-5685-4a61-915e-635db48a26f0)


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
![image](https://github.com/user-attachments/assets/11039f40-5d0e-4065-af72-49fdfb99316c)
![image](https://github.com/user-attachments/assets/9921fc3a-111d-47fc-ab4e-071b4c42c063)


### แบบทดสอบ
1. ปรับปรุงโค้ด ในฟังก์ชัน bubble_sort(arr)  ให้มีประสิทธิภาพมากขึ้นโดยเพิ่มการตรวจสอบว่ามีการสลับตำแหน่งในแต่ละรอบหรือไม่ ถ้าไม่มีการสลับแสดงว่าข้อมูลเรียงลำดับแล้ว สามารถหยุดการทำงานได้ทันที
   ### บันทึกผลแบบทดสอบ
บันทึกโค้ดแบบทดสอบ
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
บันทึกรูปผลแบบทดสอบ
![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/0873e27b-2c45-4e4a-9df6-3ec660904edd)
![image](https://github.com/user-attachments/assets/cd0bbc50-98d0-412c-98df-12ae9fd4f526)


1. ทดสอบกับชุดข้อมูลที่เรียงลำดับแล้ว เช่น `[1, 2, 3, 4, 5,6,7,8,9,10]` และวัดประสิทธิภาพ
### บันทึกผลแบบทดสอบ
```html
ชุดข้อมูลที่เรียงลำดับแล้ว: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] จะไม่มีการสลับในรอบแรก ดังนั้นฟังก์ชันจะหยุดการทำงานทันทีหลังจากการตรวจสอบในรอบแรก
การวัดเวลา: ด้วยการใช้ time.time() ฟังก์ชันจะคำนวณเวลาที่ใช้ในการทำงานของ bubble_sort_with_steps บนชุดข้อมูลที่เรียงลำดับแล้ว
```
บันทึกรูปผลแบบทดสอบ
![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/1773e732-91b7-4980-82f7-d4fa63660b42)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/6ac99ca9-dd0c-4ee0-b304-1d8e07d9e73e)


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
![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/4b888c0c-0504-4007-b888-44cf4a239e06)
![image](https://github.com/user-attachments/assets/3e4ab53b-51dd-4563-bb36-bfd6453d3ff6)


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
        
        # เปลี่ยนจากการเปรียบเทียบ arr[j] > key เป็น arr[j] < key เพื่อการเรียงลำดับจากมากไปน้อย
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
            print(f"  ย้าย {arr[j+2]} ไปทางขวา: {arr}")
        
        arr[j+1] = key
        print(f"  แทรก {key} ลงในตำแหน่ง {j+1}: {arr}")
    
    return arr

# ทดสอบแสดงขั้นตอนการเรียงลำดับจากมากไปน้อย
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
insertion_sort_descending(test_data.copy())

```
![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/c81a8fda-05c3-4e87-9053-f08a057cf25d)
![image](https://github.com/user-attachments/assets/6f4cc932-f589-4e60-bedf-769cc3064796)



2. ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกัน เช่น `[3, 1, 4, 1, 5, 9, 2, 6, 5, 9]` และตรวจสอบผลลัพธ์
### บันทึกผลแบบทดสอบ
```html
 อธิบายผลที่นี่
```
บันทึกรูปผลแบบทดสอบ

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/499ec536-8191-4471-bd5b-c13baa74db19)
![image](https://github.com/user-attachments/assets/0b633a5b-3b2c-49dc-a80a-4625c82c6af9)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/c12f7787-74e5-441f-aab5-91e272590ba2)


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
        max_idx = i  # ค้นหาค่ามากที่สุดในช่วง i ถึง n-1
        print(f"\nรอบที่ {i+1}:")
        print(f"  ข้อมูลปัจจุบัน: {arr}")
        print(f"  ค้นหาค่ามากที่สุดในตำแหน่ง {i} ถึง {n-1}")
        
        for j in range(i+1, n):
            print(f"    เปรียบเทียบ {arr[max_idx]} กับ {arr[j]}", end=" -> ")
            if arr[j] > arr[max_idx]:  # ค้นหาค่ามากที่สุด
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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/e8c044d7-62bc-4f60-b81b-7398f0fc33f0)
![image](https://github.com/user-attachments/assets/057fa796-675e-4924-9c1a-d41cd754e64d)
![image](https://github.com/user-attachments/assets/edcc67e1-8699-4a56-aae3-6c6f73c05f2e)
![image](https://github.com/user-attachments/assets/5412298f-58d8-4465-960e-c6b96062e170)



2. วัดประสิทธิภาพเมื่อทดสอบกับชุดข้อมูลที่เกือบเรียงลำดับแล้ว (nearly sorted data)
### บันทึกผลแบบทดสอบ
```html
ฟังก์ชัน selection_sort_descending_with_steps:จัดเรียงข้อมูลในลำดับจากมากไปหาน้อยโดยใช้ Selection Sortจะแสดงขั้นตอนต่าง ๆ ในแต่ละรอบการค้นหาค่ามากที่สุดและการสลับตำแหน่ง (ถ้ามีการสลับ)
ชุดข้อมูลที่เกือบเรียงลำดับ:ใช้ชุดข้อมูลที่เกือบเรียงแล้ว (แค่สลับตำแหน่ง 8 และ 7 เท่านั้น)
```
บันทึกรูปผลแบบทดสอบ

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/9777904b-4dd3-44a1-936f-1d5649801e98)
![image](https://github.com/user-attachments/assets/87b3649c-714b-4901-a4b7-86727a6a9282)
![image](https://github.com/user-attachments/assets/8d5ff1f1-5a7a-4fc3-a0f1-a16792cb8faa)




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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/e2b402d2-fac6-4eb8-9db2-e598d00c7b83)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/c3b290b7-f832-4ab8-b8bd-0927c96f1447)
![image](https://github.com/user-attachments/assets/66b59fe7-7a27-42af-b5c7-150e59ebbb21)


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

![บันทึกรูปผลการทดลอง]
![image](https://github.com/user-attachments/assets/ae5a2724-4171-4ce4-bcab-a909c1a110e4)


2. ทดสอบกับชุดข้อมูลที่มีค่าซ้ำกันจำนวนมาก และตรวจสอบผลลัพธ์
### บันทึกผลแบบทดสอบ
บันทึกโค้ดและรูปผลแบบทดสอบ
```html
- ลดโอกาสกรณีที่ Quick Sort ทำงานช้า (เมื่อข้อมูลเรียงลำดับแล้วหรือเกือบเรียงลำดับ)
- ทำให้แบ่งข้อมูลได้สมดุลมากขึ้น ส่งผลให้ประสิทธิภาพดีขึ้นในกรณีข้อมูลหลากหลาย
- ลดจำนวนขั้นตอนการเรียกซ้ำ (recursive calls) ในกรณีข้อมูลมีค่าซ้ำกันจำนวนมาก
```

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/d309223e-f801-4874-a686-54b372f3883f)



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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/5d0c8cac-280e-48b1-9ff8-d9774fde4f42)

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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/39d7e19a-35cb-4d05-9782-714f5bc7a6e9)
![image](https://github.com/user-attachments/assets/2cd640f2-0d34-445e-bbfc-725d7183a1a3)
![image](https://github.com/user-attachments/assets/fa620b12-8395-4669-b820-cbb228bd944f)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/81f0c987-640e-4405-becd-aeea768693d3)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/51cd0ff9-7082-4344-aebd-14140cba8c31)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/770d7129-f0b4-443e-ba88-0ab0a4c4dd70)


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

![บันทึกรูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/3184975a-baa7-420d-9663-1ad35ba12b06)
![image](https://github.com/user-attachments/assets/60cdd741-b1aa-4b36-a364-d04d16ea3c0a)
![image](https://github.com/user-attachments/assets/51585ec2-0e91-4f8f-abce-7f3d3da1647b)


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

![บันทึกรูปผลการทดลอง]
![image](https://github.com/user-attachments/assets/d36b1827-7081-4f69-bef3-d85a9d936136)


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

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/6b1c4e5f-dd79-4397-8915-7a10c5939e5f)


ผลการเปรียบเทียบ Selection sort, shell sort, quick sort

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/30f95036-1745-40bf-a8f0-f660237b9e2b)


ผลการเปรียบเทียบ shell sort, quick sort, radix sort

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/c61ed97f-3da3-4108-8a8c-47ed0c83764e)


ผลการเปรียบเทียบ shell sort, quick sort, radix sort, couting sort

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/a2e8e2b6-51e9-4f87-9360-c19b54f33eff)


3. ทดลองเปลี่ยนค่าช่วงข้อมูลให้มีขนาดกว้างขึ้น โดยเปลี่ยนค่า 999 เป็น 99999
   ```python
           # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-999
        data = [random.randint(0, 99999) for _ in range(size)]
   ```

   ผลการเปรียบเทียบ Bubble sort, Insertion sort, Selection sort

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/2e421ecc-aabf-4e5b-803d-8bb7ac5ccd73)



ผลการเปรียบเทียบ Selection sort, shell sort, quick sort

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/076f7add-16b7-45c7-a14b-8fbc44292b04)


    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort
![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/01346f09-d4bb-47bf-8c9b-d7880b9536dd)




4. ทดลองเปลี่ยนขนาดอินพุต 
   
   ```python
    # ทดสอบกับขนาดข้อมูลต่างๆ
    # sizes = [100,500, 1000, 5000, 10000, 20000]
    sizes = [1000,5000, 10000, 20000, 40000,100000]
    ```

    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-999)

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/c3743935-d16f-41ba-9953-d1e428b757dd)


    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-99999)

![รูปผลการทดลอง]

![image](https://github.com/user-attachments/assets/f01ba555-bef8-4bab-b161-0c2ae69d5f11)


    ผลการเปรียบเทียบ shell sort, quick sort, merge sort,radix sort, couting sort (กรณี Data 0-999999)

![รูปผลการทดลอง]
![image](https://github.com/user-attachments/assets/d3cc8cb7-3751-43c8-b4ab-1c31a0419e60)



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
