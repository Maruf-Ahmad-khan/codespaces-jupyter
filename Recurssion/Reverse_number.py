def reverse(nums):
    if nums == 0:
        return
    print(nums, end= " ")
    reverse(nums - 1)

def main():
    nums = int(input("Enter a number : \n"))
    reverse(nums)

if __name__ == "__main__":
    main()