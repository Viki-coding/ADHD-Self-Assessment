def get_age():
    """
    Get age from user
    :return: integer representing  age of user
    Run a while loop to collect valid string of data from the user
    """
    while True:
        age = input("Enter your age and press return:  \n")
        try:
            age = int(age) 
            return age 
        except ValueError:
            print("INVALID! Please enter a valid age")

def get_name():
    """
    Get users name 
    Validate that it is a string and not numbers or no value
    :return: string representing users name
    """
    
    while True:
        name = input("What is your name?  \n")
        if name == "":
            print("You did not enter your name!")
        elif not name.isalpha(): 
            print("Name should only contain letters")
        else:
            print(f"Hello {name} welcome to the ADHD assessment")
            return name           


def run():
    """
    User must be over 17 and under 110 to do test 
    """
    while True:
        age = get_age()    
        if age < 17:
            print("Sorry you must be 17 to do this test! \n")
        elif age > 110:
            print("You're too old to worry about ADHD! \n")
        else:
            name = get_name()
            ask_questions(name)
            break
   
"""
Create a ask_questions function, using the name as a parameter so that we can use the users name value when we are calling the function later displaying their results
"""
def ask_questions(name):
    """
    Insert dictionary of assessment questions with options
    """
    questions = [
        " QUESTION 1: \n \n How often do you have trouble wrapping up the final details of a project, \n once the challenging parts have been done?\n", 
        " QUESTION 2: \n \n How often do you have difficulty getting things in order \n when you have to do a task that requires organization?\n", 
        " QUESTION 3: \n \n How often do you have problems remembering appointments or obligations?\n", 
        " QUESTION 4: \n \n When you have a task that requires a lot of thought, \n how often do you avoid or delay getting started?\n", 
        " QUESTION 5: \n \n How often do you fidget or squirm with your hands or feet \n when you have to sit down for a long time?\n", 
        " QUESTION 6: \n \n How often do you feel overly active and compelled to do things,\n like you were driven by a motor?\n"
    ]

    options = ["A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often \n"]
    """
    Apply an integer score against each possible user choice
    """
    scoring = {"a": 0, "b":0, "c": 1, "d":2, "e":3}
    """
    Initialise the total score
    """
    total_score = 0
   
    """
    Iterate through the questions and display the rating the user chooses.
    Ask user for the input a, b, c, d, or e.  Apply .lower() to input encase user puts in a lowercase letter
    Ensure user can only put in letters a - e Issue error handling otherwise
    """

    for question in questions:
        print("------------------------------------------------------------------------")
        print(question)
        print("------------------------------------------------------------------------")
        for option in options:
            print(option)
        while True: 
            response = input("\n Enter A, B, C, D, or E:  ").lower()
            if response in scoring:
                total_score += scoring[response]
                break
            else:
                print("Invalid response.  Please enter A, B, C, D or E")
    
    """
    Display if user has symptoms that are consistent with ADHD depending on the score range
    """
    print(" ---------------------------------------------------------------------")
    print(" --------------------       RESULTS    -------------------------------")
    print(" ---------------------------------------------------------------------\n")

    if 0 <= total_score <= 3:
        print (f" {name} you scored {total_score}. You do NOT have any symptoms that are consistent with ADHD")
    elif 4 <= total_score <= 6:
        print (f" {name} you scored {total_score}. You have some minor symptoms that are indicative \n with ADHD we recommend you look into this further.")
    elif 7 <= total_score <= 12:
        print (f" {name} you scored {total_score}. You have symptoms that are indicative \n with ADHD we recommend you look into this further.")
    elif 13 <= total_score <= 18:
        print (f" {name} you scored {total_score}. Your high score shows indicative symptoms consistent with ADHD in adults \n we highly recommend you look into this further.")

print("---------------------------------------------------------------------")
print("                  Welcome to the ADHD assessment tool              \n")
print("---------------------------------------------------------------------")
print("----------------------     IMPORTANT    -----------------------------\n")
print(" This program was developed as a coding educational challenge \n and is NOT an  accurate ADHD diagnostic tool. \n Contact your GP if you are concerned about ADHD")
print("---------------------------------------------------------------------\n")

if __name__ == '__main__':
    run() 
    
       
  

