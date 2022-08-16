Automated Testing for Burq Application
### Web Automation Using Selenium Web Driver

Project should be able to work with Python 3 so must have packages would be
pip3
python3
 

### [Project Setup](https://docs.qameta.io/setup)

- Install virtual env using command
      pip3 install virtualenv

- Make virtual env using command

      python3 -m venv env_name

- Activate env

      source env_name/bin/activate
   
- Install requirements

      pip3 install -r requirements.txt

                   
## Execute
Tests can be run using `pytest`

### pytest

- pytest -m "marker name" -vv

#### Execute Single Test Case 

-'pytest run <suite name> <report format> <test case name>'
-'pytest ./burq_ui/tests/test_login_scenarios.py -k "test_login_with_valid_credentials""
            

### Reporting
- report format = html/junit-xml

### Allure Reporting
in order to open allure report we need to install a package named as allure locally in our system
- pip install allure

### Open Allure Reporting
in order to open allure report use command
'allure serve "directory_path"'
directory_path = 'results/iteration_2021_02_15_[00:38]/allure_report'
