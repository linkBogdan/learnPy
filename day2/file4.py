# learnPy/day2/file4.py
# Program to perform operations on a list of numbers collected from the user
from day1.file3 import collect_numbers

prompt = "Enter a number: "
my_numbers = collect_numbers(prompt, stop_on_empty=True, allow_repetition=True)
command = input("Operation to perform on the numbers (sum, average, max, min): ")

print ("You entered: ", my_numbers)

if my_numbers:
    if command.lower() == "sum":
        print("Sum: ", sum(my_numbers))
    elif command.lower() == "average":
        print("Average: ", round(sum(my_numbers)/len(my_numbers), 2))
    elif command.lower() == "max":
        print("Max: ", max(my_numbers))
    elif command.lower() == "min":
        print("Min: ", min(my_numbers))
    else:
        print("Unknown command")
else:
    print("No numbers were entered")