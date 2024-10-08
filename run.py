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


"""
Insert assessment questions
"""
questions = ["How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?", "How often do you have difficulty getting things in order when you have to do a task that requires organization?", 
"How often do you have problems remembering appointments or obligations?", "When you have a task that requires a lot of thought, how often do you avoid or delay getting started?", "How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?", "How often do you feel overly active and compelled to do things, like you were driven by a motor?" ]

ratings = (("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "Very Often"), 
            ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often"), 
            ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often"), 
            ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often"), 
            ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often"), 
            ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often"))

question_num = 0 

for question in questions:
    print ("================================")
    input(questions)