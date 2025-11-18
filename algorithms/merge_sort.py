def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Recursively sort left half
    right = merge_sort(arr[mid:])   # Recursively sort right half
    
    # Conquer (merge)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    expected = [3, 9, 10, 27, 38, 43, 82]
    
    result = merge_sort(arr)
    
    print(f"Input: {arr}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Pass: {result == expected}")