#!/usr/bin/env python3
# Author: Your Full Name
# Author ID: your_seneca_id
# Date Created: yyyy/mm/dd

import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")  # Updated usage message
    sys.exit(1)  # Exit with return code 1 to indicate an error

# Assign command line arguments to variables
name = sys.argv[1]  # First argument as the name
age = int(sys.argv[2])  # Second argument as the age, converted to integer

# Print the required output
print(f"Hi {name}, you are {age} years old.")
