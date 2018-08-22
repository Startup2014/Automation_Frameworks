# Automation_Frameworks
Pycharm-Automation_Framework

regular expression

SQL and casandra queries

basic command of linux

UI Automation

API automation

iOS Device automation--Pycharm , sikuli , see test , appium ,veency

#Setup steps to Pycharm and virtual environment
STEP 1:  cd ~
Step 2 : hg clone git@github.com:Startup2014/Automation_Frameworks.git
Step 3: hg checkout fork_by_<user>
And commit your changes for review all three functions you wrote
optional:
  1.create virtual environment (MacOS):
     pip install virtualenv
     virtualenv env
     source env/bin/activate
     pip install -r test-requirements.txt
  2.use virtual environment in PyCharm:
      1. open project
      2. Menu >> PyCharm >> Preferences >> Project:QA_automation >> Project Interpreter, Project Interpreter = env


#Github Commands:
 git status
 git add .
 git commit -m "COMMIT MSG"
 git show commit (ex: e3a014da373f689443bf044090)
 git log
 git pull origin swati_private_branch  -v
 git push origin swati_private_branch  -v
 Go to Githib and create a new pull request
 
 
 
#####Selenium Setup#####
0. Clone the repo (git clone git@github.com:Startup2014/Automation_Frameworks.git)
1. Download and install Python (2.7.x)
2. Install selenium and dependancies by:
```
pip install -r UI_Selenium_framework/test-requirements.txt
```    
3. (Optional) Download and install PyCharm
4. Download and add to PATH marionette driver:
```
   Chrome:               https://sites.google.com/a/chromium.org/chromedriver/downloads
   Firefox:              https://github.com/mozilla/geckodriver/releases/tag/v0.19.0
   IE (Win Only):        http://www.seleniumhq.org/download/
```
5. Running script locally:
   IDE - .feature or Scenario based
   terminal / prompt - using lettuce runner

