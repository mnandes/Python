def maxSubArray(nums):
    #Variables to keep the partial sum and the maximum available sum
    partial_sum = max_sum = nums[0]
    
    for i in range(1,len(nums)):
        #Does the current number justify reseting the max sum or not? 
        partial_sum = max(nums[i], partial_sum + nums[i])

        #If the sequence improves the max sum, increment it
        max_sum = max(max_sum, partial_sum)
        
        print(partial_sum, max_sum)
    
    
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))