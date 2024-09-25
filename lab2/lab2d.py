#!/usr/bin/env python3

import sys

# Check for the correct number of arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <name> <age>")
    sys.exit(1)

# Assign command line arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Print the output
print(f"Hello {name}, you are {age} years old.")
