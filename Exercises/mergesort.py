def mergesort(list):
    if len(list) > 1:

        left = list[:len(list)//2]
        right = list[len(list)//2:]
        
        mergesort(left)
        mergesort(right)
        
        i = 0 #left
        j = 0 #right
        k = 0 #merged
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1    
            
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1   
            
    return list
        
print(mergesort([8,4,5,7,1,4,9,3,8,5,2,9,5]))
