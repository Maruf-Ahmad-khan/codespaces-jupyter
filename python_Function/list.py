# list tutorial
num_matches = int(input('Enter How many matches? \n'))
idx = 0

# make empty list
# runs = []
runs = list()
while idx < num_matches:
    x = int(input("Please Enter the score :\n "))
    runs.append(x)
    print('The current runs list is :', runs)
    # get the next match data
    idx +=1