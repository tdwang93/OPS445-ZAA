#!/usr/bin/env python3
# Author: Tandin Wangmo
# Author ID: twangmo12
# Date Created: 2024/09/25

import time

# Set the countdown start value
countdown_start = 10

# Countdown loop
while countdown_start > 0:
    print(countdown_start)  # Print the current countdown number
    time.sleep(1)           # Wait for 1 second
    countdown_start -= 1     # Decrease the countdown number

print("blast off!")  # Print "blast off!" after the countdown ends
