#Naive two_sum
def twoSum(nums, target):

    #iterate through the array twice and check every combination of 2 numbers
    for x in range(len(nums) - 1):
        for y in range(x + 1, len(nums)):
            print(nums[x],nums[y])
            if((nums[x] + nums[y]) == target):
                return [x,y]

#Optimized two_sum using hashtable
def twoSumHashing(nums, target):

    #Use hashtable as a way to store the numbers that were already checked
    hashTable = {}

    for i in range(len(nums)):

        #Check number needed to sum to current number (nums[i])
        complement = target - nums[i]
        #If the needed number has already been analyzed, return the indexes for the numbers
        if complement in hashTable:
            return [hashTable[complement], i]
        
        #If the solution hasn't been found, add number to hashtable
        hashTable[nums[i]] = i

print(twoSumHashing([3,2,4],6))