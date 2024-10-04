# Assignment 5
# Trinity Thompson tyt242
# Marissa Shuchart ms87339

"""
Program that determines the minimum number of lines of code (v) that
Chris has to write before drinking a cup of coffee to complete a programming assignment.
Chris' productivity will decrease by a factor of k each time he drinks
a cup of coffee.
"""

import sys
import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    """Helper function that returns total number of lines written dependent on v and k"""
    total = 0 # Initialize total number of lines written
    factor = 1 # Factor that controls productivity decay (starts at 1)

    while v // factor > 0: # Continue as long as Chris can write lines of code
        total += v // factor # Add number of lines Chris can write given the current productivity
        factor *= k # Decrease productivity

    return total

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    """Function that seearches v linearly"""
    v = 1

    while sum_series(v, k) < n: # While lines written is less than lines need to write, increment v
        v += 1

    return v

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    """Function that performs binary search on values of v"""
  # Initialize a low and high value
    low = 1
    high = n

  # Narrowing search interval while low < high
    while low < high:
        midpoint = (low + high) // 2 # Calculating midpoint

    # If the total lines written with v = midpoint is less than n, reset low boundary
        if sum_series(midpoint, k) < n:
            low = midpoint + 1
        else:
            high = midpoint # Search lower half

    return low

def main():
    """Main function to read input from file and print to output file"""
  # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for i in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
