# learnPy/day1/file2.py 
import random

from file1 import get_number # Importing the get_number function from file1.py
print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 20.")
print("Can you guess what it is?")
random_number = random.randint(1, 20)
guess = get_number()

if guess == random_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {random_number}.")    

