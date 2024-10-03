# Assignment 5
# Trinity Thompson tyt242
# Marissa Shuchart ms87339

import sys
import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
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
  v = 1

  while sum_series(v, k) < n: # While lines written is less than lines needed to write, increment v by 1
    v += 1
  
  return v

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
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
