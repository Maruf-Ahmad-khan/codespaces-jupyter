def count(nums):
    if nums == 0:
        return 0
    return 1 + count(nums // 10)

def main():
    nums = int(input("Enter digits: \n"))
    nums = abs(nums)
    print("The count of numbers are : \n", count(nums))
    if nums % 2 == 0:
        print("Numbers are even: \n")
    else:
        print("Numbers are odd : \n")
if __name__ == "__main__":
    main()