#Space Efficient Way
def duplicates(nums):
    #Create HashTable
    hashTable = {}
    
    for x in range(len(nums)):
        #If element is already on HashTable, there is a duplicate, return true
        if nums[x] in hashTable:
            return True
        #If element is not in HashTable, add it
        else:
            hashTable[nums[x]] = x
    
    return False


print(duplicates([3,3]))

#Optimized 
def duplicates(nums):
    #Turn array into set, sets have no duplicates by nature
    numset = set(nums)

    #If their lengths are different, means there were duplicates which were deleted when creating the set
    return len(numset) != len(nums)