# learnPy/day1/file3.py
# Small program to collect numbers from the user into a list

from file1 import get_number  # Importing the get_number function from file1.py

prompt = "Enter a number to add to the list (or type 'stop' to finish):"
def collect_numbers(prompt, stop_on_empty=True, allow_repetition=True):
    """
    Collect numbers from the user until they choose to stop.
    Returns a list of collected integers.
    """
    numbers = []
    unique_numbers = []
    while True:
        number = get_number(prompt=prompt, stop_on_empty=stop_on_empty)
        if number is None: # This handles the empty input
            break
        numbers.append(number) # Could be optimized based on allow_repetition but kept simple here
        if allow_repetition is False:
            if number not in unique_numbers:
                unique_numbers.append(number)
    return unique_numbers if not allow_repetition else numbers
    
# Main program
if __name__ == "__main__":
    my_numbers = collect_numbers(prompt, stop_on_empty=True, allow_repetition=False)
    print("You entered:", my_numbers)