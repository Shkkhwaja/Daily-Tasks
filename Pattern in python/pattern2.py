'''
----*
---**
--***
-****
*****

'''
rows = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, rows + 1):
    # Printing spaces
    for j in range(rows - i):
        print(" ", end="")  # Print space without moving to the next line
    # Printing stars
    for k in range(i):
        print("*", end="")  # Print star without moving to the next line
    
    # Move to the next line after printing spaces and stars for the current row
    print()
