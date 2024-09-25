#!/usr/bin/env python3

# Author: Tandin
# Author ID: [your_seneca_id]
# Date Created: 2024/09/25

import sys

# Assign the command line argument to the timer variable
timer = int(sys.argv[1])

while timer > 0:
    print(f"{timer} seconds remaining...")
    timer -= 1

print("Time's up!")
