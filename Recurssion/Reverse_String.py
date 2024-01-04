def Reverse(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start +=1
        end -=1

nums = list(input("Enter a string : \n"))
Reverse(nums)
print("The reverse string will be : \n", ''.join(nums))
