#ex17

import random

def codename_generator():
    # Ask for user's name
    name = input("What is your name? ")

    # List of codenames
    codenames = ["Fearless Dragon", "Silent Panther", "Mighty Falcon", "Shadow Tiger", "Lone Wolf"]

    # Pick a random codename
    code = random.choice(codenames)

    # Generate a random lucky number between 1 and 100
    lucky_number = random.randint(1, 100)

    # Display the messages
    print(f"{name}, your codename is: {code}")
    print(f"Your lucky number is: {lucky_number}")

# Run the function
codename_generator()
