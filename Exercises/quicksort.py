def quick_sort(sequence):
    length = len(sequence)
    
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    greater = []
    lower = []
    
    for item in sequence:
        if item > pivot:
            greater.append(item)
        
        else:
            lower.append(item)
    
    return quick_sort(lower) + [pivot] + quick_sort(greater) 

print(quick_sort([8,3,9,2,0,5,7,4,8]))