
# Title: Fermat's Last Theorem Near Misses Finder
# Filename: NearMiss.py
# External Files: None
# External Files Created: None
# Programmers: Franklin Antony, Govardhan Reddy Jakkireddy
# Email: GovardhanReddyJakk@lewisu.edu
# Course Number and Section: CPSC-60500-001
# Date: 22nd September 2024
# Description: This program helps an interactive user search for near misses of the form (x, y, z, n, k) in the formula 
#              x^n + y^n = z^n, where x, y, z, n, k are positive integers, with 2 < n < 12, and 10 <= x, y <= k.
#              The program finds and displays the smallest relative miss for the given range of values.
# Resources: None



import math

# Function to calculate the relative miss
def calculate_relative_miss(x, y, z, n):
    left_side = x**n + y**n
    z_n = z**n
    z_plus_1_n = (z + 1)**n
    
    miss = min(abs(left_side - z_n), abs(z_plus_1_n - left_side))
    relative_miss = miss / left_side
    
    return relative_miss

# Function to find near misses
def find_near_misses(n, k):
    smallest_relative_miss = float('inf')
    best_result = None
    
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            left_side = x**n + y**n
            z = int(math.pow(left_side, 1/n))
            
            relative_miss = calculate_relative_miss(x, y, z, n)
            
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_result = (x, y, relative_miss)
    
    return best_result

def main():
    n = int(input("Enter the value of n (2 < n < 12): "))
    while n <= 2 or n >= 12:
        n = int(input("Invalid input. Please enter a value of n between 3 and 11: "))
    
    k = int(input("Enter the value of k (k > 10): "))
    while k <= 10:
        k = int(input("Invalid input. Please enter a value of k greater than 10: "))
    
    x, y, relative_miss = find_near_misses(n, k)
    
    print(f"{n}\t{k}\tx= {x}, y= {y}, relative diff= {relative_miss:.6f}")

if __name__ == "__main__":
    main()