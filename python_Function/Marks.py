# write a program take the input of the subject from the keyboard
# create an empty list and insert the subject marks in the list
subject = int(input("Enter the number of subjects : ? \n"))
marks = []
idx = 0
while idx < subject:
    print("Index is :", idx, 'and subject is: ', subject)
    x = int(input("Please Enter the marks : \n"))
    marks.append(x)
    print("The current marks of the subject is : \n",marks)
    idx +=1