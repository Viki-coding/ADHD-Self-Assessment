<h1> ADHD ASSESSMENT TOOL</h1>

[LIVE LINK SITE:]
(https://adhd-assessment-a99f3a28cb71.herokuapp.com/)

<h1> Introduction </h1>

This program is an ADHD assessment tool for adults.  


> **What is ADHD:** [From ADHD Ireland] 
"ADHD – Attention Deficit Hyperactivity Disorder is a medical/neurobiological condition in which the brain’s neurotransmitter chemicals; noradrenalin and dopamine do not work properly. <b>It is a disorder that, without proper identification, treatment and management, can have serious and long-lasting consequences and/or complications for an individual.  </b> It is a genetic and long-term condition which affects learning and behaviour right through the school years and in many cases beyond into adulthood.  ADHD is a disorder that can co-exist to a greater or lesser degree, with any or other disorders such as dyslexia, autism, learning disorder, dyspraxia, conduct disorder, oppositional defiance disorder.  <b>It is important to note that ADHD is a very treatable condition. If diagnosed and properly treated, people with ADHD can reach their potential and lead happy and successful lives."</b>

In Ireland today, a formal diagnosis is ONLY performed with an Educational Psychologist or Psychiatrist. The first step when someone is stuggling would be to visit their GP.  Not all GP's are fully up to speed on how difficult it is to have ADHD and may not be fully aware of the correct questions to ask to make a premilinary diagnosis prior to referring their patient to the correct health professional. 

There is a misconception that many people who were lazy in school, acted up due to boredom, lacked concentration was because they were bold but data shows that many have ADHD and if diagnosed early with the correct management can lead very full and productive lives.  People with ADHD have 'super-powers' ability to hyper-focus on very complex issues, many are highly intelligent but may not have gotten good grades on subjects that bored them but excelled in subjects that did. 

<h2>Description - Project Purpose - Content </h2>

The main problem many adults have is not being diagnosed AND difficulty to gain access to an already overburdoned healthcare system.  Many adults who have ADHD have struggled for years not even knowing what ADHD is.  By equipping individuals and GPs with more information about ADHD, using this assessment tool, will allow them to get on the path for a formal diagnosis and treatment, leading to improved outcomes. 

>  [From ADD.org ] "Research suggests that the symptoms of ADHD can persist into adulthood, having a significant impact on the relationships, careers, and even the personal safety of patients who may suffer from it. Because this disorder is often misunderstood, many people who have it do not receive appropriate treatment and, as a result, may never reach their full potential. Part of the problem is that it can be difficult to diagnose, particularly in adults." 

Using this tool we want adults to gain easy access to a diagnosis and GP's to have the tools to perform a premlinary screening through a series of questions. 

**Questions & Responses:**
The question content reflects the 6 most indicative questions/responses of sympthoms to ADHD according to the Attention Deficit Disorder Association of America in conjunction with the World Health Organisation (referenced in credits below).

<b>Response Options:</b>

The user is asked 6 questions with the following options:

  - A. Never 
  - B. Rarely
  - C. Sometimes
  - D. Often
  - E. Very Often
   
     These 5 options (a, b, c, d & e) remain the same, creating a clear and concise user required response, creating a familiar interactive understanding, eliciting a postive user experience.  
     
     Each response is scored, at the end of the questionnaire all scores are added up and the result is displayed as a score with some advice to the user.  The results indicate if the user has/has not symptoms that may indicate they have ADHD. 
     
<b>Scoring:</b>

     Scoring system:

     a = 0

     b = 0

     c = 1

     d = 2

     e = 3

<b>Scoring Range: </b>

     - If a user scores between 0-3 they show no signs of ADHD
     - If a user scores between 4-6 they show mild signs of ADHD
     - If a user scores between 7-12 they show signs of ADHD
     - If a user score between 13-18 they show very strong signs of ADHD
    
    IT IS NOT A FORMAL DIAGNOSIS. 

The program aims to allow people/GP's to check if they have some symptoms that may indicate they have ADHD, they can then decide whether they wish to look into having a formal diagnosis.  

ADHD is hereditary.  A diagnosis can help families discover issues they many have been experiencing leading to the correct supports and help.  

<h2>User Demographics - Target audience</h2>
The target audience for this tool is people over 17 years of age.  GP's can use this tool to assess if they feel their patient may have ADHD so they can refer them for a more comprehensive diagnosis. The benefit of this tool to be able to get more informed about this condiation and make positive changes to people's lives.  

Unfortunatley in Ireland the waiting lists for educational psychologists and psychiatrists is very long and can be very expensive. To be able to use an on-line tool to rule ADHD in OR out for a patient is hugely important and beneficial to both the patient but also the over-burdened healthcare system. 

<h2>UX</h2>

<h2>User Stories / Goals: </h2>

 - As a GP user I want to log in easily and see the questions I need to ask my patients.
 - As a GP user I need a relatively quick assessment tool to ascertain whether or not my patient may or may not have ADHD. 
 - As a GP user I want to see the patients score to give me an idea if they have mild symptoms or more significant symptoms. 
 - As a  GP user I want to be able to make informed decisions so I can help my patient be referred to the correct healthcare professional. 
 - As a user at home, I want to assess if I have ADHD, as I find it hard to concentrate and finish tasks, I want to be more informed so that I can seek appropriate healthcare advice. 
 - As a parent at home, I think my 17 year old son may have ADHD, the waiting list for assessment is very long, I would like a quick and straight forward test to assess if he may have it before he sits his state exams so that we can get access to the most appropriate treatment and services. 
- As a user at home, my son/daughter has just been diagnosed with ADHD, I think I may also suffer and would like to check before seeking more formal diagnosis. 

<h2>Design Choices</h2>

**Layout:**
The questions and content are laid out logically and clearly to allow intuitive interaction while giving user feedback.  It is clear to see which question is being displayed and the users response is displayed under that question. 

At the start of our project we created a Flowchart.  The flowchart shows the flow of the program and indicates the decisions the user needs to make in order to take them to the next step.  The flowchart indicates the loops used to manage error handlings such as invalid value inputs. 

The use of lines in the program helps to distinguish the beginning of the program, between the various questions and also distinguished the results section at the end of the page. 


<h2>Flow Chart:</h2>

![ADHD Flowchart](https://github.com/user-attachments/assets/a0e2245f-2678-49af-aa5b-cb7e60473288)



<h3>FEATURES</h3>

**Welcome & Instructions**
This program offers the user clear and informative instructions to begin the program, the age you should be and how to restart the program if required.  A warning that this is not a formal diagnosis is also mentioned here. 


![Welcome and Instructions](https://github.com/user-attachments/assets/d3da624e-4ac0-45d3-be63-87921fd92c10)

**Age Validation**
The program begins with asking the user to enter their age and press return.  The user must be over 17 years old to use this program.  If a user puts in an age <17 or older than >110 a print message is displayed to the user that you must be at least 17 to do this assessment.  If they are older than 110 we tell them they are too old to worry about ADHD. The program then returns the question asking how old they are, if no input is made the program indicates that they must input a value.  Once the user has entered a valid input the program proceeds to the next step - Name input. 

**Name Validation**
The user is then asked their first name. This {name} value will be utilised when we give the user their results to make it a more personal experience.  

If a user puts in numbers then an error message is printed that the input must be valid letters only.  If the user does not enter any value an error message is printed that they must enter their name before moving onto the first question. 

![Screenshot 2024-10-23 at 18 30 51](https://github.com/user-attachments/assets/7c34b156-7d61-459e-accf-3c48adf1d2c3)


**Questions**
There are 6 questions.  The responses are always the same making a good repetitive feedback response for the user to use. The user inserts the letter that they feel most reflects their response to each question.  The user can see which letter they have entered and then press return to enter their score and proceed to the next question. 

After question 6 the responses are calculated and a diagnosis is delivered.

![Question 1](https://github.com/user-attachments/assets/4bff901c-7290-4a28-94bd-c889e67350f4)

![Question 2](https://github.com/user-attachments/assets/23a5b246-05cb-46b8-88ba-fe203fabe6ee)

![Question 3](https://github.com/user-attachments/assets/4f656f79-8df1-4418-8529-5a07bb71ec3b)

![Question 4](https://github.com/user-attachments/assets/47dff52b-243a-4610-ab00-15301e6d9e13)

![Question 5](https://github.com/user-attachments/assets/f88ed8fe-c5b2-4d8f-9cce-bd2b8d77e7c3)

![Question 6](https://github.com/user-attachments/assets/7e6911c9-1404-433b-acff-fe40e77baff1)



**RESULTS**
The results are based on the responses the user has made as shown above in the scoring description. This will be valuable to the user to inform them of their score and diagnosis so that they can proceed or not with seeking a healthcare professional for a formal diagnosis. 

A print comment is displayed using the users first name and their total score indicating whether they have ADHD, have mild symptoms of ADHD, have symptoms of ADHD or have shown a high scoring indicating they have ADHD.

If they have symptoms they are advised to look into it further. 

![RESULTS](https://github.com/user-attachments/assets/01fcc25c-8df1-422e-b7e6-dd6096490a2f)

<h2>Future Implementation Section</h2>

 - Include the 12 extra questions that have been develped by th American ADHD Assocation and W.H.O. to develop the questionnaire to be a more accurate assessment tool in a google sheet linking them to the program.
 - Develop other healthcare question checks such as Peri-menopause / menopause tools to allow women to assess their symptoms in the security of their own home, allowing them to be more informed to be able to make the next decision in their health management.
 - Sexually Transmitted Disease checker - different symptoms pertain to different STD's, often embarrassing - allow users to assess what they may have while educating them about STDs and informing them of the next steps they need to take and the consequces of not getting treatment.
 

<h2>Technologies, Frameworks, Libraries and Programs Used:</h2>

* Python
* Heruko 
* Git - version control
* Git Pod
* Git Hub 
* Spell Check
* CI Python Linter to check for white space and character length.
* Online IDE checker  - for checking pieces of code worked. [IDE Checker] (https://www.online-ide.com/online_python_syntax_checker)

 <h2>Quality Assurance & User Experience Assurance</h2>

We took a systematic and structural approach to manually test each feature to ensure it functions correctly and to help identify potential bugs. We created a specific testing template to ensure and re-check all aspects of the quiz were working correctly as specified with expected and actual outcomes using a methodical approach. We did final testing on the deployed site to ensure our users have a smooth experience by addressing potential issues. 

<h3>Test Evaluation Sheet:</h3>

As shown in the testing sheet below we navigated around our site and manually tested all available features and input fields to ensure they were working as intended. 

We carried out various intensive testing and entered various inputs to see if any errors occurred. Many errors were fixed and works well without any bugs. 


FEATURES TESING:

|                                                                                                  |                                                              | Feature                                                                              | Test Performed                                                                                       | Expected Outcome                                                                                                                                                               | Pass / Fail |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| AGE                                                                                              | 1                                                            | AGE - User asked to enter their age, must be >17 and <110                            | Number 21  entered                                                                                   | Next prompt is displayed asking for name.                                                                                                                                      | TRUE        |
|                                                                                                  | 2                                                            | AGE -  User must be > 17, to do this assessment.                                     | Number 12 entered.  RE-TEST:  -5 entered.                                                            | Statement saying you must be over 17 to do this test.  Then prompts to re- enter age.                                                                                          | TRUE        |
|                                                                                                  | 3                                                            | AGE - User must be < 110 years old to do this assement                               | Number 120 entered. RE-TEST: 5000000 entered.                                                        | Statement saying you're too old to worry about ADHD is displayed.   Then prompts to re-enter age.                                                                              | TRUE        |
|                                                                                                  | 4                                                            | AGE - User must put numerical data in                                                | Random letters entered. Then mixture of letters and numbers entered.                                 | Statement saying INVALID! Please enter a valid age. Then prompts user to re-enter age.                                                                                         | TRUE        |
|                                                                                                  | 5                                                            | AGE - User must put in some data - not just press enter                              | No input entered, return key pressed.                                                                | Statement saying INVALID! Please enter a valid age. Then prompts user to re-enter age.                                                                                         | TRUE        |
| NAME                                                                                             | 6                                                            | NAME - User asked for name.                                                          | viki - all in lowecase entered                                                                       | Welcome message with name entered displayed.                                                                                                                                   | TRUE        |
|                                                                                                  | 7                                                            | NAME - User asked for name.                                                          | Viki - with upper and lower case entered                                                             | Welcome message with name entered displayed.                                                                                                                                   | TRUE        |
|                                                                                                  | 8                                                            | NAME - User asked for name.                                                          | Mixture of letters and numbers entered                                                               | Statement saying invalid data entered.  Please enter alphabetically letters only. Then prompts user to re-enter name.                                                          | TRUE        |
|                                                                                                  | 9                                                            | NAME - User asked for name.                                                          | No name entered, return key pressed.                                                                 | Statement saying you must enter your name. Then prompts user to re-enter name.                                                                                                 | TRUE        |
| QUESTIONS                                                                                        | 10                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | Lower case 'a' entered                                                                               | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 11                                                           | Question 2  presented - with options to enter a, b, c, d or e                        | Uppercase ' B' entered                                                                               | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 12                                                           | Question 3  presented - with options to enter a, b, c, d or e                        | Lower case 'c' entered                                                                               | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 13                                                           | Question 4 presented - with options to enter a, b, c, d or e                         | Lower case 'd' entered                                                                               | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 14                                                           | Question 5 presented - with options to enter a, b, c, d or e                         | Uppercase case 'e' entered                                                                           | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 15                                                           | Question 6 presented - with options to enter a, b, c, d or e                         | Lower case 'e' entered                                                                               | Proceeds to print {name} with their {score} and diagnosis.                                                                                                                     | TRUE        |
|                                                                                                  | 16                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | Lower case 'z' entered                                                                               | Statement saying invalid response,Please enter a, b, c, d, or e. User promted to re-eneter response.                                                                           | TRUE        |
|                                                                                                  | 17                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | Return key pressed with no input                                                                     | Statement saying invalid response,Please enter a, b, c, d, or e. User promted to re-eneter response.                                                                           | TRUE        |
|                                                                                                  | 18                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | Number entered                                                                                       | Statement saying invalid response,Please enter a, b, c, d, or e. User promted to re-eneter response.                                                                           | TRUE        |
|                                                                                                  |                                                              | User feedback of which option they choose, option letter a, b, c, d, or e displayed. | Letter c inserted under question.                                                                    | Letter 'c' displayed                                                                                                                                                           | TRUE        |
| SCORING                                                                                          |                                                              |                                                                                      |                                                                                                      |                                                                                                                                                                                |             |
| Same response scoring                                                                            | 25                                                           | If all responses are 'a' score should be 0                                           | a' selected in for each question                                                                     | Score is 0.  Prints: {name} you scored 0.  You do NOT have any symptoms that are consistent with ADHD                                                                          | TRUE        |
| 26                                                                                               | If all responses are 'b' score should be 0                   | b' selected in for each question                                                     | Score is 0.  Prints: {name} you scored 0. You do NOT have any symptoms that are consistent with ADHD | TRUE                                                                                                                                                                           |
|                                                                                                  | 27                                                           | If all responses are 'c' score should be 6                                           | c' selected in for each question                                                                     | Score is 6. Prints: {Name} you scored 6.<br> You have some mild symptoms that are indicative with<br>ADHD we recommend you look into this further.                             | TRUE        |
|                                                                                                  | 28                                                           | If all responses are 'd' score should be 12                                          | d' selected in for each question                                                                     | Score is 12.  Prints: {Name} you scored 12.<br> You have symptoms that are indicative<br>with ADHD we recommend you look into this further.                                    | TRUE        |
|                                                                                                  | 29                                                           | If all responses are 'e' score should be 18                                          | e' selected in for each question                                                                     | Score is 18.  Prints: {Name} you scored 18.<br> Your high score shows indicative symptoms<br>consistent with ADHD in adults we highly<br>recommend you look into this further. | TRUE        |
| If all answers are between 'a' and 'b' score should be 0.                                        | 19                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | a' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
| 20                                                                                               | Question 2 presented - with options to enter a, b, c, d or e | B' selected                                                                          | Proceeds to next question.                                                                           | TRUE                                                                                                                                                                           |
|                                                                                                  | 21                                                           | Question 3 presented - with options to enter a, b, c, d or e                         | A' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 22                                                           | Question 4 presented - with options to enter a, b, c, d or e                         | b' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 23                                                           | Question 5 presented - with options to enter a, b, c, d or e                         | B' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 24                                                           | Question 6 presented - with options to enter a, b, c, d or e                         | B' selected                                                                                          | Proceeds to results. Prints {Name} you scored 0. You do not have symptoms that are consistent with ADHD. Program ends.                                                         | TRUE        |
| If 2 two 'c' s , two 'd's and two 'e's selected score should be >10 and indicate correct result. | 25                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | e' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
| 26                                                                                               | Question 2 presented - with options to enter a, b, c, d or e | C' selected                                                                          | Proceeds to next question.                                                                           | TRUE                                                                                                                                                                           |
|                                                                                                  | 27                                                           | Question 3 presented - with options to enter a, b, c, d or e                         | d' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 28                                                           | Question 4 presented - with options to enter a, b, c, d or e                         | c' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 29                                                           | Question 5 presented - with options to enter a, b, c, d or e                         | D' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 30                                                           | Question 6 presented - with options to enter a, b, c, d or e                         | c' selected                                                                                          | Proceeds to results.  Prints: {Name} you scored 10.<br> You have symptoms that are indicative<br>with ADHD we recommend you look into this further."                           | TRUE        |
| Mixture of answers                                                                               | 31                                                           | Question 1 presented - with options to enter a, b, c, d or e                         | e' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
| 32                                                                                               | Question 2 presented - with options to enter a, b, c, d or e | a' selected                                                                          | Proceeds to next question.                                                                           | TRUE                                                                                                                                                                           |
|                                                                                                  | 33                                                           | Question 3 presented - with options to enter a, b, c, d or e                         | d' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 34                                                           | Question 4 presented - with options to enter a, b, c, d or e                         | b' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 35                                                           | Question 5 presented - with options to enter a, b, c, d or e                         | D' selected                                                                                          | Proceeds to next question.                                                                                                                                                     | TRUE        |
|                                                                                                  | 36                                                           | Question 6 presented - with options to enter a, b, c, d or e                         | a' selected                                                                                          | Proceeds to results.  Prints: {Name} you scored 7.<br> You have symptoms that are indicative<br>with ADHD we recommend you look into this further."                            | TRUE        |
| Spelling / Grammer                                                                               | 37                                                           | Spelling and grammer in program checked                                              | Spell check performed and proof read                                                                 | No incorrect spellings or grammer                                                                                                                                              | TRUE        |
|                                                                                                  | 38                                                           | Flow chart                                                                           | Text checked for spelling  and proof read                                                            | No incorrect spellings or grammer                                                                                                                                              | TRUE        |
|                                                                                                  | 39                                                           | READ.me                                                                              | Text checked for spelling  and proof read                                                            | No incorrect spellings or grammer                                                                                                                                              | TRUE        |
|                                                                                                  | 40                                                           | Assessment Testing sheet                                                             | Text checked for spelling  and proof read                                                            | No incorrect spellings or grammer                                                                                                                                              | TRUE        |

VALIDATOR TESTING
We performed manual testing on the deployed site and also ran our python code through the CI python linter validator which showed no error messages. 


![CI Python linter](https://github.com/user-attachments/assets/482107a4-e712-46bc-9d07-875d74ba6bcf)

BROWSER COMPATIBILITY

<h2>BUGS</h2>

<h4>Resolved Bugs</h4>
I came across many bugs while testing the quiz, from missing semi-colons to indenting incorrectly.  Using the python code checker while writing the code helped to highlight these.  It was also helpful breaking down the problem and thinking logically - what’s working and what’s not to be able to focus on the issue. It also helped to make my commit messages better as I at the beginning I was testing all my functions out in gitpod, committing, changing them, committing it again so when I started creating the function in the test area first it allowed me the confidence that I knew that function worked. 

<h4>BUG 1 - Uppercase throwing error:</h4>
While doing some testing I had been quickly entering name or letters without using an uppercase for the first name, so during a systematic check when I did capitalise my first name the following error was displayed.  On looking at my code I discovered I used .upper() method rather than .lower() Once amended it worked. 

<img width="475" alt="Capital V not being accepted" src="https://github.com/user-attachments/assets/507826cf-1200-4224-ae3f-4647ff561ae1">


<img width="576" alt="incorrect  upper for response" src="https://github.com/user-attachments/assets/3ae5859f-9d31-4e50-9e00-b7bcf0226610">

<h4>BUG 2 - Response Options repeating </h4>
Unlike other quizzes where there are a few response options to choose from I just wanted to display the same survey/questionnaire responses. I corrected iteration variable and it now works well. 

<img width="528" alt="Repeating response bug" src="https://github.com/user-attachments/assets/c9498de7-f850-4c61-a444-e2689d3441e0">


<h4> BUG 3 - Scoring Range Incorrect and showing incorrect results</h4>
On testing I entered 'e' on all my responses which should of displayed the print message that I had a high likelihood of having ADHD when in fact it displayed to me that I had 'mild' symptoms.  When looking at my code I had only used >= to scores rather than a range.  Once I fixed this it worked correctly.

<img width="545" alt="Results showing incorrect score due to wrong to from scores" src="https://github.com/user-attachments/assets/ba33d17c-2a87-4a99-b1ff-a8a3f31bbcd8">


<h4>BUG 4 - Question dump - not iterating through the questions </h4>
I did not iterate through my questions and options correctly and just got dumped all the questions at once.  After watching many YouTube videos I finally figured it out and it worked correctly. 

<img width="1034" alt="all questions and answers displayed" src="https://github.com/user-attachments/assets/913b3d1c-fec2-4d0c-824f-14ce5144a907">

<h4>BUG 5 - Numbers in name not showing error </h4>
During the testing I inserted a mixture of numbers and letters with the name input field and it did not flag any errors. I amended this using isalpha() method correctly.


<h2>Deployment Steps</h2>

Heruko Deployment

* The site is Deployed using Heruko Deployment
* [Log on to Heruko] (https://dashboard.heroku.com/apps)
* Click on the DEPLOY Tab
* Choose the GitHub deployment method
* Confirm that you want to connect to GitHub, GitHub will request your password to connect. 
* Click in repo name  and Search for your repository name and select connect. 
* Select Enable Automatic Deploys 
* Check Choose a branch to deploy is defaulted is MAIN
* Click on Display Branch 
* App will build
* Wait until the message ‘App was successfully deployed’ is displayed, click on the view button



Select “Create new app”
Name the app something unique
Choose Europe from the dropdown
Click ‘Create App’
Go to the SETTINGS  tab first
In the ‘Config Vars’ section aka environment variables 
In the KEY section type in PORT and the value section type in 8000 – add

IF you build a landmark project that doesn’t use a cred.json file you don’t need to set up config vars otherwise: 
In the KEY section type CREDS (all capital letters) – 
Go to workspace and copy the entire creds.json file and paste it into the value field and add.

 To add other dependencies:
ADD BUILDPACK
Select Python – choose add
Select Node.js – choose add 
(Should be in this order, python first then node.js)
 

* The site is Deployed using GitHub Pages
* Login to GitHub
* Go to the projects repository (https://github.com/Viki-coding/ADHD-Self-Assessment)
* Click on Settings
* Select pages in the left navigation bar
* From SOURCE dropdown select Deploy from a Branch
* Under BRANCH from dropdown select Main Branch and SAVE
* The site is now deployed but may take a few minutes to go live.
* Return to CODE tab of Github repo and wait a few minutes for build to finish, refresh page. This will show on GitHub-pages to see active deployments.

<h2>How to Fork</h2>

* Login to Github
* Go to Project repository
* Click the FORK button top right corner

<h2>How to Clone</h2>

* Log into Github
* Go to project repository
* Click on the code button, select what want to clone HTTPS, SSH or GitHub CLI and copy the link.
* Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory
* Copy 'git clone' into the terminal and paste the link you copied in step 3. Press enter.



<h2>Acknowledging Contributions & Credits</h2>

I revisited the CI Love Sandwiches project as I found it useful in setting up python workspace and heruko. Helped with good practise of using doc strings and the structure of functions. 

Inspired with how to structure questions was based on YouTube video:
[Create a QUIZ GAME with Python - BroCode]
(https://www.youtube.com/watch?v=zehwgTB0vV8&t=311s)

Understanding while loops. 
[While loops in Python are ease - Brocode]
(https://www.youtube.com/watch?v=rRTjPnVooxE)
______________

Understanding parameter values:
(https://www.w3schools.com/python/ref_func_range.asp)

Understanding questions & answers, some inspriration gained from:
[Python quiz game - Bro Code]
(https://www.youtube.com/watch?v=yriw5Zh406s)

Understanding the not.alpha concept from this hangman video:
[Let's code a HANGMAN GAME in Python - Bro Code]
(https://www.youtube.com/watch?v=ag8NtD1e0Kc)

Understanding changing a string to an integer to work out scoring: 
[Credit card validator in Python - Bro Code]
(https://www.youtube.com/watch?v=LqXIJjcRmGI)

Understanding scoring from differenet responses inspired from: 
[CREATE A QUIZ IN PYTHON | learn to code in python for beginners (python tutorial for beginners)
Maya Bello]
(https://www.youtube.com/watch?v=swstbE2bH4k)

**GENERAL EDUCATIONAL VIDEOS / LINKS ON PYTHON THAT WERE USEFUL:**

Insights into how to use Flow Charts for displaying python process:
[Problem Solving with Python]
(https://problemsolvingwithpython.com/09-Loops/09.04-Flowcharts-Describing-Loops/)

How to use pythons main() function correctly and why:
[What is Python's Main Function Useful For?]
(https://www.youtube.com/watch?v=lVUOrPunRxQ)

Inspiration of match case statements:
[Learn Python MATCH-CASE STATEMENTS in 5 minutes! - BroCode]
(https://www.youtube.com/watch?v=L7tT0NZF-Ag)

Understanding how to use .isalpha() method:
[Sting methods in Python are easy - Bro Code]
(https://www.youtube.com/watch?v=tb6EYiHtcXU)

Understanding string methods:
[W3 Schools String Methods]
(https://www.w3schools.com/python/python_ref_string.asp)

Understanding how to format python code and linebreaks:
[Breaking up long lines of code in Python] 
(https://www.pythonmorsels.com/breaking-long-lines-code-python/)

**README inspiration:**
We gained inspiration with the READ.me by watching the video 'Creating your README with Kasia Boguckae' on slack and Community Q&A.

Useful to tips to improve look of Readme:
[Hacks - Workarounds for things not offically supported by Markdown]
(https://www.markdownguide.org/hacks/#:~:text=Basically%2C%20every%20in%20your,sentence%20of%20my%20indented%20paragraph.)

**General good practise and advice on Project 3:** 
Lucy Rush the Assessments Lead chats to our own Lane-Sawyer Thompson to answers some frequently asked questions surrounding Portfolio Project 3. 

**THANKS**
Thanks to the on-line tutors for their expertise and ability to explain some challenges I encountered. Thanks to our very supportive and positive facilitator Kay and my Kiwi mentor Dick Vlaanderen. 


<h2>CONTENT</h2>
The content for the quiz is from the [ADD.org] the Attention Deficit Disorder association of America [Link] (https://add.org/wp-content/uploads/2015/03/adhd-questionnaire-ASRS111.pdf) and myself as my eldest son has ADHD so I unserstand the journey that people have to go through.

This questionnaire is used across America and Canada and the World Health Organisation. [Link] (https://add.org/adhd-questionnaire/)

Definition of ADHD  [From ADHD Ireland] (https://adhdireland.ie/general-information/what-is-adhd/) for introduction text. 

This program is not an accurate diagnostic tool.  In this educational coding project I have only used the first 6 questions on the questionnaire which can tell the patient has symptoms that are highly consistent with ADHD and require further investigation. In the full questionnaire it is advised to answer a further 12 questions, but I felt that was too many for this particular project. 

<h2>Legal & Ethical Compliance</h2>
This project is for educational coding purposes only. It is not a formal diagnostic tool for ADHD. This information also displayed on welcome screen when project first launches. 










