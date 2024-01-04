def add(x, y):
    return x + y

def square(x):
    return x * x

n1 = square(3)

print('n1 is', n1)

n2 = square(5)
print('n2 is', n2)

print(add(n1, square(9)))

# Return type
def add_2_nums_with_return(n1, n2):
    return n1 + n2

y = add_2_nums_with_return(5,6)
print(y)

if y % 2 == 0:
    print("Addition is even: \n")
else:
    print("Addition is odd: \n")


# Return type
def my_range(end, start = 3):
    print('start', start)
    print('end', end)

    while start < end :
        print(start, end = ' ' )
        start += 1
# my range
my_range(10)
print()
my_range(5)
print()
my_range(1,10)
print()
my_range(start = 1, end = 10)

# Return Type
def func(start = 0, end = 10):
    while start < end:
        print(start)
        start +=1

func(end = 20)
func(start = 5)



# Mix argument
def print_date(day = 1, month = 1, year = 2022, style = 0):
    if style == 0: #American style
        print(month, '/', day, '/', year)

    elif style == 1: #European style
        print(day, '/', month, '/', year)

    else:
        print('Invalid Style')

print_date(day = 30, year = 2023)
print_date(day= 1)

# List
runs = [1,2,3,4,5,10,20,30,40,50,60,70,80,90,100]
print("The runs are: \n")
for i in runs:
    print(i, end=' ')
matches = len(runs)
print("The lenght of the list is : \n", matches)
print("The runs in the last matches : \n", runs[matches - 1])

# append
x = int(input("Enter the run last to the list :\n"))
runs.append(x)
print(runs)

