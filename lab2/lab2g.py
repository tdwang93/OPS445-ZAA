#!/usr/bin/env python3

# Author: Tandin
# Author ID: twangmo12
# Date Created: 2024/09/25

import sys

# Check if an argument was provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Assign the first command line argument to timer
else:
    timer = 3  # Default timer value

while timer > 0:
    print(f"{timer} seconds remaining...")
    timer -= 1

print("Time's up!")
