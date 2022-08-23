def insertion_sort(list):
    index_length = range(1,len(list))
    
    for i in index_length:
        value_to_sort = list[i]
        
        while list[i - 1] > value_to_sort and i > 0:
            list[i], list[i - 1] = list[i - 1], list[i]
            
            i = i - 1
            
    return list

print(insertion_sort([9,4,0,3,7,5,8,2,6,4,8,1,9]))