# Calculate Factorial 
from typing import *
def Factorial(n : int) -> List[int]:
    ans = []
    fact = 1
    i = 1
    while fact * i <= n:
        fact = fact * i
        ans.append(fact)
        i = i + 1
    return ans

def main():
    n = int(input("Enter a digit: \n"))
    ans = Factorial(n)
    print("The factorial will be : \n", ans)

if __name__ == "__main__":
    main() 