def Bubble_Sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
        print(nums)

nums = [5,3,8,6,7,2]
print("Unsorted List = ",nums)
Bubble_Sort(nums)
print(nums)