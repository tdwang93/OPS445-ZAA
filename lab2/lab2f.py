#!/usr/bin/env python3
# Author: Tandin Wangmo
# Author ID: twangmo12
# Date Created: 2024/09/24

import sys
import time

# Check if an argument is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <number>")
    sys.exit(1)

try:
    countdown_start = int(sys.argv[1])  # Convert the argument to an integer
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

# Countdown loop
while countdown_start > 0:
    print(countdown_start)  # Print the current countdown number
    time.sleep(1)           # Wait for 1 second
    countdown_start -= 1     # Decrease the countdown number

print("blast off!")  # Print "blast off!" after the countdown ends
