"""
Get user input for name and age
"""
name = input ("What is your name?  ")

if name == "":
    print("You did not enter your name!")
    name = input ("What is your name?  ")

age = int(input("Enter your age: "))

if age >= 17:
    print(f"Hello {name} Welcome to the ADHD self assessment tool \n")
else:
    print(f"Sorry {name}. You must be 17 years or older for this test \n")

