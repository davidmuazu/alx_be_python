size = int(input("Enter the size of the pattern: "))
i = 0
#initialze row counter
while i < size:
    # loop and count each asterisk in current row
    j = 1
    for column in range(size):
        while j <= size:
            print("*", end="")
            j += 1
    #start new line
    print()
    #increment row counter
    i += 1