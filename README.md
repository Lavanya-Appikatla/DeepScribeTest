CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Maintainers


INTRODUCTION
------------

DeepScribe Project module is designed to automate the browser of the given site
to fill out a patient chart in a sample Electronic Health Records(EHR) System
(URL "https://www.charmhealth.com").


 * For Demo video on this project visit:
  https://drive.google.com/file/d/1yu3fbS8N-Et2Vg7FF6o9sneabHMJvK9k/view?usp=sharing

 * For Git Repository:
   https://www.drupal.org/node/2929013


REQUIREMENTS
------------
- Python
- Selenium webdriver package
- Pytest package
- Compatible Chromedriver.exe


INSTALLATION
------------

Install Python latest version and the required packages through PIP command


CONFIGURATION
-------------

    1. Configure python and set python path in environmental variables of your system
    2. Configure the chromedriver.exe in data.json
    3. Set py.test as runner in Python Integrated Tools in settings
    4. Configure the testcase in Python tests to run the scripts

    Note : I have used OS environ to execute paths in my code. (C:\Users\Lavanya\IdeaProjects\DeepScribe)
           was the project path in my local and python was installed in 'C' drive directly.

           In case of any OS errors during execution. Requesting you to place the project as mentioned in above note format.

How To Run
-----------

    1.Run test_patientrecord.py using pytest


MAINTAINERS
-----------

 * Lavanya Shanmukha

