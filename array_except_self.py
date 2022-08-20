def array_except_self(nums):
    n = len(nums)
    result = [1 for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            result[y] = result[y] * nums[x]
    return result

print(array_except_self([1,2,3,4]))

def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    prefix = 1
    #Multiplies array by a right shifted accumulated version of it
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    #Multiplies array by a left shifted accumulated version of it
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    print(res)
    return res
print(productExceptSelf([1,2,3,4]))