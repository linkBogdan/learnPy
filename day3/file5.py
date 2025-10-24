import json

def get_user_info():
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
            while True:
                varsta_input = input("What is your age?: ")
                try:
                    varsta = int(varsta_input)
                    if varsta < 0 or varsta > 120:
                        print("Please enter a valid age between 0 and 120.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for age.")
            break

    gender = input("What is your gender?: ").strip().lower()
    if gender == "male":
        salutation = "Mr."
        skip_gender = False
    elif gender == "female":
        salutation = "Ms."
        skip_gender = False
    else:
        salutation = ""
        skip_gender = True

    if not skip_gender:
        if varsta < 18:
            salutation = "young " + salutation
        print(f"Hello, {salutation} {nume}.")
        print(f"You are {varsta} years old.")
        print(f"Your gender is {gender}.")
    else:
        print(f"Hello, {nume}.")
        print(f"You are {varsta} years old.")

    return {"nume": nume, "varsta": varsta, "gender": gender, "salutation": salutation}


if __name__ == "__main__":
    user_info = get_user_info()
    print(user_info)
    with open("user_info.json", "w") as f:
        json.dump(user_info, f, indent=4)