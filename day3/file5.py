

while True:
    print("Hello! Welcome to the program.")
    nume = input("What is your name?: ")
    if not nume:
        print("Name cannot be empty. Please enter your name.")
        continue
    elif any(char.isdigit() for char in nume):
        print("Name cannot contain numbers. Please enter a valid name.")
        continue
    elif len(nume) < 2:
        print("Name is too short. Please enter a valid name.")
        continue
    elif len(nume) > 12:
        print("Name is too long. Please enter a valid name.")
        continue
    elif any(char in "!@#$%^&*()_+=-[]{}|;:'\",.<>?/`~" for char in nume):
        print("Name cannot contain special characters. Please enter a valid name.")
        continue
    elif any(char.isspace() for char in nume):
        print("Name cannot contain spaces. Please enter a valid name.")
        continue
    elif nume[0].islower():
        print("Name must start with an uppercase letter. Please enter a valid name.")
        continue
    else:
        continue_prompt = "What is your age?: "
        while True:
            varsta_input = input(continue_prompt)
            try:
                varsta = int(varsta_input)
                if varsta < 0 or varsta > 120:
                    print("Please enter a valid age between 0 and 120.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for age.")
        break

continue_prompt = "What is your gender?: "
sex = input(continue_prompt)
if sex == "male" or sex == "Male":
    salutation = "Mr."
    skip_gender = False
elif sex == "female" or sex == "Female":
    salutation = "Ms."
    skip_gender = False
else:
    salutation = ""
    skip_gender = True

if not skip_gender:
    if varsta < 18:
        salutation = "young " 
    print(f"Hello, {salutation} {nume}.")
    print(f"You are {varsta} years old.")
    print(f"Your gender is {sex}.")
else:
    print(f"Hello, {nume}.")
    print(f"You are {varsta} years old.")