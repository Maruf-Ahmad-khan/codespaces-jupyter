n = int(input("Enter the value of n: \n"))
A = []
for i in range(n):
    x = int(input("Enter the list element: \n"))
    A.append(x)

print("The new list is : \n",A)

B = int(input("Enter the Value of B : \n"))
# Add B to all the element in the list A
# let's update the existing list
# A[0] = A[0] + B
# A[1] = A[1] + B
# A[1] = A[1] + B
for idx in range(n):
    A[idx] = A[idx] + B
print("The new list is : \n",A)

