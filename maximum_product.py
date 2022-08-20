def maxProduct(nums):
    #Variables to keep the partial product and the maximum available product
    partial_product = possible_product = max_product_l = nums[0]
    
    #Iterate left to right
    for i in range(1,len(nums)):
        #Does the current number justify reseting the max product or not? 
        if nums[i - 1] == 0:
            #If there is a zero, skip it, as it will always result in a zero
            partial_product = possible_product = nums[i]
            #Check whether the value after the zero is bigger than before the zero, deciding whether to reset or not the product
            if nums[i] > max_product_l:
                max_product_l = nums[i]
            continue
        
        #Save a possible product due to negative numbers, which create an absolutely bigger number, but comparatively, a smaller one
        possible_product = possible_product * nums[i]
        partial_product = max(nums[i], partial_product * nums[i])

        if(possible_product > partial_product):
            max_product_l = max(max_product_l, possible_product)

        #If the sequence improves the max product, increment it
        max_product_l = max(max_product_l, partial_product)

    #Iterate right to left
    partial_product = possible_product = max_product_r = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        #Does the current number justify reseting the max product or not? 
        if nums[i + 1] == 0:
            #If there is a zero, skip it, as it will always result in a zero
            partial_product = possible_product = nums[i]
            #Check whether the value after the zero is bigger than before the zero, deciding whether to reset or not the product
            if nums[i] > max_product_r:
                max_product_r = nums[i]
            continue
        
        #Save a possible product due to negative numbers, which create an absolutely bigger number, but comparatively, a smaller one
        possible_product = possible_product * nums[i]
        partial_product = max(nums[i], partial_product * nums[i])

        if(possible_product > partial_product):
            max_product_r = max(max_product_r, possible_product)

        #If the sequence improves the max product, increment it
        max_product_r = max(max_product_r, partial_product)
        
    #Check which of the iterations had a better solution and return that as a final solution
    if(max_product_l > max_product_r):
        return max_product_l

    return max_product_r

print(maxProduct([0,1,0]))