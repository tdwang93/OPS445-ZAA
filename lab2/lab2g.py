#!/usr/bin/env python3
# Author: Tandin Wangmo
# Author ID: twangmo12
# Date Created: 2024/09/25

import sys

# Check if an argument was entered; if not, set the timer to 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the provided argument for the timer
else:
    timer = 3  # Default timer value

# While loop that repeats until timer equals 0
while timer > 0:
    print(timer)  # Print the current timer value
    timer -= 1    # Decrement the timer

print("blast off!")  # Final message after the countdown
