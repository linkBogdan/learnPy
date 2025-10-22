# learnPy/day1/file1.py

def get_number(prompt="Please enter a number (or type 'stop' to exit): ", stop_on_empty=False):
    """
    Prompt the user to enter a number until a valid integer is provided,
    or the user types 'stop' to exit.
    Returns the integer or None if the user wants to stop.
    """
    while True:
        user_input = input(prompt)
        if not user_input:
            if stop_on_empty:
                return None # Stop on empty input
            else:
                print("No input provided.")
                continue # Ignore and reprompt
        
        # Handle 'stop' command
        if user_input.lower() == 'stop':
            return None # Signal to stop
        
        # Try to convert input to an integer
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

# Main program
if __name__ == "__main__":
    while True:
        number = get_number() # Ask the user for a number
        if number is None:
            print("Exiting the program.")
            break # Exit if the user types 'stop'
        if is_even(number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")