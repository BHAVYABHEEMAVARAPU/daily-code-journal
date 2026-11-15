def Two_Sum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i] +nums[j]==target:
                return [i,j]
print(Two_Sum([1,3,5,5],10))
