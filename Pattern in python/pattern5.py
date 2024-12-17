'''
*********
-*******
--*****
---***
----*
'''

n = int(input("Enter the number of rows: "))  # Input for number of rows
for i in range(n, 0, -1):  # Loop through rows from n to 1
    print(" " * (n - i), end="")  # Print spaces for the left side
    print("*" * (2 * i - 1))  # Print stars for the inverted pyramid
