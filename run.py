"""
Get user input for name and age
Error Handling Name - if they put nothing - alert - if they put numbers - alert
Error Handing Age - if they put nothering - alert - if they put string - alert
"""
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
questions = ("Question1: ", "Question2: ", "Question3:")

# questions = ("How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?", "How often do you have difficulty getting things in order when you have to do a task that requires organization?", 
# "How often do you have problems remembering appointments or obligations?", "When you have a task that requires a lot of thought, how often do you avoid or delay getting started?", "How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?", "How often do you feel overly active and compelled to do things, like you were driven by a motor?" )

ratings = ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often")

# answers = []
# questions_num = 0 
# points = 0 

for question in questions:
    print("-------------------------------")
    print(question, flush=True)
    for rating in ratings[questions_num]:
        print(rating)

"""
for question in questions:
    response = input(question + " ")
    if response.lower() == "A" or response == "B":
        points = points + 1

if points == 0:
    print (f"{name} you do not have any sympthoms that are consistent with ADHD")
if points == >=6:
    print (f"{name} you have some sympthoms that are consistent with ADHD we recommend you look into this further")
if points == >=12:
    print (f"{name} you have sympthoms that are consistent with ADHD we recommend you look into this further")
if point == >= 15:
    print (f"{name} you sympthoms that are consistent with ADHD we recommend you look into this further")

"""