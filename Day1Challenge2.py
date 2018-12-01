import sys

"""
author - Mike Gruskin
email - Mag5856@rit.edu
date - 12/1/18
"""

# Let's create an array to store our puzzle in
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

# Our total starts at 0, and we initialize the frequencies
# dictionary with a single occurrence of that
total = 0
frequencies = {0: 1}

# Figure out the length of our puzzle
changes = len(puzzle)
# Get a starting index
index = 0

# For each number in the puzzle, apply the result
while True:
    # Since we may have to loop through our input a few times
    # we can use this index % changes to treat our input as
    # circularly linked. Once we pass our last digit this will
    # make it loop back around to the first.
    number = puzzle[index % changes]
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

    # Now figure out if our total has been seen.
    # If so, increment the count
    if total in frequencies:
        frequencies[total] += 1
    # If not, add it with a count of 1
    else:
        frequencies[total] = 1

    # If our total has been found twice now, this is our answer
    if frequencies[total] == 2:
        print(total)
        break

    # If we haven't found our answer, increment the index and repeat
    index += 1
