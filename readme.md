# Web application automation using selenium python (pytest)

This repository consist of example of selenium python (pytest)

## Installation

 - Python (2.7 or above)
 - Selenium (`pip install -U selenium`)
 - Pytest (`pip install pytest`)
    > For features like fixtures, marker, parallel execution etc.,
 - Pytest html (`pip install pytest-html`)
    > For results in html format

## Usage

> Make sure above mentioned installation is completed

 - Clone or download project
 - Go to root folder
 - Execute tests using pytest command
     - `pytest`
        > All the tests will be executed, result posted in console only
     
     - `pytest --html="results.html"`
        > All the tests executed and html report is created
    
     - `pytest -m employee --html="results.html"`
        > Executes only employee mark tests and report is created

## Example used

 - Uses free [Orange HRM](https://opensource-demo.orangehrmlive.com/index.php/auth/login) application for test

## Framework Explanation

 - Pages:
     - To acheive page object model each page considered as single class
     - Locators and functionality is implemented at page level
     - User has to call respective function using Page object

 - Tests:
     - Each functionality consist of different test suites
     - Each test suite consist of `setup()`, `teardown()` and `tests`
     - `Setup` - Launch browser and navigates to login page
     - `teardown` - Quit browser
     - `test` - Each test may intearcts with multiple pages as per requirements
     - `self.driver` instance is passed for different page files
     - `test` - suite may contain multiple tests, for each test setup and teardown will be executed
    
 - Util:
    - Util consist of reusable code snippets

 - test_data.py:
    - Consist of data like app_url, timeout etc.,

## Reference

For more info on usage or tutorial refer to (samples only)

 - [pytest_overview_medium](https://medium.com/testcult/intro-to-test-framework-pytest-5b1ce4d011ae)
 - [pytest_framework_basic](https://qaboy.com/2018/01/15/automated-framework-using-selenium-with-python/)
 - [selenium_bindings](https://selenium-python.readthedocs.io/)
 - [pytest_tut_guru99](https://www.guru99.com/pytest-tutorial.html)
 - [pytest_in_github](https://github.com/search?q=pytest&type=Repositories)


> Used pycharm to develop scirpts, make respective changes to work in local