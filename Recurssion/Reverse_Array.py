# WAP to to reverse an array
from typing import*
def ans(nums, start, end):
    if start > end:
        return
    nums[start], nums[end] = nums[end], nums[start]
    ans(nums, start + 1, end - 1)

def reverseArray(n : int, nums : List[int]) -> List[int]:
    start = 0
    end = n - 1
    ans(nums, start, end)
    return nums

def main():
    nums = [10,20,30,40,50]
    n = len(nums)
    result = reverseArray(n, nums)
    print("The reversed array will be : \n", result)

if __name__ == "__main__":
    main()
