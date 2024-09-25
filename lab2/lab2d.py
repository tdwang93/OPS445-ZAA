#!/usr/bin/env python3
# Author: Tandin Wangmo
# Author ID: twangmo12
# Date Created: 2024/09/25

import sys

# Check if there are exactly 2 additional arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")  # Print usage message if conditions are not met
    sys.exit(0)  # Exit with a return code of 0

# Assign command line arguments to variables
name = sys.argv[1]  # First argument as the name
age = sys.argv[2]   # Second argument as the age (string type)

# Print the required output
print(f"Hi {name}, you are {age} years old.")
