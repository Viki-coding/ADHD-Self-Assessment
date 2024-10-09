"""
Get user input for name and age
Error Handling Name - if they put nothing - alert - if they put numbers - alert
Error Handing Age - if they put nothering - alert - if they put string - alert
"""
# def get_age():
    # """
    # Get age from user
    # :return: integer respresenting age of user
    # Run a while loop to collect valid string of data from the user
    # via terminal, must be a number.  The age must be greater than 17 
    # and less than 110. The loop will continuely request data until data valid. 
    # """
while True:
    try:
        age = int(input("Enter your age:  \n"))
        return(age)) 
    except:
        # Error age is not int
        print("INVALID! Numbers ONLY")
        age = int(input("Enter your age:  "))
    else:
        age <17:
        print("Sorry you must be 17 to do this test" \n")
        age = int(input("Enter your age:  "))

    # return get_age()

name = input ("What is your name?  ")

if name == "":
    print("You did not enter your name!")
    name = input ("What is your name?  ")

age = int(input("Enter your age: "))

if age >= 17:
    print(f"Hello {name} welcome to the ADHD self assessment tool \n")
else:
    print(f"Sorry {name}. You must be 17 years or older for this test \n")


"""
Insert assessment questions
"""
questions = ("Question1: \n How often do you have trouble wrapping up the final details of a project, \n once the challenging parts have been done?\n", "Question 2: \n How often do you have difficulty getting things in order \n when you have to do a task that requires organization?", 
"Question 3: \n How often do you have problems remembering appointments or obligations?", "Question 4: \n When you have a task that requires a lot of thought, \n how often do you avoid or delay getting started?", "Question 4: \nHow often do you fidget or squirm with your hands or feet \n when you have to sit down for a long time?", "Qestion 5: \n How often do you feel overly active and compelled to do things,\n like you were driven by a motor?" )

ratings = ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often")

answers = []
question_num = 0 
points = 0 

"""
Iterate through the tuple questions and display the rating the user choices.
Ask user for the input a, b, c, d, or e.  Apply .upper() to input incase user puts in a lowercase letter
Ensure user can only put in letters a - e Issue alert otherwise
"""

for question in questions:
    print("-------------------------------")
    print(question, flush=True)
    for rating in ratings:
        print(rating)

    response = input("Enter (A, B, C, D, E):  ").upper()
    question_num += 1

"""
for question in questions:
    response = input(question + " ")
    if response.lower() == "A" or response == "B":
        points = points + 1

if points == >5:
    print (f"{name} you do not have any sympthoms that are consistent with ADHD")
if points == >=6:
    print (f"{name} you have some sympthoms that are consistent with ADHD we recommend you look into this further")
if points == >=12:
    print (f"{name} you have sympthoms that are consistent with ADHD we recommend you look into this further")
if point == >= 15:
    print (f"{name} you have sympthoms that are consistent with ADHD we highly recommend you look into this further")

"""