# learnPy/day1/file2.py 
import random

from file1 import get_number # Importing the get_number function from file1.py
print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 20.")
print("Can you guess what it is?")
random_number = random.randint(1, 20)

while True:
    guess = get_number(prompt= "Take a guess: ", stop_on_empty=True)
    if guess is None:
        print("Gave up already? The number was", random_number, ".")
        break
    elif guess < random_number:
        print("You guessed too low.")
    elif guess > random_number:
        print("You guessed too high.")
    elif guess == random_number:
        print("Bingo! It was ", random_number, "!")
        break
    