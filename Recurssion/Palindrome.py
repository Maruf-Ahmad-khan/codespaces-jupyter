def isPalindrome(nums):
    if nums < 0 or (nums % 10 == 0 and nums != 0):
        return False
    
    rev = 0
    while nums > rev:
        rem = nums % 10
        rev = rev * 10 + rem
        nums = nums // 10
    return nums == rev or nums == rev // 10

def main():
    nums = int(input("Enter nums : \n"))
    ans = isPalindrome(nums)
    print("The number is palindrome or not : \n", ans)

if __name__ == "__main__":
    main()