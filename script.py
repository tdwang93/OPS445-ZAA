# Conversion factors
INCH_TO_CM = 2.54
CM_TO_INCH = 1 / INCH_TO_CM

# Function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * INCH_TO_CM

# Function to convert centimeters to inches
def cm_to_inches(cm):
    return cm * CM_TO_INCH

# Main program
def main():
    print("Welcome to the Conversion Tool!")
    print("Choose a conversion option:")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")

    # Taking the user's choice as input
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        inches = int(input("Enter the value in inches: "))
        print(f"{inches} inches is equal to {inches_to_cm(inches)} centimeters.")
    elif choice == 2:
        cm = int(input("Enter the value in centimeters: "))
        print(f"{cm} centimeters is equal to {cm_to_inches(cm)} inches.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()

