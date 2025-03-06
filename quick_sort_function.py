def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Improved pivot selection: Median of first, middle, and last
    mid = len(arr) // 2
    first = arr[0]
    middle = arr[mid]
    last = arr[-1]

    # Find the median of first, middle, and last
    if (first <= middle and middle <= last) or (last <= middle and middle <= first):
        pivot = middle
    elif (middle <= first and first <= last) or (last <= first and first <= middle):
        pivot = first
    else:
        pivot = last
    
    # Remove pivot from the array for efficient processing
    arr_without_pivot = arr[: ] 
    arr_without_pivot.remove(pivot)
    
    # Partitioning: Create left and right subarrays
    left = [x for x in arr_without_pivot if x <= pivot]
    right = [x for x in arr_without_pivot if x > pivot]

    # Recursive calls and combining results
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")

    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr

    mid = len(arr) // 2
    first = arr[0]
    middle = arr[mid]
    last = arr[-1]

    if (first <= middle and middle <= last) or (last <= middle and middle <= first):
        pivot = middle
    elif (middle <= first and first <= last) or (last <= first and first <= middle):
        pivot = first
    else:
        pivot = last

    print(f"{indent}เลือก pivot = {pivot} (จาก {first}, {middle}, {last})")
    
    arr_without_pivot = arr[: ] 
    arr_without_pivot.remove(pivot)

    left = [x for x in arr_without_pivot if x <= pivot]
    right = [x for x in arr_without_pivot if x > pivot]

    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")

    result = quick_sort_with_steps(left, depth + 1) + [pivot] + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")

    return result


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