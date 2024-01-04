def checksorted(nums, n, i):
    if i == n - 1:
        return True
    
    if nums[i + 1] < nums[i]:
        return False
    
    return checksorted(nums, n, i + 1)

def main():
    nums = [1,2,3,4,5]
    n = len(nums)
    i = 0
    issorted = checksorted(nums, n, i)
    if(issorted):
        print("Array is sorted: \n")

    else:
        print("Array is not sorted: \n")

if __name__ == "__main__":
    main()