
# Program: Diamond Star Pattern
# Description: Print a diamond pattern using nested for loops.

# Upper half of the diamond
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()

# Lower half of the diamond
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
