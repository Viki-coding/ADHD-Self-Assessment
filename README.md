<h1> ADHD ASSESSMENT TOOL</h1>

<h1> Introductino </h1>
This program is an ADHD assessment tool for adults.  

ADHD/ADD Attention Deficit (Hyper) Disorder is a neurodiverse challenge that affects many people.  Many adults don't even realise they have ADHD, many don't reach their full potential due to ADHD.  

In Ireland today, a formal diagnosis is only done through an Educational Psychologist or Psychiatrist. The first step when someone is stuggling is to go to visit their GP.  GP's are not all fully up to speed on how difficult is can be to have ADHD and may not fully be aware of the correct questions to ask to be able to refer their patient to correct health professional. 

There is a misconception that many people who were lazy in school, acted up due to boredom, lacked concentration was becuase they were bold but data shows that many have ADHD and if diagnosed correctly with and correct mangement can lead very full and productive lives.  People with ADHD have 'super-powers' that lead them to be able to hyper-focus on very complex issues, many are highly intelligent but may not have gotten good grades on subjects that bored them but excelled in subjects that did. 

<h2>Description - Project Purpose</h2>

The user is asked 6 questions with options, these options are scored and the result is based on the users responses.  The results indicate if the user has/has not symptoms that may indicate they have ADHD. It is not a formal diagnosis. 

The program aims to allow people/GP's to check if they have some symptoms that may indicate they have ADHD, they can then decide wheather they wish to look into having a formal diagnosis.  

ADHD is heriditary.  A diagnois can help families discover issues they many have been experiencing to be able to gain the correct support and help.  

The target auidence for this tool is people over 17 years of age.  GP's could use this tool to assess if they feel their patient may have ADHD so they can refer them for a more comprehensive diagnosis. The benefit of this tool to be able to get more informed about this condiation and make positive changes to peoples lives.  

Unfortunetly in Ireland the waiting lists for educational pychologists and psychiarists is very long and can be very expensive. To be able to use an on-line tool to rule ADHD in OR out for a patient is hugely important and benefical to both the patient but also the over-burdoned healthcare system. 

<h2>User Demographics - Target audience</h2>

<h2>UX</h2>

<h2>USER STORIES</h2>

<h2>Design Choices</h2>
Colour Scheme
Using a colour contrast checked we checked which font colours stood out best against our base colours.  All receiving good ratings. Graphic illustrated below:

<h2>Typography</h2>

<h2>Wireframes</h2>
<h2>Flow Chart</h2>

<h3>FEATURES</h3>
	(example: nav bars, footer, contact forms, social media icons. )
	Functional Overview 
-	Core functionalities
-	Elements of the project
-	Sets expectations
Navigation and Interaction Points 
-	Offers preview of key elements which are crucial for user interaction.
Assessor wants to see:
Feature Title / Screenshot / Value to the User
<h2>Interaction Points</h2>

<h2>Future Implementation Section</h2>

<h2>Accessibility</h2>

<h2>Technologies Used</h2>
HTML -  CSS -  JS


<h2>Frameworks, Libraries and Programs Used: </h2>

* Balsamiq Wireframes - used to create wireframes
* Git - version control
* Git Pod
* Git Hub - To save and store the files for the website
* Google Fonts - to import fonts onto the website
* Font Awesome for iconography on website
* Favicon.io - to create favicon
* Coolors - checking colour pallets and their contrast abilities with fonts.
* Berme.net - to reduce image sizes and convert to .webp
* Canva - to create logo image
* Am I Responsive - quick tool to check how responsiveness on various devices and creates display
* Responsive tool - https://responsivetesttool.com/
* JSHint to check JS code
* Spell Check

  
<h2>Manual Testing</h2>
(Does the site work as intended?)
FEATURES TESING
LIGHTHOUSE PERFORMANCE
VALIDATOR TESTING
BROWSER COMPATIBILITY
SCREEN SIZE RESPONSIVENESS
BUGS RESOLVED AND NOTE SOLUTIONS AND UNRESOLVED
	
We performed manual testing on the deployed site and also ran our html, css and js codes through validators.
<h3>W3C Validator</h3>
<h3> CSS (Jigsaw) validator</h3>
<h2>JavaScript Code Validator</h2>
<h2> JSON formatter and Validator</h2>

<h2>Quality Assurance</h2>
 (Steps taken to manually test the project
-	Ensures it functions correctly
-	Identifies potential bugs
User Experience Assurance
-	Ensures that the end-users have a smooth experience by addressing potential issues. 
We took a systematic and structural approach to manually test each page to ensure it functions correctly and to help identify potential bugs. We created a specific testing template to ensure and re-check all aspects of the quiz were working correctly as specified with expected and actual outcomes using a methodical approach. We did final testing on the deployed site. 

<h3>Test Evaluation Sheet:</h3>
As shown in the evaluation sheet below we navigated around our site and tested all available features to ensure they were working as intended.

<h2>Lighthouse Testing</h2>
<h2>BUGS</h2>
<u>Solved Bugs</u>
I came across many bugs while testing the quiz, from missing semi-colons to the reset button not being contained within the centre of the quiz box due to styling errors that were fixed and rectified. I put the HTML and CSS code through W3CValidator and fixed all warnings that were shown.  Having chrome development tool open while creating code and inspect console log was very helping with some aspects of the bug finding.  It was also helpful breaking down the problem and  thinking logically - what’s working, what’s not to be able to focus in on the issue. 

One challenging bug was

<h2>User Experience Assurance</h2>
<h2>Deployment Steps</h2>

* The site is Deployed using GitHub Pages
* Login to GitHub
* Go to the projects repository (https://viki-coding.github.io/Guess-the-Flag-Quiz/)
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

Heruko Deployment

Log on to Heruko
https://dashboard.heroku.com/apps
 
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
 
DEPLOY SECTION
Click on the DEPLOY Tab
Choose the Githb deployment method
Confirm that you want to connect to GitHub, gitbub will request your password to connect. 
Click in repo name  and Search for your repository name and select connect. 
Select Enable Automatic Deploys 
Check Choose a branch to deploy is defaulted is MAIN
Click on Display Branch 
 
App will build
Wait until the message ‘App was successfully deployed’ is displayed, click on the view button


<h2>Acknowledging Contributions & Credits</h2>
TITLE OR DESCRIPTION
SOURCE OF LINK
CONTEXT

<b>General good videos and links to teaching of JS:<b>


<b>Videos & Websites that we gained visual clues of how to create the Quiz:</b>

We gained inspiration with the READ.me by watching the video 'Creating your first README with Kera Cudmore' on CI Chanel Lead Library on YouTube and also the video with Lane-Sawyer Thompson on CI Channel on YouTube. Thanks to the on-line tutor, Tom and Sean for their expertise and ability to explain some of the 'challenges' I encountered. Thanks to our very supportive and positive facilitator Laura Maycock and our new facilitator Kay and my Kiwi mentor Dick Vlaanderen. Also found the webinar 'Community Q&A: How to Troubleshoot with Lane-Sawyer Thompson' very helpful approach to how to view looking at the site for bugs and methodically identifying issues.

<h2>Media/Images</h2>
Image by of Green Globes in background by Clicker-Free-Vector-Images from Pixabay
Flag images from Britannica website. 
Image of logo created in Canva using canva template. 

<h2>CONTENT</h2>
The content text for Flags of the World quiz is written by Viki Mulhall. 

<h2>Legal & Ethical Compliance</h2>
This project is for educational purposes only.


