def get_age():
    """
    Get age from user
    :return: integer respresenting age of user
    Run a while loop to collect valid string of data from the user
    """
    while True:
        age = input("Enter your age:  \n")
        try:
            age = int(age) 
            return age 
        except ValueError:
            print("INVALID! Please enter a valid age")
            
    

def run():
    """
    User must be over 17 and under 110 to do test 
    """
    while True:
        age = get_age()    
        if age <17:
            print("Sorry you must be 17 to do this test! \n")
        elif age >110:
            print("You're too old to worry about ADHD! \n")
        else:
            get_name()
            break
   

def get_name():
    """
    Get users name 
    Validate that it is a string and not numbers or no value
    """
    
    while True:
        name = input("What is your name?  \n")
        if name == "":
            print("You did not enter your name!")
            name = input ("What is your name?  \n")
        elif not name.isalpha():
            print("Name should only contain letters")
        else:
            print(f"Hello {name} welcome to the the ADHD assessment")
            break 

get_name()

def ask_questions():
    """
    Insert tuple of assessment questions with options
    """
    questions = ("Question1: \n How often do you have trouble wrapping up the final details of a project, \n once the challenging parts have been done?\n", "Question 2: \n How often do you have difficulty getting things in order \n when you have to do a task that requires organization?", 
    "Question 3: \n How often do you have problems remembering appointments or obligations?", "Question 4: \n When you have a task that requires a lot of thought, \n how often do you avoid or delay getting started?", "Question 4: \nHow often do you fidget or squirm with your hands or feet \n when you have to sit down for a long time?", "Qestion 5: \n How often do you feel overly active and compelled to do things,\n like you were driven by a motor?" )

    Options = ("A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often")
    """
    Apply an integer score against each possible user choice
    """
    scoring = {"a": 0, "b":0, "c": 5, "d":10, "e":15}
    """
    Initialise the total score
    """
    total_score = 0

 
    """
    Iterate through the tuple questions and display the rating the user choices.
    Ask user for the input a, b, c, d, or e.  Apply .upper() to input incase user puts in a lowercase letter
    Ensure user can only put in letters a - e Issue alert otherwise
    """

    for question in questions:
        print("-------------------------------")
        print(question, flush=True)
        for option in options:
            print(rating)

        response = input("Enter (A, B, C, D, E):  ").upper()
        total_score += ratings[answer]
 

def main():
    run() 
    ask_questions()
    
if __name__ == '__main__':
    main()





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