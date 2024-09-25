#!/usr/bin/env python3
# Author: Tandin Wangmo
# Author ID: twangmo12
# Date Created: 2024/09/25

import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <name> <age>")
    sys.exit(0)  # Exit with return code 0

# Assign command line arguments to variables
name = sys.argv[1]  # First argument as the name
age = int(sys.argv[2])  # Second argument as the age, converted to integer

# Print the required output
print(f"Hi {name}, you are {age} years old.")
