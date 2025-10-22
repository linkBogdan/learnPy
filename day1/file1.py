# learnPy/day1/file1.py
# This program asks the user for a number and tells if it is even or odd.

# Ask the user to enter a number.
number = input("Enter a number: ")

# Convert the input to an integer.
# This wont crash but it will stop the program.
try:
    number = int(number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Use modulo operator to check for evenness.
if number % 2 == 0: 
    print(f"{number} is even.") # Number is divisible by 2
else:
    print(f"{number} is odd.") # Number is not divisible by 2