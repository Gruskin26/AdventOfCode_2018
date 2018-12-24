from datetime import datetime
import re

"""
author - Mike Gruskin
email - Mag5856@rit.edu
date - 12/2/18
"""

def getMinute(readRecord):
    """
    Get the minute int from a single record
    :param readRecord: The full record to read
    :return: The minute the record takes place in
    """
    timeString = re.search(dateFinder, readRecord).group(1)
    myTime = datetime.strptime(timeString, format_string)
    return myTime.minute

# An array of guard records
puzzle = []

# Read in the puzzle into an array of records
with open("Day4Input") as file:
    for line in file:
        puzzle.append(line.strip("\n"))

# Sort the list so we get each event in order
puzzle.sort()

# Keep track of our best guard number
# and the total number of minutes they slept
bestGuard = -1
bestTotal = -1

# Use this to format the datetime objects
# in Year-month-day hour:minute form
format_string = "%Y-%m-%d %H:%M"

# Use these regex to find the guard number
# and date from a record
numberFinder = "\#(\d+)"
dateFinder = "\[(.*)\]"

# This will be a dictionary of dictionaries
# Each guard will have a dictionary mapping minutes to
# counts of how often they slept at that minute
guards = {}

# Use these to keep track of the guard,
# the time they started sleeping last,
# and the time they woke up last.

# Once the guard wakes up and we do
# our logging, we can reset the sleep times
# to None. The guard number doesn't change until
# a new guard starts his/her shift
sleepStart = None
sleepEnd = None
currentGuard = None

# Scan each record
for record in puzzle:
    # If we have a new guard, we use this new guard and get their number.
    # The guard will now sleep some number of times during their shift.
    if "begins shift" in record:
        currentGuard = int(re.search(numberFinder, record).group(1))
        # If we don't have a dict entry for this guard yet we want to add one.
        if currentGuard not in guards:
            guards[currentGuard] = {}
            guards[currentGuard]["Total"] = 0
        # This guard has no sleep times yet
        sleepStart = None
        sleepEnd = None
    elif "falls asleep" in record:
        # A sleep has started. The next record will be a wake up.
        sleepStart = getMinute(record)
    elif "wakes up" in record:
        # The guard has fallen woken up. The last record must have started a sleep.
        # Get the minute, and now that the sleep is over, track the statistics of it.
        sleepEnd = getMinute(record)
        # For each minute in their range of sleep,
        # keep track of how many times the guard has slept during
        # that minute, and increment thier total sleep time
        for minute in range(sleepStart, sleepEnd):
            # If the guard has not slept at this minute yet, add it to the dictionary
            if minute not in guards[currentGuard].keys():
                guards[currentGuard][minute] = 1
                guards[currentGuard]["Total"] += 1
            # Otherwise just increment both counts
            else:
                guards[currentGuard][minute] += 1
                guards[currentGuard]["Total"] += 1
            # Now compare to our best count and see if we beat it
            if guards[currentGuard]["Total"] > bestTotal:
                bestGuard = currentGuard
                bestTotal = guards[currentGuard]["Total"]
        # Reset our sleep start and end times since our guard is no longer sleeping
        sleepEnd = None
        sleepStart = None

# Initialize variables to keep track of the best count per minute and best minute
bestCount = -1
bestMinute = -1

# Now that we have the best guard,
# loop through his/her sleep times, finding
# the minute they sleep the most
minList = guards[bestGuard]
for minute in minList.keys():
    # Ignore the Total count key/value
    if minute != "Total":
        # If the count at this minute beat the best,
        # save the new count and minute
        if minList[minute] > bestCount:
            bestCount = minList[minute]
            bestMinute = minute

# Once we get through that loop, we have the best guard, and their most slept minute

print("Best Guard: " + str(bestGuard))
print("Best Minute: " + str(bestMinute))
print("Answer: " + str(bestGuard * bestMinute))