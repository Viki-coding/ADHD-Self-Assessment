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

def get_name():
    """
    Get users name 
    Validate that it is a string and not numbers or no value
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
   

def ask_questions(name):
    """
    Insert dictionary of assessment questions with options
    """
    questions = [
        "Question1: \n How often do you have trouble wrapping up the final details of a project, \n once the challenging parts have been done?\n", 
        "Question 2: \n How often do you have difficulty getting things in order \n when you have to do a task that requires organization?", 
        "Question 3: \n How often do you have problems remembering appointments or obligations?", 
        "Question 4: \n When you have a task that requires a lot of thought, \n how often do you avoid or delay getting started?", 
        "Question 5: \nHow often do you fidget or squirm with your hands or feet \n when you have to sit down for a long time?", "Qestion 6: \n How often do you feel overly active and compelled to do things,\n like you were driven by a motor?"
    ]

    options = ["A. Never", "B. Rarely", "C. Sometimes", "D. Often", "E. Very Often"]
    """
    Apply an integer score against each possible user choice
    """
    scoring = {"a": 0, "b":0, "c": 5, "d":10, "e":15}
    """
    Initialise the total score
    """
    total_score = 0
   
    """
    Iterate through the questions and display the rating the user choices.
    Ask user for the input a, b, c, d, or e.  Apply .upper() to input incase user puts in a lowercase letter
    Ensure user can only put in letters a - e Issue alert otherwise
    """

    for question in questions:
        print("-------------------------------")
        print(question)
        for option in options:
            print(option)
        while True: 
            response = input("Enter (A, B, C, D, E):  ").lower()
            if response in scoring:
                total_score += scoring[response]
                break
            else:
                print("Invalid response.  Please enter A, B, C, D or E")
    
    """
    Display if user has symtoms that are consistent with ADHD
    """
    print("---------------------------------------------------------------------")
    print("----------------------------RESULTS----------------------------------")
    print("-------------------------------------------------------------------\n")

    if total_score <= 10:
        print (f"{name} you scored {total_score} which  means you do not have any symptoms that are consistent with ADHD")
    elif total_score >= 24:
        print (f"{name} you scored {total_score} which  means you have some symptoms that are consistent with ADHD we recommend you look into this further")
    elif total_score >= 25:
        print (f"{name} you scored {total_score} which  means you have symptoms that are consistent with ADHD we recommend you look into this further")
    elif total_score >= 26:
        print (f"{name} you scored {total_score} which  means you have symptoms that are consistent with ADHD we highly recommend you look into this further")

print("---------------------------------------------------------------------")
print("                  Welcome to the ADHD assessment tool              \n")
print("---------------------------------------------------------------------")
print("----------------------------IMPORTANT--------------------------------")
print("  This program was developed as a coding educational challenge \n and is NOT an  accurate ADHD diagnostic tool. \n Contact your GP if you are concerned about ADHD")
print("-------------------------------------------------------------------\n")

if __name__ == '__main__':
    run() 
    
       
  

