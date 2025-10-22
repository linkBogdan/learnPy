# learnPy/day1/file1.py
# This program asks the user for a number and tells if it is even or odd.
# It handles invalid inputs gracefully.

# Keep asking for input until a valid integer is provided.
while True:
    number = input("Enter a number: ") # Ask user for input.
    try:
        number = int(number) # Try to convert input to an integer.
        break # Exit the loop if conversion is successful.
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    

# Use modulo operator to check for evenness.
if number % 2 == 0: 
    print(f"{number} is even.") # Number is divisible by 2
else:
    print(f"{number} is odd.") # Number is not divisible by 2