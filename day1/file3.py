# learnPy/day1/file3.py

from file1 import get_number  # Importing the get_number function from file1.py

numbers = []  # List to store user-entered numbers

while True:
    number = get_number(prompt="Enter a number to add to the list (or type 'stop' to finish): ", stop_on_empty=True)
    if number is None:
        break
    numbers.append(number)

# Display the collected numbers after exiting the loop
if not numbers:
    print("No numbers were entered.")
else:
    print("You entered the following numbers:", numbers)