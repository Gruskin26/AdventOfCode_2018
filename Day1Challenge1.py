import sys

"""
author - Mike Gruskin
email - Mag5856@rit.edu
date - 12/1/18
"""

# Let's create an array
puzzle = []

# Read in line by line until we find a blank line, then we can break
for line in sys.stdin:
    if line == "\n":
        break
    # Add each number to the puzzle without any space
    puzzle.append(line.strip())

# Output the puzzle
print(puzzle)
print()

# Start with a total of zero
total = 0

# For each number in the puzzle, apply the result
for number in puzzle:
    # The operator is the first character
    operator = number[0]
    # The number is the rest of the string
    digit = int(number[1:])
    # Figure out which operator and apply the proper math
    if operator == "+":
        total += digit
    elif operator == "-":
        total -= digit
    else:
        print("error! " + number)

# Finally, output the results
print(total)
