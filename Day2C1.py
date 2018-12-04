import sys

"""
author - Mike Gruskin
email - Mag5856@rit.edu
date - 12/2/18
"""

# Let's create an array to store our puzzle in
puzzle = []

# Read in line by line until we find a blank line, then we can break
for line in sys.stdin:
    if line == "\n":
        break
    # Add each sequence to the puzzle
    puzzle.append(line.strip())

# Output the puzzle
print(puzzle)

# Keep track of the amount for each type
twoCount = 0
threeCount = 0

# For each code, count the amount of each letter,
# storing the results in a frequencies dictionary
for code in puzzle:
    frequencies = {}
    for letter in code:
        # If we've already seen the letter, increment it's count
        if letter in frequencies:
            frequencies[letter] += 1
        # Otherwise add it to the list with a count of one
        else:
            frequencies[letter] = 1

    # Keep track of if we've added to the two or three count
    addedTwo = False
    addedThree = False

    # Now go through the values and see if any of them are two or three.
    # We can skip the rest of the code if we've already counted it for both
    # the two and the three count, as any box can only count once for each
    if not addedTwo and not addedThree:
        for val in frequencies.values():
            if val == 2 and addedTwo is False:
                twoCount += 1
                addedTwo = True
            if val == 3 and addedThree is False:
                threeCount += 1
                addedThree = True

# Finally, compute the checksum and print it
checksum = twoCount * threeCount
print(checksum)
