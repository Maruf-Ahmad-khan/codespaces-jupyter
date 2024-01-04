A = [9,1,2,5,6]
B = 4
def solve(A, B):
    n = len(A)
    for i in range(n):
        A[i] = A[i] + B
    return A
res = solve([9,1,2,5,6], 4)
print("The new Array will be : \n", res)