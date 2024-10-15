#!/usr/bin/env python3
"""
script.py
Author: Tandin

This script prompts the user for numbers and calculates their average.
It continues to prompt until the user enters an empty string.
Non-numeric inputs are ignored.
"""

def main():
    numbers = []
    
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        
        # If input is an empty string, exit the loop
        if user_input == "":
            break
        
        # If the input is numeric, add it to the list of numbers
        if user_input.isnumeric():
            numbers.append(float(user_input))
    
    # Calculate and print the average of the numbers
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average of the numbers is: {average}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()

