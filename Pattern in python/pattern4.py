'''
____1
___01
__101
_0101
10101


'''
# Taking input for the number of rows
num = int(input("enter a number"))

# Loop through rows from 1 to num
for i in range(1, num + 1):
    # Print spaces before numbers to align the pattern
    for j in range(num - i):
        print(" ", end="")
    
    # Loop through each column in the row
    for j in range(i):
        # Print 1 if the column index is even, else print 0
        if j % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    
    # Move to the next line after each row
    print()
