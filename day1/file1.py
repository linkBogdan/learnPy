# learnPy/day1/file1.py

def get_number():
    """
    Prompt the user to enter a number until a valid integer is provided.
    Returns the integer.
    """
    while True:
        user_input = input("Please enter a number: ")
        try:
            return int(user_input) # Return the valid integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_even(number):
    """
    Check if the provided number is even.
    Returns True if even, False otherwise.
    """
    return number % 2 == 0

# Example usage
number = get_number() # Ask the user for a number
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")            