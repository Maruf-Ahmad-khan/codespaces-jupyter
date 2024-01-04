# Write a program to generate fibbonaci series
def generate_Fibonaci_Number(num):
    if num == 1:
        return [0]
    if num == 2:
        return [0,1]
    ans = generate_Fibonaci_Number(num - 1)
    ans.append(ans[-2] + ans[-1])
    return ans

def main():
    num = int(input("Enter a number : \n"))
    result = generate_Fibonaci_Number(num)
    print("The fibbonaci sereies are : \n", result)

if __name__ == "__main__":
    main()